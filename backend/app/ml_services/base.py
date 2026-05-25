from abc import ABC , abstractmethod

class BaseModel(ABC):

    @abstractmethod
    def update(self, value: float):
        """Update model with new data point"""
        pass

    @abstractmethod
    def predict(self):
        """Return next predicted value"""
        pass

        