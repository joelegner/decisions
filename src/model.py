from json import JSONEncoder
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Criterium(Base):

    __tablename__ = 'criteria'

    id = Column(Integer, Sequence('criteria_id_seq'), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Criterium(id=%s, name='%s')>" % (self.id, self.name)


class Decision(Base):

    __tablename__ = 'properties'

    id = Column(Integer, Sequence('decision_id_seq'), primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Decision(id=%s, name='%s')>" % (self.id, self.name)


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
