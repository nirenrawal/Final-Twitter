from bottle import put, request
import g
import time
from datetime import datetime

##############################
@put("/tweets/<tweet_id>")
@put("/<language>/tweets/<tweet_id>")
def _(language="en", tweet_id=""):

  # VALIDATE
  try:
    # Use any key to see if the language is in the errors dictionary
    if f"{language}_server_error" not in g._errors : language = "en"
    tweet_id, error = g._is_uuid4(tweet_id, language)
    if error : return g._send(400, error)      

    allowed_keys = ["tweet_title", "tweet_text",]
    for key in request.forms.keys():
      if not key in allowed_keys:
        print(key)
        return g._send(400, f"Forbidded key {key}")

  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])


  try:
    # Get the item to overwrite it with new data
    db = g._db_connect("database.sqlite")
    tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
    if not tweet: return g._send(204, "")
    # The item has been fetched from the db, now overwrite the fields with the new values
    for key in tweet.keys():
      if key in request.forms.keys():
        tweet[key] = request.forms.get(key)
    # Validate the newly updated item
    tweet_title, error = g._is_tweet_title(tweet["tweet_title"], language)
    if error : return g._send(400, error)
    tweet_text, error = g._is_tweet_text(tweet["tweet_text"], language)
    if error : return g._send(400, error)
    
    if error : return g._send(400, error)
    # Update the field
    tweet ["tweet_title"] = tweet_title
    tweet["tweet_updated_at"] = str(int(time.time()))
    now = datetime.now()
    tweet["tweet_updated_at_date"] = now.strftime("%Y-%B-%d-%A %H:%M:%S")
    # Save the item with its updated values
    counter = db.execute("""UPDATE tweets 
                  SET tweet_title=:tweet_title, 
                  tweet_text=:tweet_text,
                  tweet_updated_at =:tweet_updated_at,
                  tweet_updated_at_date = :tweet_updated_at_date 
                  WHERE tweet_id = :tweet_id""", tweet).rowcount
    db.commit()
    if not counter : return g._send(204, "")
    return tweet
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()

  






