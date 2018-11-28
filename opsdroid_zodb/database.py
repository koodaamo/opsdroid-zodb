import asyncio
import logging
import transaction
import ZODB, ZODB.FileStorage
from persistent.mapping import PersistentMapping
from opsdroid.database import Database

_LOGGER = logging.getLogger(__name__)


class ZODBDatabase(Database):

  async def connect(self, opsdroid=None):
    filepath = self.config.get("database", "opsdroid.fs")
    self.storage = ZODB.FileStorage.FileStorage(filepath)
    self.db = ZODB.DB(self.storage)
    self.connection = self.db.open()
    self.root = self.connection.root

  async def put(self, key, value):
    with transaction.manager:
        self.root[key] = value
    return True

  async def get(self, key):
    with transaction.manager:
        result = self.root[key]
    return result
