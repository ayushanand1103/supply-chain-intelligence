from app.database import SessionLocal
from app.models.warehouse import Warehouse


from app.ml_services.moving_average import  moving_average
from app.ml_services.exponential_smoothening import ExponentialSmoothingModel
from app.ml_services.kalman_filter import KalmanFilter

db = SessionLocal()

class ETAService:
    def __init__(self):
        #Seperate models for different singnals
        self.ma = moving_average(window_size=5)
        self.es = ExponentialSmoothingModel(alpha=0.5)
        self.kf = KalmanFilter(process_variance=1e-3, measurement_variance=1.0, initial_value=0.0)

    def get_warehouse(self , db , warehouse_id : int):
        return db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    
    def compute_base_eta(self, distance_km: float, speed_kmph: float = 60):
        """
        Physics-based ETA from OSRM distance
        """
        return distance_km / speed_kmph
    
    def get_eta(self,
                source_id:int,
                dest_id:int,
                distance_km:float,
                duration_hours:float=None):
        db = SessionLocal()

        try:
            source = self.get_warehouse(db, source_id)
            dest = self.get_warehouse(db, dest_id)

            if not source or not dest:
                return {
                    "error": "Invalid warehouse IDs"
                }
            
            ## Base ETA
            base_eta = self.compute_base_eta(distance_km)
            
            if duration_hours is not None:
                base_eta = duration_hours

             # -----------------------------------
            # MODEL 1: MOVING AVERAGE
            # -----------------------------------
            self.ma.update(base_eta)
            ma_value = self.ma.predict()

            # -----------------------------------
            # MODEL 2: EXPONENTIAL SMOOTHING
            # -----------------------------------
            self.es.update(base_eta)
            es_value = self.es.predict()

            # -----------------------------------
            # MODEL 3: KALMAN FILTER
            # -----------------------------------
            self.kf.update(base_eta)
            kf_value = self.kf.predict()

            # -----------------------------------
            # ENSEMBLE WEIGHTING
            # -----------------------------------
            final_eta = (
                0.2 * ma_value +
                0.3 * es_value +
                0.5 * kf_value
            )

            return {
                "source_id": source_id,
                "destination_id": dest_id,
                "distance_km": round(distance_km, 2),

                "base_eta_hours": round(base_eta, 2),
                "ma_eta": round(ma_value, 2),
                "es_eta": round(es_value, 2),
                "kf_eta": round(kf_value, 2),

                "final_eta_hours": round(final_eta, 2)
            }

        finally:
            db.close()
        
