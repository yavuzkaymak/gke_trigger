from .SQSRule import SQSRule
from .SNSRule import SNSRule
from .IRule import BaseRule
from dataclasses import dataclass, field


@dataclass
class RuleFactory:
    body: dict
    __rule: BaseRule = field(repr=False)

    def __post_init__(self):
        rule_name = self.body.get("ruleName")
        if rule_name == "sns":
            self.__rule = SNSRule(**self.body)
        if rule_name == "sqs":
            self.__rule = SQSRule(**self.body)

    def getRule(self) -> BaseRule:
        return self.__rule
