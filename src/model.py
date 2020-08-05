from json import JSONEncoder
import os
import persistent
import transaction
import ZODB
import ZODB.FileStorage
import settings


class Criterium(persistent.Persistent):

    def __init__(self, name="Unnamed Criterium"):
        self.name = name

    def __repr__(self):
        return "<Criterium(oid=%s, name='%s')>" % (self._p_oid, self.name)


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

    def __repr__(self):
        return "<Decision(oid=%s, name='%s')>" % (self._p_oid, self.name)

    def add_criterium(self, name):
        new_criterium = Criterium(name=name)
        new_criterium.decision = self
        return new_criterium

    def save(self):
        pass


if __name__ == "__main__":
    storage = ZODB.FileStorage.FileStorage(settings.DB_PATH_FILENAME)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    new_decision = Decision("Select Graph Database to Use")
    root.decision = new_decision
    transaction.commit()

    print("Saved to database. Now let's try loading it.")

    old_decision = root.decision
    print(new_decision.name)
    print(old_decision.name)

    print("Change the name.")
    old_decision.name = "Joe Legner"
    transaction.commit()
    print(new_decision.name)
    print(old_decision.name)

    storage.close()
