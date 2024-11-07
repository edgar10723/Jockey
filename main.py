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
        else:
            self.total -= montant
            return True
  
    def mettre_a_jour_total(self, montant):
        self.total += montant

class CourseDeJockey:
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
                if cheval.distance >= 100: #SI 2 CHOISI PLUS HAUT
                    return cheval

def main():
    jeu = CourseDeJockey()

    while True:
        action = input("Entrez 'parier' pour placer un pari, 'course' pour commencer la course, 'information' savoir plus sur les chevaux, ou 'exit' pour quitter: ").lower()
        if action == 'parier':
            montant = int(input("Entrer la somme à parier: "))
            if jeu.systeme_de_paris.parier(montant):
                numero_cheval = int(input("Entrez le numéro du cheval sur lequel parier (1-8): ")) - 1
                jeu.pari_en_cours = (jeu.chevaux[numero_cheval], montant)
                print(f"Vous pariez {montant} sur {jeu.chevaux[numero_cheval].nom}.")
        elif action == 'course':
            gagnant = jeu.demarrer()
            print(f"Le gagnant est {gagnant.nom}!")

            if gagnant == jeu.pari_en_cours[0]:
                paiement = 2 * jeu.pari_en_cours[1]
                jeu.systeme_de_paris.mettre_a_jour_total(paiement)
                print(f"Vous avez gagné {paiement}! Nouveau solde: {jeu.systeme_de_paris.total}")
            else:
                print("Vous avez perdu votre pari.")
        elif action == "info":     # Horse[] [numero] , V:[vitesse]
            self.information()
        
        elif action == 'exit':
            print("Sortie du jeu.")
            break
        else:
            print("Action invalide. Veuillez choisir à nouveau.")
            
    def information(self):
      print("Informations sur les chevaux:")
      print(f"{cheval.nom}, V: [{cheval.min_vitesse} - {cheval.max_vitesse}] km/h")

class Menu:
    def __init__(self, menu_fiche):
        self.menu_fiche = menu_fiche

    def affiche_debut(self):
        with open(self.menu_fiche) as menu:
            for line in menu:
                print(line, end="")
        print()



menu = Menu("Menu.txt")
menu.affiche_debut()

if __name__ == "__main__":
    main()
