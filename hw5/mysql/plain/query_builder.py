from mysql.base_builder import BaseQueryBuilder
from mysql.plain.entity.log_data import LogDataEntity


class PlainQueryBuilder(BaseQueryBuilder):
    def __init__(self, logs_table_name):
        self.table_name = logs_table_name

    def create_logs_table(self):
        """ Создание таблицы с логами """
        return f"""
        CREATE TABLE IF NOT EXISTS `{self.table_name}` (
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        `ip` VARCHAR(30) NOT NULL ,
        `time` DATETIME NOT NULL ,
        `method` VARCHAR(20) NOT NULL ,
        `url` VARCHAR(255) NOT NULL ,
        `status_code` INT NOT NULL ,
        `bytes_sent` INT NOT NULL
        ) CHARSET=utf8
        """

    def insert_log(self, log: LogDataEntity):
        """ Вставка лога """
        return f"""
        INSERT INTO `{self.table_name}` VALUE (
        NULL ,
        '{log.ip}' ,
        '{log.time}' ,
        '{log.method}' ,
        '{log.url}' ,
        {log.status_code} ,
        {log.bytes_sent}
        )
        """

    def select_logs(self):
        """ Выбор логов """
        return f"SELECT * FROM {self.table_name}"
