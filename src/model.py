from json import JSONEncoder
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import logging
from sqlalchemy import create_engine
from sqlalchemy import orm
from sqlalchemy.orm import sessionmaker
import os


Base = declarative_base()


class Criterium(Base):

    __tablename__ = 'criteria'

    id = Column(Integer, Sequence('criteria_id_seq'), primary_key=True)
    name = Column(String(50))
    decision_id = Column(Integer, ForeignKey('decisions.id'))
    decision = relationship("Decision", back_populates="criteria")

    def __repr__(self):
        return "<Criterium(id=%s, name='%s')>" % (self.id, self.name)


class CriteriaComparison(Base):
    __tablename__ = 'criteria_comparison'
    left_id = Column(Integer, ForeignKey('criteria.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('criteria.id'), primary_key=True)
    value = Column(Float, default=1.0)
    decision_id = Column(Integer, ForeignKey('decisions.id'))
    decision = relationship("Decision", back_populates="criteria_comparisons")
    left_greater = Column(Boolean, default=True)

    def __repr__(self):
        return "<CriteriaComparison(left_id=%s, right_id=%s, value=%.3f)>" % (self.left_id, self.right_id, self.value)


class Decision(Base):
    __tablename__ = 'decisions'
    id = Column(Integer, Sequence('decision_id_seq'), primary_key=True)
    name = Column(String(50))
    criteria = relationship("Criterium")
    criteria_comparisons = relationship("CriteriaComparison")

    @orm.reconstructor
    def init_on_load(self):
        self.session = None

    def __repr__(self):
        return "<Decision(id=%s, name='%s')>" % (self.id, self.name)

    def add_criterium(self, name):
        new_criterium = Criterium(name=name)
        new_criterium.decision = self
        return new_criterium

    def save(self):
        self.session.commit()

    def get_or_add_relationship(self, left_id, right_id):
        instance = self.session.query(CriteriaComparison).filter_by(
            left_id=left_id, right_id=right_id).first()
        if instance:
            return instance
        else:
            logging.info("Add relationship (%d, %d)" %
                         (left_id, right_id))
            new_comparison = CriteriaComparison(
                left_id=left_id, right_id=right_id)
            new_comparison.decision = self
            return new_comparison, True

    def remake_relationships(self):
        # Add a new relationship when none exists
        criteria_ids = [c.id for c in self.criteria]

        comparisons = self.session.query(CriteriaComparison).all()

        if len(comparisons):
            print(comparisons)

        for left_id in criteria_ids:
            for right_id in criteria_ids[left_id:]:
                if not left_id == right_id:
                    self.get_or_add_relationship(left_id, right_id)


def open_decision_file(filename):
    "Opens an existing decision file and returns the Decision object."
    decision = None
    if os.path.isfile(filename):
        logging.info("File %s exists. Attempting to connect to it now.")
        engine = create_engine('sqlite:///%s' % filename, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        decision_query = session.query(Decision)
        if len(decision_query.all()) == 1:
            decision = decision_query.all()[0]
            decision.session = session
    else:
        logging.warn("Attempted to load file %s but it does not exist.")
    return decision


if __name__ == "__main__":
    if os.path.exists("testfile.dec"):
        os.remove("testfile.dec")
    engine = create_engine('sqlite:///testfile.dec', echo=True)
    Base.metadata.create_all(engine)
    decision = Decision(name="Software Project")
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(decision)
    decision.session = session
    decision.session.commit()
    decision.add_criterium("Fun to Use")
    decision.add_criterium("Cheap")
    decision.add_criterium("Colorful")
    decision.add_criterium("Snappy Name")
    decision.session.commit()
    decision.remake_relationships()
    decision.session.commit()
    decision.remake_relationships()
    decision.session.commit()
