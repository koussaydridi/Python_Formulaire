from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId  # Import ObjectId from bson module
from Classes import Etudiant
import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Etudiant'
mongo = PyMongo(app)

# Récupérer la valeur du port depuis la variable d'environnement ou utiliser 5000 par défaut
port = int(os.environ.get('PORT', 5000))

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

            # Insert data into MongoDB
            mongo.db.etudiant.insert_one({
                'name': etudiant0.name,
                'lastname': etudiant0.lastname,
                'age': etudiant0.age,
                'departement': etudiant0.departement,
                'moyenne': etudiant0.moyenne,
                'matiereX': etudiant0.matiereX,
                'matiereY': etudiant0.matiereY
            })

            # Redirect to the 'results' page
            #return redirect(url_for('results'))

        except ValueError:
            return render_template('index.html', error="Invalid input. Age, moyenne, matiereX, and matiereY must be numeric.")

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    etudiants_from_db = list(mongo.db.etudiant.find())
    return render_template('result.html', etudiants=etudiants_from_db)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'GET':
        etudiant_to_edit = mongo.db.etudiant.find_one({'_id': ObjectId(id)})
        return render_template('edit.html', etudiant=etudiant_to_edit)

    elif request.method == 'POST':
        try:
            # Update the record in MongoDB based on the submitted form data
            mongo.db.etudiant.update_one(
                {'_id': ObjectId(id)},
                {
                    '$set': {
                        'name': request.form['name'],
                        'lastname': request.form['lastname'],
                        'age': int(request.form['age']),
                        'departement': request.form['departement'],
                        'moyenne': float(request.form['moyenne']),
                        'matiereX': float(request.form['matiereX']),
                        'matiereY': float(request.form['matiereY'])
                    }
                }
            )
            return redirect(url_for('results'))

        except ValueError as e:
            return render_template('edit.html', etudiant=request.form, error=f"Error: {str(e)}")

@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    # Delete the record from MongoDB
    mongo.db.etudiant.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('results'))

if __name__ == '__main__':
    app.run(debug=True , port=port) 

    #cette fichier pour run toute le code et aussi la methode crud