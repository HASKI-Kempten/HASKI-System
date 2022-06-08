# HASKI-System

Das System benötigt folgende Packages:

NodeJS
Yarn
Python 3

Im Backend Ordner kann über eine virtuelle Umgebung Flask installiert werden. Für Linux:
  
    $ cd backend
    $ python3 -m venv venv
    $ source venv/bin/activate

Oder für Windows:

    $ cd backend
    $ python -m venv venv
    $ venv\Scripts\activate

Anschließend in den frontend Ordner wechseln und beides (in unterschiedlichen Terminals) starten:
    
    $ cd ..
    $cd frontend

Um das Frontend zu starten:

    $yarn start

Um das Backend zu starten:

    $yarn start-api
  
Das Frontend ist über localhost:3000 erreichbar, das Backend über localhost:5000/getLearningPath.
Derzeit ist dies nur ein rudimentärer Prototyp und soll nur die grundlegende Vorgehensweise aufzeigen.
Die APIs sind noch nicht ausdefiniert und spielen für das Frontend nur eine untergeordente Rolle.
