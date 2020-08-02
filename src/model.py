from json import JSONEncoder
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import logging


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

    def __repr__(self):
        return "<Decision(id=%s, name='%s')>" % (self.id, self.name)

    def add_criterium(self, name):
        new_criterium = Criterium(name=name)
        new_criterium.decision = self
        return new_criterium

    def save(self, session):
        session.commit()

    def get_or_add_relationship(self, session, left_id, right_id):
        instance = session.query(CriteriaComparison).filter_by(
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

    def remake_relationships(self, session):
        # Add a new relationship when none exists
        criteria_ids = [c.id for c in self.criteria]

        comparisons = session.query(CriteriaComparison).all()

        if len(comparisons):
            print(comparisons)

        for left_id in criteria_ids:
            for right_id in criteria_ids[left_id:]:
                if not left_id == right_id:
                    self.get_or_add_relationship(session, left_id, right_id)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///testfile.db', echo=True)
    decision = Decision(name="Software Project")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(decision)
    session.commit()
    decision.add_criterium("Fun to Use")
    decision.add_criterium("Cheap")
    decision.add_criterium("Colorful")
    decision.add_criterium("Snappy Name")
    session.commit()
    decision.remake_relationships(session)
    session.commit()
    decision.remake_relationships(session)
    session.commit()
