import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Initialize Elements 
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 Kurzuberblick', '0', 1656330943, 'Informatik I', 15, 3, 'visual, auditory, interactive', 'Text', 'Lorem Ipsum', 'Lorem Ipsum 2', '- Definition von Metrik -Unterschiedliche Verwendungszwecke von Metriken -Verschiedene Arten von Metriken und Einordnung von einigen Metriken ')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 Beispiel & Lektion', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'url', 'Lorem Ipsum', 'Lorem Ipsum 2','https://www.youtube.com/embed/kXUAFFOTt-k')
            )              
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 uebung', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'Picture', 'Lorem Ipsum', 'Lorem Ipsum 2', 'wortsuche.png')
            )   
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 Zusatzliteratur', '0', 1656330943, 'Informatik I', 15, 3, 'visual, auditory, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','Inhalt zusatzliteratur')
            )     
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 Selbsteinschaetzungstest', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'Picture', 'Lorem Ipsum', 'Lorem Ipsum 2', 'Ziehen.png')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 Zusammenfassung', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'Text', 'Lorem Ipsum', 'Lorem Ipsum 2', 'Eine Metrik wird folgendermassen definiert Eine Metrik ist im Software Engineering eine quantifizierte Aussage ueber ein Artefakt, einen Prozess oder ein Projekt. Dabei bedeutet quantifizierte Aussage, dass eine Information in Zahlenform vorliegt und so verglichen werden kann.\n'+
            'Eine Metrik hilft dabei: \n'+
            '- Probleme zu identifizieren\n'+
            '- Neue Methoden zu testen\n'+
            '- Produkte zu beurteilen-\n'+
            '- Auftraggeber zu informieren (Transparenz)-\n'+
            '- Komplexitaet, Qualitaet und Einhaltung des Standards zu kontrollieren-\n'+
            '- Abschaetzung des Aufwands, der Kosten und der Zeit-\n'+            
            '- Verfolgung des Aufwands, der Kosten und der Zeit\n'+ 
            'Metriken koennen in folgende Arten eingeteilt werden: Produkt-, Prozess-, und Projektmasse. Diese Masse werden durch verschiedene Methoden gemessen.'
             )
            )       
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1 uebung', '0', 1656330943, 'Informatik I', 15, 3, 'visual, auditory, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )   
#### mock other
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1', '0', 1656330943, 'Informatik I', 15, 3, 'visual, auditory, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1', '0', 1656330943, 'Informatik I', 10, 3, 'visual, auditory', 'url', 'Lorem Ipsum', 'Lorem Ipsum 2','https://www.youtube.com/embed/kXUAFFOTt-k')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 2', '0', 1656330943, 'Informatik I', 10, 3, 'visual, auditory, interactive', 'url', 'Lorem Ipsum', 'Lorem Ipsum 2','https://www.youtube.com/embed/kXUAFFOTt-k')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 2', '0', 1656330943, 'Informatik I', 11, 3, 'visual, auditory', 'url', 'Lorem Ipsum', 'Lorem Ipsum 2','https://www.youtube.com/embed/kXUAFFOTt-k')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Word Search', '1', 1656330943, 'Informatik I', 15, 3, 'visual, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Definition Metriken', '0', 1656330943, 'Informatik I', 15, 3, 'visual, text', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Text Wozu Metriken', '0', 1656330943, 'Informatik I', 15, 3, 'visual, text', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Arten von Metriken', '0', 1656330943, 'Informatik I', 5, 3, 'visual, text, image', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Eigenschaften von Metriken', '0', 1656330943, 'Informatik I', 7, 3, 'visual, iamge', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Schiebespiel Metriken zuordnen', '0', 1656330943, 'Informatik I', 20, 3, 'visual, image, interactiv', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Tueroeffner Bestimmte Metriken', '0', 1656330943, 'Informatik I', 20, 3, 'visual, image, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Haltstead Metrik C++', '0', 1656330943, 'Informatik I', 8, 3, 'visual, coding', 'quiz', 'Lorem Ipsum', 'Lorem Ipsum 2','content successful')            
            )            
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST,content) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Haltstead Metrik C++ Aufgabe', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'upload', 'Lorem Ipsum', 'Lorem Ipsum 2', 'content successful')
            )
 

#Initialize Modules
cur.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            ('Metrikne I', 'IT-1234', 1)
            )
cur.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            ('Einfuehrung in die Programmierung', 'IT-1478', 2)
            )
cur.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            ('Redekunst', 'AS-1478', 6)
            )
cur.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            ('Professionelles Kruemmeln', 'EW-3570', 5)
            )

#Initialize Students
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("Jim Haug", 1, "balanciert, intuitiv, visuell, balanciert", "Angewandte Informatik")
            )
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("Marc Normann", 1, "balanciert, balanciert, visuell, global", "Angewandte Informatik")
            )
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("David Fischer", 1, "active, intuitiv, visuell, balanciert", "Angewandte Informatik")
            )


#Initialize StudentModules
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (1,1)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (2,1)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (3,1)
            )

#Initalize learning Paths
cur.execute("INSERT INTO learningPath (moduleId, module) VALUES (?, ?)",
            (1, 'Metriken I')
            )

#Initialize Elements for Learning Paths
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (1, 1, '1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (2, 1, '2')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (3, 1, '3')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (4, 1, '4')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (5, 1, '5')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (6, 1, '6')
            )


#Initialize Learning Ways
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Metriken I', 1, 1, 1)
            )           
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Metriken I', 1, 2, 1)
            )
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Metriken I', 1, 3, 1)
            )

#Initialize Learning Way Elements
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (1, False, 1656330943, "", "1", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (2, False, 1656330943, "", "2", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (3, False, 1656330943, "", "3", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (4, False, 1656330943, "", "4", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (5, False, 1656330943, "", "5", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (6, False, 1656330943, "", "6", 1)
            )

cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (1, False, 1656330943, "", "1", 2)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (2, False, 1656330943, "", "2", 2)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (6, False, 1656330943, "", "3", 2)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (5, False, 1656330943, "", "4", 2)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (3, False, 1656330943, "", "5", 2)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (4, False, 1656330943, "", "6", 2)
            )

cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (1, False, 1656330943, "", "1", 3)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (2, False, 1656330943, "", "2", 3)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (3, False, 1656330943, "", "3", 3)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (5, False, 1656330943, "", "4", 3)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (4, False, 1656330943, "", "5", 3)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (6, False, 1656330943, "", "6", 3)
            )

connection.commit()
connection.close()