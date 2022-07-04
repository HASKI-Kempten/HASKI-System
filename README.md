# HASKI-System

## Das System benötigt folgende Packages:

NodeJS

Yarn

Anaconda (nur bei Windows)

Python 3

## Installation

Im Backend Ordner kann über eine virtuelle Umgebung die benötigten packages installiert werden.
Linux:

    $ cd backend
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

Windows (Anaconda):

    $ cd backend
    $ conda create --name haski
    $ conda activate haski
    $ pip install -r requirements.txt

Anschließend in den frontend Ordner wechseln:

    $ cd ../frontend

Als nächstes die für yarn benötigten Packages installieren:

    $ yarn install

Die Daten für die APIs kommen aus einer SQLite3 Datenbank, welche lokal aufgesetzt ist.
Um diese zu initialisieren, folgende Schritte befolgen:

    $ cd backend/database
    $ python init_db.py

Frontend und Backend (in unterschiedlichen Terminals) starten:
Um das Frontend zu starten:

    $yarn start

Um das Backend zu starten:
Linux:

    $yarn start-api

Windows:

    $yarn start-api-conda

Das Frontend ist über localhost:3000 erreichbar, das Backend über localhost:5000.
Derzeit ist dies nur ein rudimentärer Prototyp und soll nur die grundlegende Vorgehensweise aufzeigen.
Die APIs sind noch nicht ausdefiniert und spielen für das Frontend nur eine untergeordente Rolle.
