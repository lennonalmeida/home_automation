#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode

def read_state():
    #read state of machine

def read_db():
    #read state of db

def update_ap(id_gpio, state):
    #update appliance
    GPIO.output(id_gpio, state)

def update_db(cursor, data_db):
    #update db if diff_db == True
    update_state = "update %s set state %s where id = %s;"
    cursor.execute(update_state, data_db)

def add_app:
    #add a appliance
    #stand by

def diff_db():
    #return True if db != appliance
    status = False
    return status

#main code

data_db ={
    db_name = 'pi',
    table_name = 'app2state'
    id = '0',
}

try:
    db = mysql.connector.connect(user="root", password="mysql", host="192.168.0.155",database=db_name)
    cursor = db.cursor()
    while True:
        read_state()
        update_db()
except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
       print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
       print("Database does not exist")
     else:
       print(err)
else:
     db.close()
