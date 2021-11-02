import mysql.connector

def connectDB(Enforcement):
    def inside(*args, **kwargs):
        db = mysql.connector.connect(user='root', password='123456', host='localhost', database='hotel_management',charset = 'utf8')
        mycursor = db.cursor(dictionary=True,buffered=True)
        with db:
            result = Enforcement(mycursor, *args, **kwargs)
            db.commit()
            return result
    return inside

