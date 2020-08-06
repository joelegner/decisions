from . import model
from . import settings
import persistent
import transaction
import unittest
import ZODB


class DecisionTestCase(unittest.TestCase):

    def setUp(self):
        self.storage = ZODB.FileStorage.FileStorage(settings.DB_PATH_FILENAME)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root
        self.d = model.Decision("Select Graph Database to Use")
        c1 = model.Criterium("Fun")
        c2 = model.Criterium("Fast")
        c3 = model.Criterium("Reliable")
        self.d.add_criteria([c1, c2, c3])
        self.root.decision = self.d
        transaction.commit()

    def test_criterium(self):
        self.assertEqual(self.d.criteria[0].__str__(), "Fun")
        self.assertEqual(self.d.criteria[1].__str__(), "Fast")

    def test_decision_basics(self):
        self.assertEqual(self.d.__str__(), "Select Graph Database to Use")

    def tearDown(self):
        self.storage.close()


if __name__ == '__main__':
    unittest.main()
