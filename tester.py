import sqlite3
#conn = sqlite3.connect("E-VOTING.db")
#cur = conn.cursor()
##email = input("EMAIL>>> ")
##cur.execute("SELECT * FROM test WHERE USERNAME = ?",(email,))
##result = cur.fetchall()
##for row in result:
##    name = row[0]
##    surname = row[1]
##    print("welcome",namesurname)
#conn = sqlite3.connect("E-VOTING.db")
#cur = conn.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS masterlogin(USERNAME TEXT)")
#conn.commit()
#conn.close()

conn = sqlite3.connect("E-VOTING.db")
cur = conn.cursor()
results = cur.execute("SELECT * FROM masterlogin")
result = results.fetchall()
final = list(result)
    #print(final)
query = final[-1]
    #print(query)
    #result2 = cur.execute("SELECT * FROM registered_voters WHERE EMAIL = ?" ,(query,))
result2 = cur.execute("SELECT * FROM registered_voters WHERE EMAIL = ? ",(query))
query2 = result2.fetchall()
for lists in query2:
    name = lists[0]
    surname = lists[1]
    mat = lists[2]
    school = lists[3]
    email = lists[4]
    
#print(name,surname,mat,school,email)

student_name = name + " " + surname
student_mat = mat
student_details = school
student_email = email

#print(student_mat)


def print_details():
    mat = student_mat
    print(mat)
    
print_details()
   
    
    