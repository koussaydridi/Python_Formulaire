class Etudiant:
    def __init__(self, name, lastname, age, departement, moyenne, matiereX, matiereY):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.departement = departement
        self.matiereX = matiereX
        self.matiereY = matiereY
        self.moyenne = moyenne

    def __str__(self):
        return f"{self.name} {self.lastname} ({self.age}) {self.departement} {self.is_excellent()} {self.moyenne} {self.calcule_moyenne()}"

    def is_excellent(self):
        if self.moyenne >= 16:
            return "very good"
        else:
            return "good"
    
    def calcule_moyenne(self):
        self.moyenne = (self.matiereX + self.matiereY) / 2
        return self.moyenne