from json import JSONEncoder
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
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
    session.commit()
    print(decision.criteria)
