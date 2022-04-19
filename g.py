from bottle import response
import sqlite3
import re

_errors = {
  "en_server_error":"server error",
  "en_json_error":"invalid json",
}

##############################
def _send(status = 400, error_message = "unknown error"):
  response.status = status
  return {"info":error_message}

# ##############################
def _is_tweet_title(text=None, language="en"):
  min, max = 2, 20
  errors = {
    "en":f"tweet_title {min} to {max} characters. No spaces", 
  }
  if not text: return None, errors[language]
  text = re.sub("[\n\t]*", "", text)
  text = re.sub(" +", " ", text)
  text = text.strip()
  if len(text) < min or len(text) > max : return None, errors[language]
  # if " " in text : return None, errors[language]
  text = text.capitalize()
  return text, None

# ##############################


#   ##############################
def _is_tweet_text (text=None, language="en"):
  min, max = 10, 500
  errors = {
    "en":f"tweet_text {min} to {max} characters. No spaces", 
  }
  if not text: return None, errors[language]
  text = re.sub("[\n\t]*", "", text)
  text = re.sub(" +", " ", text)
  text = text.strip()
  if len(text) < min or len(text) > max : return None, errors[language]
  # if " " in text : return None, errors[language]
  text = text.capitalize()
  return text, None
  


# ##############################
def _is_uuid4(text=None, language="en"):
  errors = {
    "en":f"tweet_id must be uuid4", 
  }
  if not text: return None, errors[language]
  regex_uuid4 = "^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
  if not re.match(regex_uuid4, text) : return None, errors[language]
  return text, None

# ##############################
def create_json_from_sqlite_result(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

##############################
def _db_connect(db_name):
  db = sqlite3.connect(db_name)
  db.row_factory = create_json_from_sqlite_result
  return db

























