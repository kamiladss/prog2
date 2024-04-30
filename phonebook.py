import psycopg2
import csv
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="kami26", port=5432)
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20)
);
""")
conn.commit()

def insert_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    print("Data inserted from CSV successfully.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Data inserted from console successfully.")

def update_data(name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Data updated successfully.")

def query_data(filter=None):
    if filter:
        cur.execute("SELECT * FROM PhoneBook WHERE " + filter)
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted successfully.")

# Example usage
#insert_from_csv('bookfile.csv')
#insert_from_console()
#update_data("Jane", new_name="Jannet")
#query_data("phone LIKE '%55%'")
delete_data(name=" ")

cur.close()
conn.close()
