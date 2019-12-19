import sqlite3
conn = sqlite3.connect("E-VOTING.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS masterlogin(USERNAME TEXT)")
conn.commit()
conn.close()