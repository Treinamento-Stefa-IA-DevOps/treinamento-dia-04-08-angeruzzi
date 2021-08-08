import pickle
from fastapi import FastAPI
import pandas as pd

app = FastAPI()
@app.post('/model')
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
	dados = pd.DataFrame([[Sex,Age, Lifeboat,Pclass]], columns = ['Sex','Age','Lifeboat','Pclass'])
	with open('codigo/model/Titanic.pkl', 'rb') as fid: 
		titanic = pickle.load(fid)

	pred = titanic.predict(dados)
	
	if pred[0] == 1:
		survived = True
		message  = 'Sobrevivente'
	else:
		survived = False
		message  = 'Nao sobrevivente'  

	ret = { 'survived': survived, 'status': 200, 'message': message}

	return ret

@app.get('/model')
def get():
    return {'hello':'test'}
