import random
import time


class Chevaux:
  def __init__(self, nom, min_vitesse, max_vitesse):
    self.nom = nom
    self.min_vitesse = min_vitesse
    self.max_vitesse = max_vitesse
    self.speed = 0
  
  def courir_speed(self):
    self.speed = randint(min_vitesse, max_vitesse)

class System_pari:
  def __init__(self):
    self.total = 500
  
  def parier(self, montant):
    if self.total > montant:
      raise IndexError("Vous n'avez pas assez d'argent pour parier cette somme")
    else:
      self.total -= montant
      return True
  
  def mis_a_jour_total(self, montant):
    self.total += montant

class Jockey_race:
  def __init__(self):
        self.horses = [
            Horse("Horse 1", 10, 15),
            Horse("Horse 2", 12, 18),
            Horse("Horse 3", 8, 14),
            Horse("Horse 4", 9, 16),
            Horse("Horse 5", 11, 17),
            Horse("Horse 6", 10, 20),
            Horse("Horse 7", 13, 19),
            Horse("Horse 8", 15, 22)
        ]
        self.system_pari = System_pari()
  
  def demmarer(self):
    print("Le course demarre...")
    for horse in self.horses:
      horse.run()



class Fait_aleatoire:
  def __init__(self,accident, blessure, boost):
    self.accident = "Accident"
    self.blessure = "Blessure"
    self.boost = "Boost"

  def evenement_innatendue(self, chevaux):
    #for random cheval
    if random.random() < 0.05:
      print(f"{cheval.name} a eu un accident et s'arrête.")
      cheval.speed = 0
      time.sleep(2)
      cheval.speed = random.randint(5, 20)
    if random.random() < 0.03:
      print(f"{cheval.name} c´est blesse.")
      cheval.speed = 5
    if random.random() < 0.01:
      print(f"{cheval.name} a dope")
      cheval.speed = 20

#MENU---------------------------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self, menu_fiche):
        self.menu_fiche = menu_fiche

    def affiche_debut(self):
        with open(self.menu_fiche) as menu:
            for line in menu:
                print(line, end="")
        print()





