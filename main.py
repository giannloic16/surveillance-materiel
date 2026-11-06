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

def affichage_informations():
    print(f"Utilisation du processeur : {utilisation} %")
    print(f"Nombre de cœurs logiques : {coeurs_logiques}")

    if frequence is not None:
        print(f"Fréquence du processeur : {frequence} MHz")
    else:
        print("Fréquence du processeur : Non disponible")

while True:
    utilisation = psutil.cpu_percent(interval=1)

    print(f"L'utilisation du processeur est de {utilisation} %")

    if utilisation <= 69:
        print("NORMAL")
    elif utilisation <= 89:
        print("ATTENTION")
    else:
        print("CRITIQUE")
