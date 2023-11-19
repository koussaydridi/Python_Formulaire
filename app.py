from flask import Flask, render_template, request
from Classes import Etudiant

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            name = request.form['name']
            lastname = request.form['lastname']
            age = int(request.form['age'])
            departement = request.form['departement']
            moyenne = float(request.form['moyenne'])
            matiereX = float(request.form['matiereX'])
            matiereY = float(request.form['matiereY'])

            etudiant0 = Etudiant(name, lastname, age, departement, moyenne, matiereX, matiereY)
            return render_template('index.html', etudiant=etudiant0)

        except ValueError:
            return render_template('index.html', error="Invalid input. Age, moyenne, matiereX, and matiereY must be numeric.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
