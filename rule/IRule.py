from abc import ABCMeta, abstractmethod, abstractstaticmethod


class BaseRule(metaclass=ABCMeta):

    @abstractmethod
    def deploy_dataflow(self):
        pass

    @abstractmethod
    def another_common_method(self):
        """rule spesific implementation"""
        pass

    @property
    @abstractmethod
    def common_property(self):
        pass

