import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'Contact'
    ContactID = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=True ,nullable=False)
    Email = Column(String(50), unique=True ,nullable=False)
    Address = Column(String(50))
    Phone = Column(String(50))
    Active = Column(Boolean)

class Agenda(Base):
    __tablename__ = 'Agenda'
    AgendaID = Column(Integer, primary_key=True)
    Active = Column(Boolean)
    ContactID = Column(Integer, ForeignKey(Contact.ContactID))
    C = relationship(Contact)

class AddContact(Base):
    __tablename__ = 'AddContact'
    AddContactID = Column(Integer, primary_key=True)
    Model = Column(String(50), nullable=False)
    Type = Column(String(250))
    ContactID = Column(Integer, ForeignKey(Contact.ContactID))
    C = relationship(Contact)

class EditContact(Base):
    __tablename__ = 'EditContact'
    EditContactID = Column(Integer, primary_key=True)
    AgendaID = Column(Integer, ForeignKey(Agenda.AgendaID))
    A = relationship(Agenda)
    ContactID = Column(Integer, ForeignKey(Contact.ContactID))
    C = relationship(Contact)

class DeleteContact(Base):
    __tablename__ = 'DeleteContact'
    DeleteContactID = Column(Integer, primary_key=True)
    AgendaID = Column(Integer, ForeignKey(Agenda.AgendaID))
    A = relationship(Agenda)
    ContactID = Column(Integer, ForeignKey(Contact.ContactID))
    C = relationship(Contact)

class DeleteAgenda(Base):
    __tablename__ = 'DeleteAgenda'
    DeleteAgendaID = Column(Integer, primary_key=True)
    AgendaID = Column(Integer, ForeignKey(Agenda.AgendaID))
    A = relationship(Agenda)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
