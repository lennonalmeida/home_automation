#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode

def read_db():
    #read state of db
    a = ''
    #a[0] = id from db
    #a[1] = state from db
    return a

def update_ap(id_gpio, state):
    #update appliance
    GPIO.output(id_gpio, state)

def update_db(cursor, data_db):
    #update db if diff_db == True
    update_state = ("UPDATE %s SET STATE %s WHERE ID = %s;")
    cursor.execute(update_state, data_db)
    cursor.commit()

def add_app:
    #add a appliance
    #stand by

def diff_db(new):
    #return True if db != appliance
    #TODO compare db with 'new'
    status = False
    return status

#main code

data_db ={
    db_name = 'pi',
    table_name = 'app2state'
    id = '0',
}

db = mysql.connector.connect(user="root", password="mysql", database=db_name)
cursor = db.cursor()

while True:
    new = read_db()
    if diff_db(new):
        update_ap(new)
