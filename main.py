# Création de scratch d'un logiciel de tracking concernant une prépa au permis.

# -*- coding: utf-8 -*-
import json
from tkinter import *
from datetime import date


def carre():
    total = int(Valeur.get()) + int(Valeur2.get()) + int(Valeur3.get()) + int(Valeur4.get()) + int(
        Valeur5.get()) + int(Valeur6.get()) + int(Valeur7.get()) + int(Valeur8.get()) + int(Valeur9.get()) + int(
        Valeur10.get()) + int(Valeur11.get()) + int(Valeur12.get()) + int(Valeur13.get()) + int(Valeur14.get()) + \
            int(Valeur15.get())
    + int(Valeur16.get()) + int(Valeur17.get()) + int(Valeur18.get()) + int(Valeur19.get()) + int(Valeur20.get()) + \
    int(Valeur21.get()) + int(Valeur22.get()) + int(Valeur22.get()) + int(Valeur23.get()) + int(Valeur24.get()) + \
    int(Valeur25.get()) + int(Valeur26.get()) + int(Valeur27.get()) + int(Valeur28.get()) + int(Valeur29.get()) + \
    int(Valeur30.get()) + int(Valeur31.get()) + int(Valeur32.get()) + int(Valeur33.get()) + int(Valeur34.get()) + \
    int(Valeur35.get()) + int(Valeur36.get()) + int(Valeur37.get()) + int(Valeur38.get()) + int(Valeur39.get()) + \
    int(Valeur40.get()) + int(Valeur41.get()) + int(Valeur42.get()) + int(Valeur43.get()) + int(Valeur44.get()) + \
    int(Valeur45.get()) + int(Valeur46.get()) + int(Valeur47.get())
    return total


Mafenetre = Tk()

boite = IntVar()
Valeur = IntVar()
Valeur2 = IntVar()
Valeur3 = IntVar()
Valeur4 = IntVar()
Valeur5 = IntVar()
Valeur6 = IntVar()
Valeur7 = IntVar()
Valeur8 = IntVar()
Valeur9 = IntVar()
Valeur10 = IntVar()
Valeur11 = IntVar()
Valeur12 = IntVar()
Valeur13 = IntVar()
Valeur14 = IntVar()
Valeur15 = IntVar()
Valeur16 = IntVar()
Valeur17 = IntVar()
Valeur18 = IntVar()
Valeur19 = IntVar()
Valeur20 = IntVar()
Valeur21 = IntVar()
Valeur22 = IntVar()
Valeur23 = IntVar()
Valeur24 = IntVar()
Valeur25 = IntVar()
Valeur26 = IntVar()
Valeur27 = IntVar()
Valeur28 = IntVar()
Valeur29 = IntVar()
Valeur30 = IntVar()
Valeur31 = IntVar()
Valeur32 = IntVar()
Valeur33 = IntVar()
Valeur34 = IntVar()
Valeur35 = IntVar()
Valeur36 = IntVar()
Valeur37 = IntVar()
Valeur38 = IntVar()
Valeur39 = IntVar()
Valeur40 = IntVar()
Valeur41 = IntVar()
Valeur42 = IntVar()
Valeur43 = IntVar()
Valeur44 = IntVar()
Valeur45 = IntVar()
Valeur46 = IntVar()
Valeur47 = IntVar()
Valeur48 = IntVar()
Valeur49 = IntVar()
Valeur50 = IntVar()
Valeur51 = IntVar()
Valeur52 = IntVar()
Valeur53 = IntVar()
Valeur54 = IntVar()
Valeur55 = IntVar()
Valeur56 = IntVar()
Valeur57 = IntVar()
Valeur58 = IntVar()
Valeur59 = IntVar()
Valeur60 = IntVar()
Valeur.set(0.0)


