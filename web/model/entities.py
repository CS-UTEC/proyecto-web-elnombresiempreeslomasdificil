from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from xdg import BaseDirectory
from os import path

import json
import markdown

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
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(100))
    description = Column(String(600))

    #           "ingredient":quantity
#    Ingredients = Column({})
    #       "step":time
#    Steps = Column({})

    def to_json_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description
        }


recipe_data_dir = path.join(BaseDirectory.xdg_data_home, "web")


class Recipe2(connector.Manager.Base):
    __tablename__ = 'recipe2'
    id = Column(Integer, Sequence('recipe2_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(100))

    md_file = Column(String(255))
    json_file = Column(String(255))

    def to_json_dict(self):

        tag_file = open(path.join(recipe_data_dir, self.json_file))
        markdown_file = open(path.join(recipe_data_dir, self.md_file))

        tags = json.loads(tag_file.read())
        markdown_str = markdown_file.read()

        tag_file.close()
        markdown_file.close()

        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'markdown': markdown.markdown(markdown_str),
            'tags': tags['tags']
        }
