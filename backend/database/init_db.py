import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Initialize Elements 
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1', '0', 1656330943, 'Informatik I', 15, 3, 'visual, auditory, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 1', '0', 1656330943, 'Informatik I', 10, 3, 'visual, auditory', 'url:https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 2', '0', 1656330943, 'Informatik I', 10, 3, 'visual, auditory, interactive', 'url:https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Metriken Teil 2', '0', 1656330943, 'Informatik I', 11, 3, 'visual, auditory', 'url:https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Word Search', '1', 1656330943, 'Informatik I', 15, 3, 'visual, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Definition Metriken', '0', 1656330943, 'Informatik I', 15, 3, 'visual, text', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Text Wozu Metriken', '0', 1656330943, 'Informatik I', 15, 3, 'visual, text', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Arten von Metriken', '0', 1656330943, 'Informatik I', 5, 3, 'visual, text, image', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Eigenschaften von Metriken', '0', 1656330943, 'Informatik I', 7, 3, 'visual, iamge', 'ppt', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Schiebespiel Metriken zuordnen', '0', 1656330943, 'Informatik I', 20, 3, 'visual, image, interactiv', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Tueroeffner Bestimmte Metriken', '0', 1656330943, 'Informatik I', 20, 3, 'visual, image, interactive', 'h5p', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Haltstead Metrik C++', '0', 1656330943, 'Informatik I', 8, 3, 'visual, coding', 'quiz', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )
cur.execute("INSERT INTO element (name, difficulty, creationDate, module, averageDuration, semester, style, type, proLIST, contraLIST) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Haltstead Metrik C++ Aufgabe', '0', 1656330943, 'Informatik I', 20, 3, 'visual, interactive, coding', 'upload', 'Lorem Ipsum', 'Lorem Ipsum 2')
            )

#Initialize Modules
cur.execute("INSERT INTO module (name, module, semester) VALUES (?, ?, ?)",
            ('Informatik I', 'IT-1234', 1)
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
            ("Max Mustermann", 1, "active, verbal, sensing, gloabl", "Angewandte Informatik")
            )
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("Maria Musterfrau", 2, "active, visual, sensing, sequential", "Angewandte Informatik")
            )
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("Olaf Scholz", 5, "reflective, visual, intuitive, gloabl", "Angewandte Schlafforschung")
            )
cur.execute("INSERT INTO student (name, semester, style, courseOfStudy) VALUES (?, ?, ?, ?)",
            ("Das Kruemelmonster", 1, "reflective, verbal, sensing, sequential", "Ernaehrungswissenschaften")
            )

#Initialize StudentModules
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (1,1)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (2,1)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (2,2)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (3,3)
            )
cur.execute("INSERT INTO studentModule (studentId, moduleId) VALUES (?, ?)",
            (4,4)
            )

#Initalize learning Paths
cur.execute("INSERT INTO learningPath (moduleId, module) VALUES (?, ?)",
            (1, 'Informatik I')
            )

#Initialize Elements for Learning Paths
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (1, 1, '1.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (2, 1, '2.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (3, 1, '3.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (4, 1, '4.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (5, 1, '5.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (6, 1, '6.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (7, 1, '7.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (8, 1, '8.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (9, 1, '9.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (10, 1, '10.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (11, 1, '11.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (12, 1, '12.1')
            )
cur.execute("INSERT INTO elementMetaPath (elementId, learningPath, position) VALUES (?, ?, ?)",
            (13, 1, '13.1')
            )

#Initialize Learning Ways
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Informatik I', 1, 1, 1)
            )
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Einfuehrung in die Programmierung', 2, 1, 12)
            )
cur.execute("INSERT INTO learningWay (module, moduleId, studentId, recommendedElement) VALUES (?, ?, ?, ?)",
            ('Informatik I', 1, 2, 1)
            )

#Initialize Learning Way Elements
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (1, True, 1656330943, "2.0", "1.1", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, doneAt, evaluation, position, learningWayId) VALUES (?, ?, ?, ?, ?, ?)",
            (2, True, 1656330943, "1.3", "2.1", 1)
            )
cur.execute("INSERT INTO learningWayElement (elementId, done, position, learningWayId) VALUES (?, ?, ?, ?)",
            (3, False, "3.1", 1)
            )

connection.commit()
connection.close()