def showtwo():
    frameTwo = Toplevel()
    frameTwo.grab_set()
    label = Label(frameTwo, text='Connaître et maîtriser son véhicule')
    label.pack()

    laVer = Label(frameTwo, text='Vérifications intérieures et extérieures')
    laVer.pack()

    boite = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur, command=carre)
    boite.pack()

    laVer = Label(frameTwo, text='Installation au poste de conduite :')
    laVer.pack()
    boite1 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur2, command=carre)
    boite1.pack()

    laVer = Label(frameTwo, text='Distance entre le siège et les pédales :')
    laVer.pack()
    boite2 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur3, command=carre)
    boite2.pack()
    laVer = Label(frameTwo, text='Hauteur et l\'inclinaison du siège :')
    laVer.pack()
    boite3 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur4, command=carre)
    boite3.pack()
    laVer = Label(frameTwo, text='Position du volant :')
    laVer.pack()
    boite4 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur5, command=carre)
    boite4.pack()
    laVer = Label(frameTwo, text='La manipulation des commandes et le fonctionnement du véhicule :')
    laVer.pack()
    boite5 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur6, command=carre)
    boite5.pack()
    laVer = Label(frameTwo, text='Dégivrage de la lunette arrière :')
    laVer.pack()
    boite6 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur7, command=carre)
    boite6.pack()
    laVer = Label(frameTwo, text='Les feux :')
    laVer.pack()
    boite7 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur8, command=carre)
    boite7.pack()
    laVer = Label(frameTwo, text='Les airbags :')
    laVer.pack()
    boite8 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur9, command=carre)
    boite8.pack()
    laVer = Label(frameTwo, text='Les témoins du tableau de bord :')
    laVer.pack()
    boite9 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur10, command=carre)
    boite9.pack()
    laVer = Label(frameTwo, text='Réglages et accessoires :')
    laVer.pack()
    boite11 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur11, command=carre)
    boite11.pack()
    laVer = Label(frameTwo, text='Chauffage et désembuage :')
    laVer.pack()
    boite12 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur12, command=carre)
    boite12.pack()
    laVer = Label(frameTwo, text='Freinage de précision :')
    laVer.pack()
    boite13 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur13, command=carre)
    boite13.pack()
    laVer = Label(frameTwo, text='Manœuvre en marche arrière :')
    laVer.pack()
    boite14 = Spinbox(frameTwo, from_=0, to=3, increment=1, width=5, textvariable=Valeur14, command=carre)
    boite14.pack()

    BoutonNext = Button(frameTwo, text='Suivant', command=showthree)
    BoutonNext.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(frameTwo, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)


def showthree():
    total = carre()

    Resultat.set(total)

    frameThree = Toplevel()
    frameThree.grab_set()
    label = Label(frameThree, text='Appréhender la route')
    label.pack()

    laVer = Label(frameThree, text='La prise d’information')
    laVer.pack()
    boite15 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur41, command=carre)
    boite15.pack()
    laVer = Label(frameThree, text='Prendre l\'information vers l\'avant et latéralement :')
    laVer.pack()
    boite16 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur15, command=carre)
    boite16.pack()
    laVer = Label(frameThree, text='Prendre l\'information vers l\'arrièreà l\'aide des rétroviseurs :')
    laVer.pack()
    boite17 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur16, command=carre)
    boite17.pack()
    laVer = Label(frameThree, text='Prendre l\'information en vision directe:')
    laVer.pack()
    boite18 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur17, command=carre)
    boite18.pack()
    laVer = Label(frameThree, text='L’allure du véhicule :')
    laVer.pack()
    boite19 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur18, command=carre)
    boite19.pack()
    laVer = Label(frameThree, text='Connaître les limitations de vitesse :')
    laVer.pack()
    boite20 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur19, command=carre)
    boite20.pack()
    laVer = Label(frameThree, text='Adapter son allure :')
    laVer.pack()
    boite21 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur20, command=carre)
    boite21.pack()

    laVer = Label(frameThree, text='Rouler au pas :')
    laVer.pack()
    boite22 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur21, command=carre)
    boite22.pack()
    laVer = Label(frameThree, text='Connaître les limitations sur route :')
    laVer.pack()
    boite23 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur22, command=carre)
    boite23.pack()
    laVer = Label(frameThree, text='Connaître les limitations pour jeunes conducteurs :')
    laVer.pack()
    boite24 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur23, command=carre)
    boite24.pack()
    laVer = Label(frameThree, text='Connaître les limitations en ville :')
    laVer.pack()
    boite25 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur24, command=carre)
    boite25.pack()
    laVer = Label(frameThree, text='Connaître les limitations sur périphérique :')
    laVer.pack()
    boite26 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur25, command=carre)
    boite26.pack()
    laVer = Label(frameThree, text='Connaître les limitations sur autoroute :')
    laVer.pack()
    boite27 = Spinbox(frameThree, from_=0, to=3, increment=1, width=5, textvariable=Valeur26, command=carre)
    boite27.pack()

    BoutonNext = Button(frameThree, text='Suivant', command=showfour)
    BoutonNext.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(frameThree, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)


