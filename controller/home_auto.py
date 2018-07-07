#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

import mysql.connector
from datetime import date, datetime, timedelta
from mysql.connector import errorcode

# def read_db():
#     #READ db
#     comand_show = 'SELECT state FROM app2state WHERE state BETWEEN 1 AND 2;'
#     cursor.execute(comand_show)
#     out = cursor.fetchall()
#
#     for i in out:
#         print(i)

def update_ap(id_gpio, state):
     #update appliance
     GPIO.output(id_gpio, state)

# def diff_db(new):
#     #return True if db != appliance
#     #TODO compare db with 'new'
#     status = False
#     return status
#
#main code
if __name__ == '__main__':
    db_name = 'pi'
    table_name = 'app2state'
    #TODO id to all appliance

    #connect to db
    db = mysql.connector.connect(user="root", password="mysql", database=db_name)
    cursor = db.cursor()

    #read_db()

    #update db
    while True:
        if state == 'GPIO.HIGH':
            state = 'GPIO.OUT'
        else:
            state = 'GPIO.HIGH'
            update_ap(2, state)
        time.sleep(2)
    db.close()
