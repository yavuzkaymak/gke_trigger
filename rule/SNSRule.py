from model.Scaler import Scaler
from model.Scaler import KedaPubSub
from .IRule import BaseRule


class SNSRule(BaseRule):

    def __init__(self, ruleName: str):
        self.rule_name = ruleName
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
