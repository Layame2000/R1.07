jour = int(input("On est quel jour ? "))
heure = int(input("Il est quelle heure ? juste l'heure pas la minute "))
minute = int(input("donne la minute ? "))
temps = (jour-1)*24*60+heure*60+minute

print(f"il s'est écoulé {temps} minutes depuis le début du mois")