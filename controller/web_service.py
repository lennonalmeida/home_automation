import mysql.connector
from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!"

@route('/insert/<state>')
def insert(state):
    cnx = mysql.connector.connect(user='root', password='mysql', database='pi')
    add_state = ("INSERT INTO app2state (state) VALUES (%(state)s)")
    data_state = {'state': state}
    cursor = cnx.cursor()
    cursor.execute(add_state, data_state)
    cnx.commit()
    cursor.close()
    cnx.close()

run(host='192.168.0.8', port=8080, debug=True)
