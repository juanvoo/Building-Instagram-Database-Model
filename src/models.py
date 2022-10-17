import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

followers = Table (
    "followerS_",
    Base.metadata,
    Column("user_from_id", Integer,  ForeignKey('usuario.id')),
    Column("user_to_id", Integer,  ForeignKey('usuario.id'))
)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    seguidores = relationship("followerS_", secondary=followers)

# class Followers(Base):
#     __tablename__ = 'followers'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     user_from_id = Column(Integer,  ForeignKey('usuario.id'), nullable=False)
#     user_to_id = Column(Integer,  ForeignKey('usuario.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('usuario.id'))
    comments = relationship("Comentarios", backref="comentarios")
    media = relationship("Media", backref="media")

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    comentario = Column(String(250), nullable=False)
    author_id = Column(Integer,  ForeignKey('usuario.id'))
    id_post = Column(Integer,  ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    media_id = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    id_post = Column(Integer,  ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')