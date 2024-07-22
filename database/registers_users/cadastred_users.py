from peewee import *

db = SqliteDatabase('registred_users.db')


class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    
    class Meta:
        database = db
    
Users.create_table(['Users'])