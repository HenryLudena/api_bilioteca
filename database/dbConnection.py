import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost", user="postgres", password="12345678", database="Biblioteca"
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM Libros")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as error:
    print(error)
finally:
    connection.close()
    print("Conexión cerrada")
