import psycopg2

con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="37495437",
  host="127.0.0.1",
  port="5432"
)

con.autocommit = True

with con:
    with con.cursor() as cursor:
        cursor.execute(
            "select COLUMN_NAME from information_schema.columns\
            where table_name='products'")
        column_names = [row[0] for row in cursor]

print("Column names:\n")

for i in column_names:
    print(i)



print("Database opened successfully")
cur = con.cursor()

#Ввод данных пользователя
def customerAdd():
                cur = con.cursor()


                id = 1
                author = input("Введите автора книги")
                bookName = input("Введите название книги")
                quantity = input("Введите количество книг")
                description = input("Введите описание книги")

                mas = (id, author, bookName, quantity, description)

                cur = con.cursor()
                cur.execute(
                         f"INSERT INTO BOOK (ID,AUTHOR,NAME,QUANTITY,DESCRIPTION) VALUES {mas}"
                         )


def output():
        cur.execute("SELECT ID, ADDRESS, PHONE, NAME, BOOK from CUSTOMER")
        cur.execute("select column_name,data_type from information_schema.columns where table_name = 'table_name';")
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