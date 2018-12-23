CREATE TABLE IF NOT EXISTS images (
    uuid NOT NULL INTEGER PRIMARY KEY,
    hash TEXT not null,
    image BLOB not null
)

CREATE INDEX idx_contacts_name ON images (hash)