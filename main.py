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


def affichage_informations_ram(informations_ram):
    print(f"Mémoire totale : {informations_ram.total}")
    print(f"Mémoire disponible : {informations_ram.available}")
    print(f"Pourcentage d'utilisation : {informations_ram.percent}%")
    print(f"Mémoire utilisée : {informations_ram.used}")
    print(f"Mémoire libre : {informations_ram.free}")
    print(f"Mémoire active : {informations_ram.active}")
    print(f"Mémoire inactive : {informations_ram.inactive}")
    print(f"Mémoire buffers : {informations_ram.buffers}")
    print(f"Mémoire cachée (cached) : {informations_ram.cached}")
    print(f"Mémoire partagée : {informations_ram.shared}")
    print(f"Mémoire slab : {informations_ram.slab}")


while True:

    utilisation = psutil.cpu_percent(interval=1)

    print(f"L'utilisation du processeur est de {utilisation} %")

    if utilisation <= 69:
        print("NORMAL")
    elif utilisation <= 89:
        print("ATTENTION")
    else:
        print("CRITIQUE")

    affichage_informations()


    informations_ram = psutil.virtual_memory()

    if informations_ram.percent <= 70:
        etat = "normal"
        print(etat)
    elif informations_ram.percent >= 70 and informations_ram.percent <= 85:
        etat = "attention"
        print(etat)
    elif informations_ram.percent > 85:
        etat = "critique"
        print(etat)

    affichage_informations_ram(informations_ram)

    time.sleep(5)
