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
  


    def demarre(self):
      while True:
        cmd = input()
        if cmd == "start":



#LES CHEVEAUX ---------------------------------------------------------------------------------------------------------------------------



#SYSTEM PARI ----------------------------------------------------------------------------------------------------------------------------

class Sys_pari:
  def __init__(self, argent, multiplier)
    self.argent = 1000
    self.multiplier = 

  def parier(self, argent, montant):
    if self.argent < montant:
      print("Vous n'avez pas assez d'argent pour parier.")
    else:
      self.argent -= montant
        print(f"Vous pariez {montant} sur {cheval.name}.")



#FAIT ALEATOIRE -------------------------------------------------------------------------------------------------------------------------

class Fait_aleatoire:
  def __init__(self,accident, blessure, boost):
    self.accident = "Accident"
    self.blessure = "Blessure"
    self.boost = "Boost"

  def event_innatendue(self, chevaux):
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





