import enum
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///core_data.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Program(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    program_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    # section = Column(String)               # could also represent the sections as an ordered, 
    #                                         # comma separated list of section ids, but order_index is required anyway
    #                                         # ALSO could have created a ProgramSection mapping table

class ProgramSectionMapping(Base):
    __tablename__ = 'program_section_mappings'
    mapping_id = Column(String, primary_key=True)
    program_id = Column(String, nullable=False)
    section_id = Column(String, nullable=False)
    order_index = Column(Integer, nullable=False)       
    # might make sense to create a unique index key on (program_id, section_id, order_index)
    # could make foreign keys to Program table and Section table


class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    section_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    overview_image = Column(String)


class SectionActivityMapping(Base):
    __tablename__ = 'session_activity_mappings'
    mapping_id = Column(Integer, primary_key=True)
    section_id = Column(String, nullable=False)
    activity_id = Column(String, nullable=False)


class ActivityEnum(enum.Enum):
    HTML = "HTML"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    activity_id = Column(String, nullable=False)
    activity_type = Column(Enum(ActivityEnum), nullable=False)  # could add a CheckConstraint here
    description = Column(String)                                # this is either the question or the html content


class Answer(Base):                         # no ActivityAnswer mapping because can use Answer table
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer = Column(String, nullable=False)
    activity_id = Column(String, nullable=False)
    