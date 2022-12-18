BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Character";
CREATE TABLE IF NOT EXISTS "Character" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Enemy";
CREATE TABLE IF NOT EXISTS "Enemy" (
	"id"	INTEGER NOT NULL,
	FOREIGN KEY("id") REFERENCES "Character"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "SharedAttributes";
CREATE TABLE IF NOT EXISTS "SharedAttributes" (
	"shared_attributes_id"	INTEGER NOT NULL,
	"character_id"	INTEGER NOT NULL,
	"hp"	INTEGER NOT NULL,
	"dodge"	REAL NOT NULL,
	"prot"	INTEGER NOT NULL,
	"spd"	INTEGER NOT NULL,
	FOREIGN KEY("character_id") REFERENCES "Character"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("shared_attributes_id","character_id")
);
DROP TABLE IF EXISTS "EnemyAttributes";
CREATE TABLE IF NOT EXISTS "EnemyAttributes" (
	"shared_attributes_id"	INTEGER NOT NULL,
	"character_attributes_id"	INTEGER NOT NULL,
	"stealth"	INTEGER NOT NULL DEFAULT 0 CHECK("stealth" IN (0, 1)),
	FOREIGN KEY("character_attributes_id") REFERENCES "Character"("id") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("shared_attributes_id") REFERENCES "SharedAttributes"("shared_attributes_id") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("shared_attributes_id","character_attributes_id")
);
DROP TABLE IF EXISTS "ResolveLevels";
CREATE TABLE IF NOT EXISTS "ResolveLevels" (
	"level"	INTEGER NOT NULL CHECK("level" IN (1, 2, 3, 4, 5)),
	PRIMARY KEY("level" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "EnemyVariations";
CREATE TABLE IF NOT EXISTS "EnemyVariations" (
	"enemy_id"	INTEGER NOT NULL,
	"variation_id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("enemy_id","variation_id")
);
COMMIT;
