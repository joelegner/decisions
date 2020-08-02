from json import JSONEncoder
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


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
    __tablename__ = 'criteria_relationship'
    left_id = Column(Integer, ForeignKey('criteria.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('criteria.id'), primary_key=True)
    value = Column(Float, default=1.0)


class Decision(Base):

    __tablename__ = 'decisions'

    id = Column(Integer, Sequence('decision_id_seq'), primary_key=True)
    name = Column(String(50))
    criteria = relationship("Criterium")

    def __repr__(self):
        return "<Decision(id=%s, name='%s')>" % (self.id, self.name)

    def add_criterium(self, name):
        new_criterium = Criterium(name=name)
        new_criterium.decision = self
        return new_criterium

    def save(self, session):
        session.commit()

    def remake_relationships(self, session):
        # Add a new relationship when none exists
        criteria_ids = [c.id for c in self.criteria]
        for left_id in criteria_ids:
            for right_id in criteria_ids[left_id:]:
                if not left_id == right_id:
                    print("TODO: Add relationship (%d, %d)" %
                          (left_id, right_id))


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///:memory:', echo=True)
    decision = Decision(name="Software Project")
    print(type(Decision.__table__))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(decision)
    session.commit()
    print(decision)
    decision.add_criterium("Fun to Use")
    decision.add_criterium("Cheap")
    decision.add_criterium("Colorful")
    decision.add_criterium("Snappy Name")
    session.commit()
    decision.remake_relationships(session)
    session.commit()
    print(session.query(CriteriaComparison).all())
