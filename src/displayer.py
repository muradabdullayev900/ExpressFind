import abc


class Displayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def convert_cur(self, record, currency):
        pass

    @abc.abstractmethod
    def minMaxFilter(self, record, min_price, max_price):
        pass

    @abc.abstractmethod
    def sorter(self, record, sort):
        pass

    @abc.abstractmethod
    def Filter(self, record, sort, currency, min_price, max_price):
        pass
