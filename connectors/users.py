# encoding: utf-8
from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))

from configurations import bot_config
from . import mongo_connection as mongo

def register_user(user_id, username, chat_id):
    client = mongo.connect()

    db = client[bot_config.DB_NAME]

    if db.registered_users.count_documents(
        {'user_id': user_id}) == 0:
        db.registered_users.insert_one({
            'user_id': user_id,
            'username': username,
            'chat_id': chat_id
        })

    return 1

def get_all_users():
    client = mongo.connect()

    db = client[bot_config.DB_NAME]

    return db.registered_users.find({})
