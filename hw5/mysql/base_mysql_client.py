from abc import abstractmethod, ABC


class BaseMysqlConnection(ABC):
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

        self.connection = self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def _get_connection(self, is_db_created=False):
        pass
