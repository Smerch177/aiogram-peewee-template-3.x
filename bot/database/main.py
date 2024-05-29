import peewee_async
from data import config
import logging

database = peewee_async.PostgresqlDatabase(
    database=config.DB_NAME,
    user=config.DB_USER,
    host=config.DB_HOST,
    port=config.DB_PORT,
    password=config.DB_PASSWORD,
)

objects = peewee_async.Manager(database)

# logging
logger = logging.getLogger('peewee_async')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


database.set_allow_sync(False)

