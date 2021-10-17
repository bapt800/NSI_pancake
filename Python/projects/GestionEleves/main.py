from SGBDD import *


db = DataBase()
#db.execute("INSERT INTO eleves (FirstName, LastName) VALUES ('Bilal', 'NomChelou')")
db.execute("SELECT * FROM `eleves`;")
db.closeStream()
