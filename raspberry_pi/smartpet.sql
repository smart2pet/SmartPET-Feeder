PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "plan" (
  "hours" integer NOT NULL,
  "minutes" integer NOT NULL,
  "weights" integer NOT NULL
);
CREATE TABLE history (
    hours   INTEGER NOT NULL,
    minutes INTEGER NOT NULL,
    weight  INTEGER NOT NULL,
    year    INTEGER NOT NULL,
    month   INTEGER NOT NULL,
    day     INTEGER NOT NULL
);

COMMIT;
