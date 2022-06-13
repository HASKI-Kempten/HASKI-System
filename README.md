# HASKI-System

Das System benötigt folgende Packages:

NodeJS
Yarn
Python 3

Im Backend Ordner kann über eine virtuelle Umgebung Flask installiert werden. Für Linux:

    $ cd backend
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install Flask

Oder für Windows:

    $ cd backend
    $ python -m venv venv
    $ venv\Scripts\activate
    $ pip install Flask
    $ pip install python-dotenv

Anschließend in den frontend Ordner wechseln:

    $ cd ..
    $cd frontend

Als nächstes die für yarn benötigten Packages installieren:

    $ yarn install

Und beides (in unterschiedlichen Terminals) starten:
Um das Frontend zu starten:

    $yarn start

Um das Backend zu starten:

    $yarn start-api

Das Frontend ist über localhost:3000 erreichbar, das Backend über localhost:5000/getLearningPath.
Derzeit ist dies nur ein rudimentärer Prototyp und soll nur die grundlegende Vorgehensweise aufzeigen.
Die APIs sind noch nicht ausdefiniert und spielen für das Frontend nur eine untergeordente Rolle.
