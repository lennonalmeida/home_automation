import mysql.connector
from bottle import route, run

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


@route('/hello')
def hello():
    return "Hello World!"
@route('/insert/<state>/<id_pi>')
def insert(state, id_pi):
    print(state, id_pi)
    cnx = mysql.connector.connect(user='pidb', password='mysql', database='pi')
    add_state = ("UPDATE app2state SET  state = '"+state+"' WHERE id = "+id_pi+";")
    data_db = (state, id_pi)
    #data_state = {'state': state}
    cursor = cnx.cursor()
    cursor.execute(add_state)
    cnx.commit()
    cursor.close()
    cnx.close()
    id_pi = int(id_pi)
    update_ap((id_pi+1), state)
def update_ap(id_gpio, state):
    if state == 'OFF':
        state = 1
    else:
        state = 0
    GPIO.output(id_gpio, state)
run(host='192.168.0.11', port=8080, debug=True)

