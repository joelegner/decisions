from json import JSONEncoder
import os
import persistent
import transaction
import ZODB
import ZODB.FileStorage
from . import settings


class Criterium(persistent.Persistent):

    def __init__(self, name="Unnamed Criterium"):
        self.name = name

    def __str__(self):
        return "%s" % (self.name)


class Comparison(persistent.Persistent):

    def __init__(self, left, right, value=1.0):
        self.left = left
        self.right = right
        self._value = value

    def __repr__(self):
        return "<Comparison(left=%s, right=%s, value=%.3f)>" % (self.left, self.right, self.value)

    def set_value(self, newvalue):
        if isfloat(newvalue):
            if newvalue >= 0.0 and newvalue <= 1.0:
                self._value = newvalue
                self._p_changed = True

    def get_value(self):
        return self._value


class Decision(persistent.Persistent):

    def __init__(self, name="Undefined Decision"):
        self.name = name
        self.criteria = []

    def __repr__(self):
        return "<Decision(oid=%s, name='%s')>" % (self._p_oid, self.name)

    def add_criterium(self, name):
        new_criterium = Criterium(name=name)
        self.criteria.append(new_criterium)
        self._p_changed = True
        return new_criterium

    def add_criteria(self, criteria):
        for c in criteria:
            self.add_criterium(c)

    def save(self):
        pass


if __name__ == "__main__":
    storage = ZODB.FileStorage.FileStorage(settings.DB_PATH_FILENAME)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    d = Decision("Select Graph Database to Use")
    c1 = Criterium("Fun")
    c2 = Criterium("Fast")
    c3 = Criterium("Reliable")
    d.add_criteria([c1, c2, c3])
    root.decision = d
    transaction.commit()

    for c in d.criteria:
        print(c)
        print(c._p_oid)
        print("------------------")

    storage.close()
