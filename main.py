import psutil
import time
import datetime
import platform


utilisation = psutil.cpu_percent(interval=1)
coeurs_logiques = psutil.cpu_count()

frequence_cpu = psutil.cpu_freq()

if frequence_cpu is not None:
    frequence = frequence_cpu.current
else:
    frequence = None

while True:
    print(f"L'utilisation du processeur est de {utilisation} %")
    utilisation = psutil.cpu_percent(interval=1)

    if utilisation >= 0 and utilisation <= 69:
        print("Normal")
    elif utilisation > 69 and utilisation <= 89:
        print("Attention")
    elif utilisation > 89:
        print("Critique")


def affichage_informations():
    print(f"Utilisation du processeur : {utilisation}")
    print(f"Nombre de coeurs logiques : {coeurs_logiques}")
    print(f"Frequence du processeur : {frequence}")


def sauvegarde():
    moment_actuel = datetime.datetime.now()
    date_formatee = moment_actuel.strftime("%d/%m/%Y")
    print(date_formatee)

    informations = [utilisation, coeurs_logiques, frequence, date_formatee]

    with open("historique_cpu.txt", "a") as file1:
        for info in informations:
            file1.write(f"{str(info)}\n")
