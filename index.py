from flask import Flask, render_template, jsonify, request
from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en el formulario')
    return render_template('index.html', form = comment_form)

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/user/<name>', methods = ['GET', 'POST'])
def user(name='Juan'): #Va a recoger el valor del string entre los diamantes, en el decorador
    age = 32
    my_list = ['Estrella','Leffe','Grimbergen','Paulaner']
    return render_template('user.html', nombre=name, edad=age, list=my_list)#Va a devolver el template indicado, junto con el valor del segundo parámetro

@app.route('/json', methods = ['GET', 'POST'])
def json():
    persons = [{
        "name" : "Juan",
        "surname": "JC"
    },
    {
        "name" : "Another",
        "surname": "Person"
    }]
    return jsonify(persons)

if __name__ == '__main__':
    app.run(debug=True, port=8000) #Parámetros: Modo debug con autoreinicio, conectar mediante el puerto 8000
