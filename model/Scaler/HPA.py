
from dataclasses import dataclass
from IScaler import Scaler

@dataclass
class HPAScaler(Scaler):
    @property
    def manifest(self):
        return "foo"