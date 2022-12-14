import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    name = Column(Integer, primary_key=True)
    followers = Column(String(50), nullable=False)
    following = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return {
            "name": self.name,
            "followers": self.followers,
            "following": self.following
        }


class Post(Base):
    __tablename__ = 'post'

    title = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return {
            "title": title.self,
            "description": description.self,
        }


class Likes(Base):
    __tablename__ = 'likes'

    photold = Column(Integer, primary_key=True)
    user = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return {
            "photold": photold.self,
            "user": user.self,
        }


class Comments(Base):
    __tablename__ = 'comments'

    postdate = Column(Integer, primary_key=True)
    content = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return {
            "postdate": postdate.self,
            "content": content.self,
        }

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
