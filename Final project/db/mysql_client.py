from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.orm_query_builder import OrmQueryBuilder


class MysqlConnection:
    def __init__(self, host, port, user, password, db_name):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name

        self.connection = self._get_connection()

        session = sessionmaker(bind=self.connection)
        self.session = session()

        self.builder = OrmQueryBuilder(
            connection=self.connection,
            session=self.session,
        )

    def _get_connection(self):
        engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db_name=self.db_name,
        ))

        return engine.connect()
