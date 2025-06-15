from abc import ABC, abstractmethod

# abstract base class all simulators inherit from 
class BaseSimulator(ABC):
    @abstractmethod
    def generate_paths(self):
        pass
