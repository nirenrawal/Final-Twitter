DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                  TEXT UNIQUE NOT NULL,
  tweet_title               TEXT NOT NULL,
  tweet_text                TEXT NOT NULL,
  tweet_created_at          TEXT NOT NULL,
  tweet_created_at_date     TEXT NOT NULL,
  tweet_updated_at          TEXT NOT NULL,
  tweet_updated_at_date     TEXT NOT NULL,
  PRIMARY KEY(tweet_id)
); WITHOUT ROWID

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id                  TEXT UNIQUE NOT NULL,
  user_first_name          TEXT  NOT NULL,
  user_last_name           TEXT  NOT NULL,
  user_name                TEXT  NOT NULL,
  user_email               TEXT  NOT NULL,
  user_password            TEXT  NOT NULL,
  PRIMARY KEY(user_id)
); WITHOUT ROWID