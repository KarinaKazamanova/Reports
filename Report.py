from abc import ABC, abstractmethod, classmethod


class Report(ABC):
    @classmethod # не совсем поняла, насколько нужен данный декоратор
    @abstractmethod
    def create_report(self, date):
        pass
        