def showfour():
    total = carre()

    frameFour = Toplevel()
    frameFour.grab_set()
    label = Label(frameFour, text='Partager la route avec les autres usagers')
    label.pack()

    laVer = Label(frameFour, text='La communication avec les autres usagers')
    laVer.pack()
    boite28 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur27, command=carre)
    boite28.pack()
    laVer = Label(frameFour, text='Utiliser les clignotants dès que cela est nécessaire :')
    laVer.pack()
    boite29 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur28, command=carre)
    boite29.pack()
    laVer = Label(frameFour, text='Utiliser les feux stop ou de détresse :')
    laVer.pack()
    boite30 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur40, command=carre)
    boite30.pack()
    laVer = Label(frameFour, text='Utiliser l\'avertisseur sonore (seulement si la situation l\'exige) :')
    laVer.pack()
    boite31 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur29, command=carre)
    boite31.pack()
    laVer = Label(frameFour, text='Le partage de la chaussée :')
    laVer.pack()
    boite32 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur30, command=carre)
    boite32.pack()
    laVer = Label(frameFour, text='Se positionner correctement sur la chaussée :')
    laVer.pack()
    boite33 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur31, command=carre)
    boite33.pack()
    laVer = Label(frameFour, text='Se positionner correctement sur autoroute :')
    laVer.pack()
    boite34 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur32, command=carre)
    boite34.pack()
    laVer = Label(frameFour, text='Veiller aux autres véhicules et distance de sécurité :')
    laVer.pack()
    boite35 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur33, command=carre)
    boite35.pack()
    laVer = Label(frameFour, text='Le maintien des espaces de sécurité :')
    laVer.pack()
    boite36 = Spinbox(frameFour, from_=0, to=3, increment=1, width=5, textvariable=Valeur34, command=carre)
    boite36.pack()

    BoutonNext = Button(frameFour, text='Suivant', command=showfive)
    BoutonNext.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(frameFour, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)


def showfive():
    total = carre()

    frameFive = Toplevel()
    frameFive.grab_set()
    label = Label(frameFive, text='Autonomie et conscience du risque')
    label.pack()
    laVer = Label(frameFive, text='L’analyse des situations :')
    laVer.pack()
    boite37 = Spinbox(frameFive, from_=0, to=3, increment=1, width=5, textvariable=Valeur35, command=carre)
    boite37.pack()
    laVer = Label(frameFive, text='L’adaptation aux situations :')
    laVer.pack()
    boite38 = Spinbox(frameFive, from_=0, to=3, increment=1, width=5, textvariable=Valeur36, command=carre)
    boite38.pack()
    laVer = Label(frameFive, text='La conduite autonome :')
    laVer.pack()
    boite39 = Spinbox(frameFive, from_=0, to=3, increment=1, width=5, textvariable=Valeur37, command=carre)
    boite39.pack()

    BoutonNext = Button(frameFive, text='Suivant', command=showsix)
    BoutonNext.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(frameFive, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)


def showsix():
    total = carre()

    frameSix = Toplevel()
    frameSix.grab_set()
    label = Label(frameSix, text='Point bonus')
    label.pack()
    laVer = Label(frameSix, text='Courtoisie au volant :')
    laVer.pack()
    boite40 = Spinbox(frameSix, from_=0, to=3, increment=1, width=5, textvariable=Valeur38, command=carre)
    boite40.pack()
    laVer = Label(frameSix, text='Conduite économique :')
    laVer.pack()
    boite41 = Spinbox(frameSix, from_=0, to=3, increment=1, width=5, textvariable=Valeur39, command=carre)
    boite41.pack()
    BoutonNext = Button(frameSix, text='Suivant', command=showfinal)
    BoutonNext.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(frameSix, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)


# Mon parser JSON

def write_my_values(datejour, score):

    inscrire = [{"date": f"{datejour}", "score": f"{score}".format(score)}]

    with open("scores.json", "w") as file:
        json.dump(inscrire, file)


def showfinal():
    total = carre()
    print(total)
    dateConv = date.today()
    write_my_values(dateConv, total)
    print(dateConv)
    frameFinal = Toplevel()
    frameFinal.grab_set()
    final = Label(frameFinal, text='Félicitations !')
    final.pack()
    points = Label(frameFinal, text=" Total des points " + str(int(total)))
    points.pack()


# Ma lecture de nom

# Give a Json file and return a List
def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values


Resultat = IntVar()

Label1 = Label(Mafenetre, text='Bonjour {} !'.format(read_values_from_json('user.json', 'name')), fg='blue')
Label1.pack()

BoutonLancer = Button(Mafenetre, text='Suivant', command=showtwo)
BoutonLancer.pack(side=LEFT, padx=5, pady=5)

BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
BoutonQuitter.pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()
