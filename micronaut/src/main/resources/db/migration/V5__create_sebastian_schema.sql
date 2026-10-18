CREATE SCHEMA IF NOT EXISTS sebastian;

CREATE SEQUENCE sebastian.tracked_media_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE sebastian.tracked_media_watch_seq START WITH 1 INCREMENT BY 1;


CREATE TABLE sebastian.tracked_media
(
    id           BIGINT PRIMARY KEY       DEFAULT NEXTVAL('sebastian.tracked_media_seq'),
    version      BIGINT       NOT NULL    DEFAULT 0,
    type         VARCHAR(17)  NOT NULL CHECK (type IN ('MOVIE', 'TV')),
    title        VARCHAR(255) NOT NULL,
    release_date DATE         NOT NULL,
    tmdb_id      INTEGER      NOT NULL,
    rating       FLOAT,
    poster_path  VARCHAR(255) NOT NULL,
    created_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at   TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE sebastian.tracked_media_watch
(
    id               BIGINT PRIMARY KEY                DEFAULT NEXTVAL('sebastian.tracked_media_watch_seq'),
    version          BIGINT                   NOT NULL DEFAULT 0,
    tracked_media_id BIGINT                   NOT NULL REFERENCES sebastian.tracked_media (id),
    timestamp        TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at       TIMESTAMP WITH TIME ZONE          DEFAULT NOW(),
    updated_at       TIMESTAMP WITH TIME ZONE          DEFAULT NOW()
);
