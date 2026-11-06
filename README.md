Surveillance materielle avec Python - Version 1

1. Presentation du projet

Surveillance materielle avec Python est un projet de developpement d'un outil de surveillance des ressources materielles d'un ordinateur fonctionnant sous Debian Linux.

L'objectif est de concevoir un programme capable de collecter, d'analyser et d'afficher les informations relatives aux principales ressources materielles d'un ordinateur.

Le projet est developpe en Python selon une approche de programmation procedurale, sans utilisation de la programmation orientee objet.

2. Objectifs du projet

- Surveiller le taux d'utilisation du processeur.
- Identifier le nombre de coeurs logiques du processeur.
- Recuperer la frequence du processeur lorsqu'elle est disponible.
- Surveiller l'utilisation de la memoire vive.
- Controler l'espace disque utilise et disponible.
- Identifier les situations de forte utilisation des ressources.
- Enregistrer les mesures dans un fichier historique.

3. Fonctionnalites

3.1 Surveillance du processeur

- Recuperation du taux d'utilisation du processeur.
- Identification du nombre de coeurs logiques.
- Recuperation de la frequence actuelle du processeur.
- Classification du niveau d'utilisation selon trois etats : NORMAL, ATTENTION et CRITIQUE.
- Affichage des informations dans le terminal.
- Enregistrement des mesures avec leur date et leur heure.

3.2 Surveillance de la memoire vive

- Recuperation de la capacite totale de la memoire vive.
- Identification de la memoire utilisee.
- Identification de la memoire disponible.
- Calcul du pourcentage d'utilisation.
- Classification du niveau d'utilisation.

3.3 Surveillance du disque

- Identification de la capacite totale du disque.
- Recuperation de l'espace utilise.
- Recuperation de l'espace disponible.
- Calcul du pourcentage d'utilisation.
- Classification du niveau d'occupation.

4. Environnement technique

Systeme d'exploitation : Debian Linux

Langage de programmation : Python 3

Bibliotheque principale : psutil

Paradigme de programmation : Programmation procedurale

5. Installation

Cloner le depot GitHub :

```bash
git clone URL_DU_DEPOT
```

Acceder au repertoire du projet :

```bash
cd surveillance_materielle
```

Creer un environnement virtuel :

```bash
python3 -m venv .venv
```

Activer l'environnement virtuel :

```bash
source .venv/bin/activate
```

Installer les dependances :

```bash
pip install -r requirements.txt
```

6. Execution

Lancer le programme avec la commande suivante :

```bash
python3 main.py
```

 7. Structure du projet

```text
surveillance_materielle/
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- historique_cpu.txt
```

 8. Limites de la version 1

Cette premiere version se concentre sur la surveillance des principales ressources materielles de l'ordinateur.

Les fonctionnalites suivantes ne sont pas encore integrees :

- Surveillance des temperatures materielles.
- Analyse de l'etat des disques avec SMART.
- Surveillance de la batterie.
- Prediction automatique des pannes materielles.
- Generation de rapports detailles.

9. Evolutions envisagees

Les prochaines versions pourront integrer :

- La surveillance des temperatures du processeur.
- L'analyse de l'etat des disques.
- La surveillance de la batterie.
- Un systeme d'alertes.
- L'enregistrement et la consultation de l'historique complet.
- La generation de rapports de surveillance.

## 10. Auteur

NOUKOUKOU Senyenyо Gianni Loic

Etudiant en Licence Professionnelle en Systemes et Reseaux Informatiques.
