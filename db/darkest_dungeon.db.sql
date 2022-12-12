BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Character";
CREATE TABLE IF NOT EXISTS "Character" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"bleed"	REAL NOT NULL,
	"blight"	REAL NOT NULL,
	"debuff"	REAL NOT NULL,
	"death_blow"	REAL NOT NULL,
	"disease"	REAL NOT NULL,
	"move"	REAL NOT NULL,
	"stun"	REAL NOT NULL,
	"trap"	REAL NOT NULL,
	"movement"	TEXT NOT NULL,
	"crit_buff_bonus"	TEXT NOT NULL,
	"religious"	INTEGER NOT NULL,
	"provisions"	TEXT,
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "CharacterlevelLevels";
CREATE TABLE IF NOT EXISTS "CharacterlevelLevels" (
	"id"	INTEGER NOT NULL UNIQUE,
	"character_id"	INTEGER NOT NULL,
	"level"	INTEGER NOT NULL,
	"max_hp"	INTEGER NOT NULL,
	"dodge"	INTEGER NOT NULL,
	"prot"	REAL NOT NULL,
	"spd"	INTEGER NOT NULL,
	"acc_mod"	REAL NOT NULL,
	"crit"	REAL NOT NULL,
	"lower_dmg"	INTEGER NOT NULL,
	"upper_dmg"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "Character"("id") ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS "CharacterSkill";
CREATE TABLE IF NOT EXISTS "CharacterSkill" (
	"id"	INTEGER NOT NULL UNIQUE,
	"character_id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"on_range"	TEXT NOT NULL,
	"rank"	TEXT NOT NULL,
	"target"	TEXT NOT NULL,
	"dmg_mod"	REAL NOT NULL,
	"acc"	INTEGER NOT NULL,
	"crit_mod"	REAL NOT NULL,
	"heal"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_id") REFERENCES "Character"("id") ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS "Effect";
CREATE TABLE IF NOT EXISTS "Effect" (
	"id"	INTEGER NOT NULL UNIQUE,
	"character_skill_id"	INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("character_skill_id") REFERENCES "CharacterSkill"("id") ON UPDATE CASCADE ON DELETE CASCADE
);
INSERT INTO "Character" ("id","name","bleed","blight","debuff","death_blow","disease","move","stun","trap","movement","crit_buff_bonus","religious","provisions") VALUES (1,'ADSF',1.0,11.0,1.0,1.0,1.0,1.0,1.0,1.0,'1','1',1,NULL),
 (2,'2',2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,'0','2',0,'');
COMMIT;
