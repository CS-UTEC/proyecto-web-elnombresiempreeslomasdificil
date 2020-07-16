from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

if __package__ == 'model':
    from database import connector
else:
    from ..database import connector


class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(12))
    password = Column(String(12))


"""
class Message(connector.Manager.Base):
    __tablename__ = 'messages'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)
    content = Column(String(500))
    sent_on = Column(default=datetime.datetime.now())
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])
"""


class Recipe(connector.Manager.Base):
    __tablename__ = 'recipe'
    id = Column(Integer, Sequence('recipe_id_seq'), primary_key=True)
    Description = Column(String(600))
    #           "ingredient":quantity
#    Ingredients = Column({})
    #       "step":time
#    Steps = Column({})


class Recipe2(connector.Manager.Base):
    __tablename__ = 'recipe2'
    id = Column(Integer, Sequence('recipe2_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    md_file = Column(String(255))
    json_file = Column(String(255))
