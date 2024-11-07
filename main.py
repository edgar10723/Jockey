import random
import time

class Cheval:
    def __init__(self, nom, min_vitesse, max_vitesse):
        self.nom = nom
        self.min_vitesse = min_vitesse
        self.max_vitesse = max_vitesse
        self.distance = 0
        self.vitesse = 0
  
    def courir(self):
        self.vitesse = random.randint(self.min_vitesse, self.max_vitesse)
        self.distance += self.vitesse
        return self.vitesse

class SystemeDeParis:
    def __init__(self):
        self.total = 500
  
    def parier(self, montant):
        if self.total < montant:
            print("Vous n'avez pas assez d'argent pour parier cette somme")
            return False
        else:
            self.total -= montant
            return True
  
    def mettre_a_jour_total(self, montant):
        self.total += montant

class CourseDeJockey:
    def __init__(self):
        self.chevaux = self.creer_chevaux()
        self.systeme_de_paris = SystemeDeParis()
  
    def creer_chevaux(self):
        return [
            Cheval(f"Cheval {i+1}", random.randint(8, 12), random.randint(15, 22))
            for i in range(8)
        ]

        def demarrer(self):
        print("La course démarre...")
        while True:
            for cheval in self.chevaux:
                vitesse = cheval.courir()
                print(f"{cheval.nom} court {vitesse} mètres (Total: {cheval.distance})")
                cheval_fini = cheval in self.chevaux if cheval.distance >= 100
                if len(cheval_fini) >=2:
                  premier = 0
                  if premier < cheval_fini:
                    cheval_fini = premier
                    return premier
                else:
                  if cheval.distance >= 100:
                    return cheval
                      
    '''def demarrer(self):
        print("La course démarre...")
        while True:
            for cheval in self.chevaux:
                vitesse = cheval.courir()
                print(f"{cheval.nom} court {vitesse} mètres (Total: {cheval.distance})")
                if cheval.distance >= 100: #SI 2 CHOISI PLUS HAUT
                    return cheval'''

class Jeu:
    def __init__(self):
        self.course = CourseDeJockey()

    def information(self):
        print("Informations sur les chevaux:")
        for cheval in self.course.chevaux:
            print(f"{cheval.nom}, V: [{cheval.min_vitesse} - {cheval.max_vitesse}] km/h")

    def demarrer(self):
        while True:
            action = input("Entrez 'parier' pour placer un pari, 'course' pour commencer la course, 'info' pour savoir plus sur les chevaux, ou 'exit' pour quitter: ").lower()
            if action == 'parier':
                self.placer_pari()
            elif action == 'course':
                self.lancer_course()
            elif action == 'info':
                self.information()
            elif action == 'exit':
                print("Sortie du jeu.")
                break
            else:
                print("Action invalide. Veuillez choisir à nouveau.")

    def placer_pari(self):
        montant = int(input("Entrer la somme à parier: "))
        if self.course.systeme_de_paris.parier(montant):
            numero_cheval = int(input("Entrez le numéro du cheval sur lequel parier (1-8): ")) - 1
            self.course.pari_en_cours = (self.course.chevaux[numero_cheval], montant)
            print(f"Vous pariez {montant} sur {self.course.chevaux[numero_cheval].nom}.")

    def lancer_course(self):
        gagnant = self.course.demarrer()
        print(f"Le gagnant est {gagnant.nom}!")

        if gagnant == self.course.pari_en_cours[0]:
            paiement = 2 * self.course.pari_en_cours[1]
            self.course.systeme_de_paris.mettre_a_jour_total(paiement)
            print(f"Vous avez gagné {paiement}! Nouveau solde: {self.course.systeme_de_paris.total}")
        else:
            print("Vous avez perdu votre pari.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.demarrer()
