# Hacer pip install pymsql
from peewee import AutoField, CharField, DateField, ForeignKeyField, Model, MySQLDatabase, DateTimeField
import datetime

#db = peewee.MySQLDatabase("peewee_test", host="localhost",port=3306, user="root", password="mpmp")
db = MySQLDatabase('peewee_test', user='root', password='mpmp',host='127.0.0.1', port=3306)

class User(Model):
    username = CharField(unique=True)
    email = CharField(index=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db
        table_name = "usuarios"  #http://docs.peewee-orm.com/en/latest/peewee/models.html#fields

if __name__ == "__main__":
    if not (User.table_exists()): #http://docs.peewee-orm.com/en/latest/peewee/api.html#database
        print("Crea Tabla")
        User.create_table()
    else:
        print("Tabla existente")

    xusername="Marcelo3"
    xemail=xusername + "@gmail.com"
    if not (User.select().where(User.username==xusername).exists()): #pregunta si el username con valor xusername existe
       new_user=User.create(username=xusername,email=xemail)  # insert
       new_user.save()
    else:
        print("Usuario ya registrado en la tabla.")
        