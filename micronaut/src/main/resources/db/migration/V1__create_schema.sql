CREATE SEQUENCE person_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE life_event_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE location_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE marriage_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE occupation_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE location
(
    id           BIGINT PRIMARY KEY DEFAULT nextval('location_seq'),
    version      BIGINT NOT NULL    DEFAULT 0,
    city         VARCHAR(255),
    country      VARCHAR(255),
    region       VARCHAR(255),
    notes        VARCHAR(5000),
    latitude     DOUBLE PRECISION,
    longitude    DOUBLE PRECISION,
    fetch_status VARCHAR(20) CHECK (fetch_status IN ('FETCHED_WITH_SUCCESS', 'AWAITING', 'FETCHED_WITH_ERRORS')),
    created_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE life_event
(
    id          BIGINT PRIMARY KEY                DEFAULT nextval('life_event_seq'),
    version     BIGINT                   NOT NULL DEFAULT 0,
    notes       VARCHAR(5000),
    day         INTEGER,
    month       INTEGER,
    year        INTEGER,
    date        DATE,
    location_id BIGINT REFERENCES location (id),
    created_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE person
(
    id           BIGINT PRIMARY KEY                DEFAULT nextval('person_seq'),
    version      BIGINT                   NOT NULL DEFAULT 0,
    first_name   VARCHAR(255),
    last_name    VARCHAR(255),
    middle_names VARCHAR(255),
    notes        VARCHAR(20000),
    sex          VARCHAR(7)                 NOT NULL CHECK (sex IN ('MAN', 'WOMAN', 'UNKNOWN')),
    pdf_page     INTEGER,
    father_id    BIGINT REFERENCES person (id),
    mother_id    BIGINT REFERENCES person (id),
    birth_id     BIGINT UNIQUE REFERENCES life_event (id),
    death_id     BIGINT UNIQUE REFERENCES life_event (id),
    burial_id    BIGINT UNIQUE REFERENCES life_event (id),
    created_at   TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at   TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE marriage
(
    id          BIGINT PRIMARY KEY                DEFAULT nextval('marriage_seq'),
    version     BIGINT                   NOT NULL DEFAULT 0,
    notes       VARCHAR(5000),
    spouse_1_id BIGINT NOT NULL REFERENCES person (id),
    spouse_2_id BIGINT NOT NULL REFERENCES person (id),
    location_id BIGINT REFERENCES location (id),
    day         INTEGER,
    month       INTEGER,
    year        INTEGER,
    date        DATE,
    created_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE occupation
(
    id          BIGINT PRIMARY KEY                DEFAULT nextval('occupation_seq'),
    version     BIGINT                   NOT NULL DEFAULT 0,
    notes       VARCHAR(5000),
    location_id BIGINT REFERENCES location (id),
    day         INTEGER,
    month       INTEGER,
    year        INTEGER,
    date        DATE,
    created_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE TABLE person_marriages
(
    person_id   BIGINT NOT NULL REFERENCES person (id),
    marriage_id BIGINT NOT NULL UNIQUE REFERENCES marriage (id)
);

CREATE TABLE person_occupations
(
    person_id     BIGINT NOT NULL REFERENCES person (id),
    occupation_id BIGINT NOT NULL UNIQUE REFERENCES occupation (id)
);
