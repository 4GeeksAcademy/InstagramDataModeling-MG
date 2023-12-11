import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contact'
    contact_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True ,nullable=False)
    email = Column(String(50), unique=True ,nullable=False)
    address = Column(String(50))
    phone = Column(String(50))
    active = Column(Boolean)

class Agenda(Base):
    __tablename__ = 'agenda'
    agenda_id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    contact_id = Column(Integer, ForeignKey('contact.contact_id'))
    contact = relationship('Contact')

class AddContact(Base):
    __tablename__ = 'add_contact'
    add_contact_id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    type = Column(String(250))
    contact_id = Column(Integer, ForeignKey('contact.contact_id'))
    contact = relationship('Contact')

class EditContact(Base):
    __tablename__ = 'edit_contact'
    edit_contact_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey('agenda.agenda_id'))
    agenda = relationship('Agenda')
    contact_id = Column(Integer, ForeignKey('contact.contact_id'))
    contact = relationship('Contact')

class DeleteContact(Base):
    __tablename__ = 'delete_contact'
    delete_contact_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey('agenda.agenda_id'))
    agenda = relationship('Agenda')
    contact_id = Column(Integer, ForeignKey('contact.contact_id'))
    contact = relationship('Contact')

class DeleteAgenda(Base):
    __tablename__ = 'delete_agenda'
    delete_agenda_id = Column(Integer, primary_key=True)
    agenda_id = Column(Integer, ForeignKey('agenda.agenda_id'))
    agenda = relationship('Agenda')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
