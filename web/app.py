from flask import Flask
import sqlite3 as lite

app = Flask(__name__)
DATABASE = '/tmp/database.db'

@app.route('/')
def hello():
	con = None
	upd = None

	con = lite.connect(DATABASE)
	c = con.cursor()
	try:  
	  c.execute('CREATE TABLE counters (id INTEGER PRIMARY KEY AUTOINCREMENT, waktu INTEGER)')
	except:
	  pass
	finally:
	  c.execute('SELECT waktu from counters where id="1"')
	  count = c.fetchone()
	  if count == None:
	    c.execute('INSERT INTO counters(waktu) values("1")')
	    upd = 1
	  elif count[0] == None:
	    pass
	  else:
	    upd = int(count[0]) + 1
	    c.execute('UPDATE counters SET waktu="'+ str(upd) +'" where id="1"')
	  con.commit()
	  c.close()
	  if con:
	    con.close()

	return 'Hello World! I have been seen {} times.\n'.format(upd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
