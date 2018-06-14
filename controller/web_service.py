'''
 O web_service.py é o responsável por montar um web service rest na máquina a qual está sendo executado.
 Para que seja executado duas depedencia devem ser executadas:
 #1 O mysql-connector-python deve estar instalado. Instruções de instalação são encontradas em https://dev.mysql.com/
 #2 O framework bottle deve estar instalado. Instruções de instalação são encontradas em https://bottlepy.org/docs/dev/index.html
 
 Depois de instaladas as depedencias e executado a seguinte mensagem irá aparecer no prompt:

	shell:~/Desktop$ sudo python web_service.py 
	Bottle v0.12.13 server starting up (using WSGIRefServer())...
	Listening on http://ip:port/
	Hit Ctrl-C to quit.

'''

import mysql.connector
from bottle import route, run


'''
 Função criada para teste do servidor. Vá ao nevegador, e na barra de endereço coloque:
 ip:port/hello e uma mensagem de será exibida
'''
@route('/hello')
def hello():
    return "Hello World!"


'''
 Função criada para inserir um registro na tabela
'''
@route('/insert/<state>')
def insert(state):
    cnx = mysql.connector.connect(user='root', password='root', database='pi')
    add_state = ("INSERT INTO app2state (state) VALUES (%(state)s)")
    data_state = {'state': state}
    cursor = cnx.cursor()    
    cursor.execute(add_state, data_state)
    cnx.commit()
    cursor.close()
    cnx.close()
'''
 Função responsável por executar o web service. É preciso passar o ip do host e a porta na qual a aplicação vai executar
'''
run(host='192.168.75.3', port=8080, debug=True)
