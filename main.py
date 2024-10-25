import random
import time

edgar

#https://docs.google.com/document/d/12Lgoe0pz3LDN1C1GnyhO4mznLoy_PkJRcGvO-OsKtC8/edit (TRACK)        download file w track as .txt
#https://docs.google.com/document/d/1op-mx9VOonx-x1e-jvTox2gHTJ540Gxo0te0QokSxX0/edit?pli=1 (MENU)


class Main:
  jeu = Jeu("/content/track.txt")
  jeu.affiche()

  menu = Menu("/Menu.txt")
  menu.affiche()

  Sys_pari.demarre()
  montant = int(input("Entrez le montant à parier : "))
    sys_pari.parier(chevaux[0], montant)


class Jeu:
  def __init__(self, nom_de_carte):
        with open(nom_de_carte) as carte:
          self.track = [[Case(char) for char in ligne if char != '\n'] for ligne in carte.readlines()]


  def affiche(self):
    for ligne in self.track:
      for case in ligne:
          print(case, end='')
      print()
    print('\n')

    def demarre(self):
      while True:
        cmd = input()
        if cmd == "start":



#LES CHEVEAUX ---------------------------------------------------------------------------------------------------------------------------

class Cheveaux:
  def __init__(self, name, numero, stat):
    self.name = name
    self.speed = 0
    self.numero = numero

  def courir_speed(self, Cheval):
        self.speed = random.randint(7, 16)

Cheval1 = Chevaux("Cheval 1", 1)
Cheval2 = Chevaux("Cheval 2", 2)
Cheval3 = Chevaux("Cheval 3", 3)
Cheval4 = Chevaux("Cheval 4", 4)
Cheval5 = Chevaux("Cheval 5", 5)
Cheval6 = Chevaux("Cheval 6", 6)
Cheval7 = Chevaux("Cheval 7", 7)
Cheval8 = Chevaux("Cheval 8", 8)



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





