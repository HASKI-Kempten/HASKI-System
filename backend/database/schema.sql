DROP TABLE IF EXISTS element;

CREATE TABLE element(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    creationDate INTEGER NOT NULL,
    module TEXT NOT NULL,
    averageDuration INTEGER NOT NULL,
    semester INTEGER NOT NULL,
    style TEXT NOT NULL,
    type TEXT NOT NULL,
    proLIST TEXT NOT NULL,
    contraLIST TEXT NOT NULL
);

DROP TABLE IF EXISTS module;

CREATE TABLE module(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    module TEXT NOT NULL,
    semester INTEGER NOT NULL
);

DROP TABLE IF EXISTS student;

CREATE TABLE student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    semester INTEGER NOT NULL,
    style TEXT NOT NULL,
    courseOfStudy TEXT NOT NULL
);

DROP TABLE IF EXISTS studentModule;

CREATE TABLE studentModule(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER NOT NULL REFERENCES student(id),
    moduleId INTEGER NOT NULL REFERENCES module(id)
);

DROP TABLE IF EXISTS learningPath;

CREATE TABLE learningPath(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    moduleId INTEGER NOT NULL REFERENCES module(id),
    module TEXT NOT NULL REFERENCES module(name)
);

DROP TABLE IF EXISTS elementMetaPath;

CREATE TABLE elementMetaPath(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    elementId INTEGER NOT NULL REFERENCES element(id),
    learningPath INTEGER NOT NULL REFERENCES learningPath(id),
    position TEXT NOT NULL
);

DROP TABLE IF EXISTS learningWay;

CREATE TABLE learningWay(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module TEXT NOT NULL REFERENCES module(name),
    moduleId INTEGER NOT NULL REFERENCES module(id),
    studentId INTEGER NOT NULL REFERENCES student(id),
    recommendedElement INTEGER
);

DROP TABLE IF EXISTS learningWayElement;

CREATE TABLE learningWayElement(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    elementId INTEGER NOT NULL,
    done BOOLEAN NOT NULL,
    doneAt INTEGER,
    evaluation TEXT,
    position TEXT NOT NULL,
    learningWayId INTEGER NOT NULL REFERENCES learningWay(id)
);