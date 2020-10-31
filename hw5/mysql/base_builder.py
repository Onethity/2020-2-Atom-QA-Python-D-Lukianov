from abc import ABC, abstractmethod


class BaseQueryBuilder(ABC):
    @abstractmethod
    def create_logs_table(self):
        pass

    @abstractmethod
    def insert_log(self, log):
        pass

    @abstractmethod
    def select_logs(self):
        pass
