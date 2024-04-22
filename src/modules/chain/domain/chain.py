from datetime import datetime

from peewee import CharField, DateTimeField, AutoField, Model

from src.core.base_domain import BaseDomain
from src.infra.database.mysql.mysql_connection import db


class ChainModel(Model):
    id = AutoField(primary_key=True)
    pid = CharField(191, unique=True)
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    model = CharField(191, unique=True)

    class Meta:
        database = db
        db_table = "Chain"


class ChainDomain(BaseDomain):
    model: str
