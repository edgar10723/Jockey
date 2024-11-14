import random

class Cheval:
    def __init__(self, nom, min_vitesse, max_vitesse):
        self.nom = nom
        self.min_vitesse = min_vitesse
        self.max_vitesse = max_vitesse
        self.distance = 0
        self.vitesse = 0
        self.total_vitesse = 0
        self.courses = 0

    def courir(self):
        self.vitesse = random.randint(self.min_vitesse, self.max_vitesse)
        self.distance += self.vitesse
        self.total_vitesse += self.vitesse
        self.courses += 1

    def reset(self):
        self.distance = 0
        self.courses = 0

class SystemeDeParis:
    def __init__(self):
        self.total = 500

    def parier(self, montant):
        if self.total < montant:
            print("Vous n'avez pas assez d'argent pour parier cette somme.")
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
            gagnants = []
            for cheval in self.chevaux:
                cheval.courir()
            self.afficher_course()
            for cheval in self.chevaux:
                if cheval.distance >= 100:
                    gagnants.append(cheval)
            if gagnants:
                return max(gagnants, key=lambda x: x.total_vitesse / x.courses if x.courses > 0 else 0)

    def afficher_course(self):
        track_length = 33
        for i, cheval in enumerate(self.chevaux):
            position = int(cheval.distance // 3)
            position = min(position, track_length - 1)
            track = '-' * position + f"({i + 1})>" + '-' * (track_length - position - 4)
            print(track)
        print()

    def reset_chevaux(self):
        for cheval in self.chevaux:
            cheval.reset()

class Jeu:
    def __init__(self):
        self.course = CourseDeJockey()
        self.course.pari_en_cours = None

    def information(self):
        print("Informations sur les chevaux:")
        for cheval in self.course.chevaux:
            print(f"{cheval.nom}, Spd: [{cheval.min_vitesse} - {cheval.max_vitesse}] m/s")

    def demarrer(self):
        while True:
            print(f"Votre solde: {self.course.systeme_de_paris.total} €")
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
        while True:
            try:
                montant = int(input("Entrer la somme à parier: "))
                if montant <= 0:
                    print("Le montant doit être positif. Veuillez réessayer.")
                    continue
                if self.course.systeme_de_paris.parier(montant):
                    while True:
                        numero_cheval = int(input("Entrez le numéro du cheval sur lequel parier (1-8): ")) - 1
                        if numero_cheval < 0 or numero_cheval >= 8:
                            print("Veuillez choisir entre les chevaux 1 à 8.")
                            continue
                        self.course.pari_en_cours = (self.course.chevaux[numero_cheval], montant)
                        print(f"Vous pariez {montant} sur le Cheval {numero_cheval + 1}.")
                        return
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def lancer_course(self):
        if self.course.pari_en_cours is None:
            print("Vous devez d'abord placer un pari avant de commencer la course.")
            return

        gagnant = self.course.demarrer()
        print(f"Le gagnant est le Cheval {self.course.chevaux.index(gagnant) + 1}!")

        if gagnant == self.course.pari_en_cours[0]:
            paiement = 2 * self.course.pari_en_cours[1]
            self.course.systeme_de_paris.mettre_a_jour_total(paiement)
            print(f"Vous avez gagné {paiement}! Nouveau solde: {self.course.systeme_de_paris.total} €")
        else:
            print("Vous avez perdu votre pari.")
            if self.course.systeme_de_paris.total <= 0:
                print("Vous n'avez plus d'argent. Bye bye!")
                return

        self.course.reset_chevaux()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.demarrer()
