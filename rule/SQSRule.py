from model.Scaler import Scaler
from model.Scaler.HPA import HPAScaler
from .IRule import BaseRule


class SQSRule(BaseRule):

    def __init__(self, rule_name: str, **kwargs):
        self.rule_name = rule_name
        self._scaler = HPAScaler()


    @property
    def scaler(self) -> Scaler:
        return self._scaler


    def deploy_dataflow(self):
        pass

    def another_common_method(self):
        pass

    @property
    def common_property(self):
        pass
