import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class contact(Base):
    __tablename__ = 'contact'
    contact_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True ,nullable=False)
    email = Column(String(50), unique=True ,nullable=False)
    address = Column(String(50))
    phone = Column(String(50))
    active = Column(Boolean)

class agenda(Base):
    __tablename__ = 'agenda'
    agenda_id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    contact_id = Column(Integer, ForeignKey(contact.contact_id))
    contact_id = relationship(contact)

class add_contact(Base):
    __tablename__ = 'add_contact'
    add_contact_id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    type = Column(String(250))
    contact_id = Column(Integer, ForeignKey(contact.contact_id))
    contact_id = relationship(contact)

class edit_contact(Base):
    __tablename__ = 'edit_contact'
    edit_contact_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey(agenda.agenda_id))
    agenda_id = relationship(agenda)
    contact_id = Column(Integer, ForeignKey(contact.contact_id))
    contact_id = relationship(contact)

class delete_contact(Base):
    __tablename__ = 'delete_contact'
    delete_contact_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey(agenda.agenda_id))
    agenda_id = relationship(agenda)
    contact_id = Column(Integer, ForeignKey(contact.contact_id))
    contact_id = relationship(contact)

class delete_agenda(Base):
    __tablename__ = 'delete_agenda'
    delete_agenda_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey(agenda.agenda_id))
    agenda_id = relationship(agenda)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
