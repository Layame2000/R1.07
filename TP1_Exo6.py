minutestotal = int(input("Entrez les minutes écoulées depuis le début du mois ? "))
jours = minutestotal//1440
heure = minutestotal%1440//60
minutes = minutestotal-jours*1440-heure*60

print(f"Nous sommes le {jours} et il est {heure} heure {minutes}")