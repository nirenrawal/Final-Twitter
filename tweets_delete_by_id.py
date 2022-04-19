from bottle import delete
import g

##############################
@delete("/tweets/<tweet_id>")
@delete("/<language>/tweets/<tweet_id>")
def _(language = "en", tweet_id = ""):
  try:
    # Maybe the user enters a language that is not supported, then default to english
    # Use any key to see if the language is in the errors dictionary
    if f"{language}_server_error" not in g._errors : language = "en"
    
    tweet_id, error = g._is_uuid4(tweet_id, language)
    if error : return g._send(400, error)
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:
    db = g._db_connect("database.sqlite")
    counter = db.execute("DELETE FROM tweets WHERE tweet_id = ?", (tweet_id,)).rowcount
    db.commit()
    if not counter : return g._send(204, "")
    return {"info":"ok"}
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()






