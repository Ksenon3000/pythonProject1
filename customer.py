import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="37495437",
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")
cur = con.cursor()

#Ввод данных пользователя
def customerAdd():
                cur = con.cursor()

                id = cur.execute("SELECT ID from CUSTOMER ")
                address = input("Введите адрес пользователя")
                phone = input("Введите телефон пользователя")
                name = input("Введите ФИО пользователя")
                book = ' '
                mas = (id, address, phone, name, book)

                cur = con.cursor()
                cur.execute(
                         f"INSERT INTO CUSTOMER (ID,ADDRESS,PHONE,NAME,BOOK) VALUES {mas}"
                         )


def output():
        cur.execute("SELECT ID, ADDRESS, PHONE, NAME, BOOK from CUSTOMER")

        rows = cur.fetchall()
        for row in rows:
            print("ID =", row[0])
            print("ADDRESS =", row[1])
            print("PHONE =", row[2])
            print("NAME =", row[3])
            print("BOOK =", row[4], "\n")


output()
con.commit()
con.close()