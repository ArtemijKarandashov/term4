CREATE TABLE IF NOT EXISTS "rates"(
    "charcode"  TEXT NOT NULL UNIQUE,
    "value"     REAL NOT NULL,
    'nominal'   INTEGER NOT NULL,
    "added"     TEXT NOT NULL,
    PRIMARY KEY ("charcode")
)