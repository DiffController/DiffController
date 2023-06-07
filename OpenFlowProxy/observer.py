from abc import ABCMeta, abstractmethod
from logging import getLogger

class OFObserver(metaclass=ABCMeta):

    def __init__(self, observable,logger_name):
        """init params and register for observable

        Args:
            observable (Observable) :
        """
        self.observable = observable
        self.observable.register_observer(self)
        self.logger = getLogger(logger_name+"." + __name__)

    @abstractmethod
    def update(self, msg):
        pass

