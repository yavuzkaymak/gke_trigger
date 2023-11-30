from pydantic import BaseModel, Extra, ConfigDict
from importlib import import_module
from .irule import BaseRule
from .sqs import SQSRule
from .sns import SNSRule


class RuleFactory(BaseModel):
    rule_name: str
    rule_type: str
    model_config = ConfigDict(use_enum_values=True, extra=Extra.allow)

    def getRule(self) -> BaseRule:
        ## way - 1 with reflection
        # _rule = self.rule_type.upper() + "Rule"
        # module = import_module(self.__module__.split(".")[0])
        # try:
        #     class_ = getattr(module, _rule)
        #     return class_(**self.__dict__)
        # except AttributeError:
        #     raise Exception(f"{self.rule_type} is not a registered rule type")

        ## way - 2 simple if

        # if self.rule_type == "sns":
        #     _rule = SNSRule
        # elif self.rule_type == "sqs":
        #     _rule = SQSRule
        # else:
        #     raise Exception(f"{self.rule_type} is not a registered rule type")
        # return _rule(**self.__dict__)


        ## way 3 - hashmap

        ## create this var outside the class

        rule_type_map = {
            "sns": SNSRule,
            "sqs": SQSRule
        }

        ## EAFP - easier to ask for forgiveness than permission
        try:
            _rule = rule_type_map[self.rule_type]
            return _rule(**self.__dict__)
        except KeyError:
            raise Exception(f"{self.rule_type} is not a registered rule type")