from .IRule import BaseRule
from pydantic import BaseModel, Extra, ConfigDict
from importlib import import_module


class RuleFactory(BaseModel):
    rule_name: str
    rule_type: str
    model_config = ConfigDict(use_enum_values=True, extra=Extra.allow)

    def getRule(self) -> BaseRule:
        _rule = self.rule_type.upper() + "Rule"
        module = import_module(self.__module__.split(".")[0])
        try:
            class_ = getattr(module, _rule)
            return class_(**self.__dict__)
        except AttributeError:
            raise Exception(f"{self.rule_type} is not a registered rule type")
