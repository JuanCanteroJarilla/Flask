from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<name>')
def user(name='Juan'): #Va a recoger el valor del string entre los diamantes, en el decorador
    age = 32
    my_list = ['Estrella','Leffe','Grimbergen','Paulaner']
    return render_template('user.html', nombre=name, edad=age, list=my_list)#Va a devolver el template indicado, junto con el valor del segundo parámetro

@app.route('/json')
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
