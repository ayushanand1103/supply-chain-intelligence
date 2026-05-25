from collections import deque
from app.ml_services.base import BaseModel

class MovingAverageModel(BaseModel):
    def __init__(self, window_size:int=5):
        self.window_size = window_size
        self.data_points = deque(maxlen=window_size)

    def update(self,value:float):
        self.data_points.append(value)

    def predict(self):
        if not self.data_points:
            return 0
        return sum(self.data_points) / len(self.data_points)
    
    def reset(self):
        """
        Clear history (useful for testing or per-route models)
        """
        self.data_points.clear()

    def get_history(self):
        """
        Debugging helper
        """
        return list(self.data_points)
    