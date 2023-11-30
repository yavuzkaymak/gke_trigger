from model.scaler import Scaler
from model.scaler import KedaPubSub
from .irule import BaseRule


class SNSRule(BaseRule):

    def __init__(self, rule_name: str, **kwargs):
        self.rule_name = rule_name
        self._scaler = KedaPubSub(name=self.rule_name, subscriptionName=f"pubsub_{self.rule_name}", authenticationRef="auth-df", scaled_target=f"sns-adapter_{self.rule_name}")

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
