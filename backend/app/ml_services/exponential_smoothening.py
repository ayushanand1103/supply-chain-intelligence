from app.ml_services.base import BaseModel

class ExponentialSmoothingModel(BaseModel):
    def __init__(self , alpha : float=0.5):
        """
        alpha:
            0 → slow reaction (stable)
            1 → fast reaction (reactive)
        """
        self.alpha = alpha
        self.value = None
        
        def update(self , value : float):
            value = float(value)
            if self.value is None:
                self.value = value
            else:
                self.value = self.alpha * value + (1 - self.alpha) * self.value

    def predict(self):
        if self.value is None:
            return 0.0
        return self.value
    
    def reset(self):
        self.value = None