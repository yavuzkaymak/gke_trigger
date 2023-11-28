from .SQSRule import SQSRule
from .SNSRule import SNSRule
from .IRule import BaseRule
from dataclasses import dataclass, field


@dataclass
class RuleFactory:
    body: dict
    rule: BaseRule = field(init=False, default="")

    def getRule(self) -> BaseRule:
        rule_name = self.body.get("ruleName")
        if rule_name == "sns":
            return SNSRule(**self.body)
        if rule_name == "sqs":
            return SQSRule(**self.body)
        else:
            raise Exception(f"Unknown rule type: {rule_name}")
