from bottle import get
import g

##############################
@get("/tweets/<tweet_id>")
@get("/<language>/tweets/<tweet_id>")
def _(language = "en", tweet_id = ""):
  try:
    # Use any key to see if the language is in the errors dictionary
    if f"{language}_server_error" not in g._errors : language = "en"
    tweet_id, error = g._is_uuid4(tweet_id, language)
    if error : return g._send(400, error)
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:
    db = g._db_connect("database.sqlite")
    tweet = db.execute("SELECT * FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
    if not tweet: return g._send(204, "")
    return tweet
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()






