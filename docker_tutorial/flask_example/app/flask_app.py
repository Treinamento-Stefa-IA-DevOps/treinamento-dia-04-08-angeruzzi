#from flask import Flask
#
#app = Flask(__name__)
#
#
#@app.route('/')
#def hello_world():
#    return 'Hello, World!'

from flask import Flask

# vamos pegar nossas credenciais de conexão como variaveis de ambiente!!
import os
# lib que vai nos conectar ao postgres!
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    #with psycopg2.connect(f"dbname={os.getenv('DB_NAME')} user={'DB_USER'} password={os.getenv('DB_PASS')}") as conn:
    with psycopg2.connect("dbname=teste user=userino password=password123") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test;")
# retorna o resultado como tuplas, onde cada item dentro da tupla [e o valor de uma coluna]
        rows = cur.fetchall()
        message = ''
        for row in rows:
        	# seleciona primeiro elemento da tupla retornada
            message = message + row[1]
    return message + " Direto de meu belo database!!"



    #conn = psycopg2.connect("dbname=test user=postgres password=secret")