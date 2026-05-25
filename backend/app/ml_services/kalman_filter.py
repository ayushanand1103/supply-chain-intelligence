from app.ml_services import BaseModel


class KalmanFilter(BaseModel):

    def __init__(
        self,
        process_variance: float = 1e-3,
        measurement_variance: float = 1.0,
        initial_value: float = 0.0
    ):
        """
        process_variance:
            how much system is expected to change (model uncertainty)

        measurement_variance:
            how noisy your real data is

        initial_value:
            starting ETA
        """

        self.process_variance = process_variance
        self.measurement_variance = measurement_variance

        self.estimate = initial_value
        self.error_covariance = 1.0

        self.initialized = False

    def update(self, measurement: float):
        measurement = float(measurement)

        # -----------------------------------
        # STEP 1: Prediction step
        # -----------------------------------
        if not self.initialized:
            self.estimate = measurement
            self.initialized = True
            return

        self.error_covariance += self.process_variance

        # -----------------------------------
        # STEP 2: Kalman Gain
        # -----------------------------------
        kalman_gain = (
            self.error_covariance /
            (self.error_covariance + self.measurement_variance)
        )

        # -----------------------------------
        # STEP 3: Update estimate
        # -----------------------------------
        self.estimate = (
            self.estimate +
            kalman_gain * (measurement - self.estimate)
        )

        # -----------------------------------
        # STEP 4: Update error covariance
        # -----------------------------------
        self.error_covariance = (
            (1 - kalman_gain) * self.error_covariance
        )

    def predict(self):
        if not self.initialized:
            return 0.0

        return self.estimate

    def reset(self):
        self.estimate = 0.0
        self.error_covariance = 1.0
        self.initialized = False