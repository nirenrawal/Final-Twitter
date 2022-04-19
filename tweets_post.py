from bottle import post, request
import g
import uuid
import time
from datetime import datetime

##############################
@post("/tweets")
@post("/<language>/tweets")
def _(language = "en"):
  try:
   #just to make user that the user does not type anyother language
    if f"{language}_server_error" not in g._errors : language = "en"

    tweet_title, error = g._is_tweet_title(request.forms.get("tweet_title"), language)
    if error : return g._send(400, error)
    tweet_text, error = g._is_tweet_text(request.forms.get("tweet_text"), language)
    if error : return g._send(400, error)    
    tweet_id = str(uuid.uuid4())
    tweet_created_at = str(int(time.time()))
    now = datetime.now()
    tweet_created_at_date = now.strftime("%Y-%B-%d-%A %H:%M:%S")
    tweet_updated_at = ""
    tweet_updated_at_date = ""
    tweet = {
      "tweet_id":tweet_id,
      "tweet_title":tweet_title,
      "tweet_text":tweet_text,
      "tweet_created_at":tweet_created_at,
      "tweet_created_at_date":tweet_created_at_date,
      "tweet_updated_at":tweet_updated_at,
      "tweet_updated_at_date":tweet_updated_at_date
    }
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:    
    db = g._db_connect("database.sqlite")
    db.execute("""INSERT INTO tweets 
                VALUES(:tweet_id, :tweet_title, :tweet_text, :tweet_created_at, 
                :tweet_created_at_date, :tweet_updated_at, :tweet_updated_at_date)""", tweet)
    db.commit()
    return tweet
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()