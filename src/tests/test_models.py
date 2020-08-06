from .. import model
from .. import settings
import persistent
import transaction
import unittest
import ZODB


class TestDecision(unittest.TestCase):

    def setUp(self):
        self.storage = ZODB.FileStorage.FileStorage(settings.DB_PATH_FILENAME)
        self.db = ZODB.DB(storage)
        self.connection = self.db.open()
        self.root = self.connection.root
        self.d = Decision("Select Graph Database to Use")
        self.c1 = Criterium("Fun")
        self.c2 = Criterium("Fast")
        self.c3 = Criterium("Reliable")
        self.d.add_criteria([c1, c2, c3])
        self.root.decision = d
        transaction.commit()

    def tearDown(self):
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
