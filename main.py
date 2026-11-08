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


def affichage_informations_ram(informations_ram):
    print(f" memoire totale: {informations_ram.total}")
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


def affichage_disque(disk_memory):
    print(f" La capacite totale du disque est de : {disk_memory.total}")
    print(f" La capacite occupée du disque est de : {disk_memory.used}")
    print(f" La capacite libre du disque est de: {disk_memory.free}")
    print(f" Pourcentage utilisé du disque est de: {disk_memory.percent}")


def sauvegarde_disque(disk_memory, etat):
    moment_actuel = datetime.datetime.now()
    date_formatee = moment_actuel.strftime("%d/%m/%Y %H:%M:%S")

    informations = [disk_memory.total, disk_memory.used, disk_memory.free,
    disk_memory.percent, date_formatee, etat]

    with open("historique_disque.txt", "a") as file1:
        for info in informations:
            file1.write(str(info) + " ")
        file1.write("\n")


while True:

    print(f"L'utilisation du processeur est de {utilisation} %")
    utilisation = psutil.cpu_percent(interval=1)

    if utilisation >= 0 and utilisation <= 69:
        print("Normal")
    elif utilisation > 69 and utilisation <= 89:
        print("Attention")
    elif utilisation > 89:
        print("Critique")

    affichage_informations()
    sauvegarde()


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


    disk_memory = psutil.disk_usage("/")

    if disk_memory.percent <= 70:
        etat = "normal"
        print(etat)
    elif disk_memory.percent > 70 and disk_memory.percent <= 85:
        etat = "attention"
        print(etat)
    elif disk_memory.percent > 85:
        etat = "critique"
        print(etat)

    affichage_disque(disk_memory)
    sauvegarde_disque(disk_memory, etat)

    time.sleep(5)
