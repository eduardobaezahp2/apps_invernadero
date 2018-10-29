from flask import Flask, request
import mysql.connector
from usuario import Usuario



conexion = mysql.connector.connect(user="root",password="",database="invernadero", port =3406)
cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/")
def hello():

    return "Hello world!"
#/login/?usuario=nombre&password=contraseña    
@app.route("/login/", methods=['GET'])
def login():
    usuario =request.args.get('usuario')
    password =request.args.get('password')
    
    userDB = Usuario(conexio, cursor)
    print(userDB.login(usuario, password))
    
    print(usuario, password)
    
   #print(request.args)
   #return "Para hacer login"
    return usuario + " " + password
    
app.run(debug=True)