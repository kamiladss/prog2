import psycopg2
import csv
# Connect to PostgreSQL
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

#11lab
#def to return pattens
def search_phonebook(pattern):
    cur.execute("SELECT * FROM PhoneBook WHERE name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    return rows

#def for adding new
def insert_or_update_user(new_name, new_phone):
    cur.execute("SELECT id FROM PhoneBook WHERE name = %s", (new_name,))
    existing_user = cur.fetchone()
    if existing_user:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE id = %s", (new_phone, existing_user[0]))
    else:
        cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (new_name, new_phone))
    conn.commit()
    
#def for large adding
def insert_many_users(user_data):
    incorrect_data = []
    for user_row in user_data:
        user_name, user_phone = user_row
        if len(user_phone.strip()) != 10:
            incorrect_data.append((user_name, user_phone))
        else:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (user_name, user_phone))
    conn.commit()
    return incorrect_data

#def for pages
def get_phonebook_page(limit_val, offset_val):
    cur.execute("SELECT * FROM PhoneBook LIMIT %s OFFSET %s", (limit_val, offset_val))
    rows = cur.fetchall()
    return rows

#def for deleting
def delete_data_name_phone(username=None, phone=None):
    if username:
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (username,))
    elif phone:
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()

# Example usage for 11lab
#print(search_phonebook(pattern="123"))
#print(insert_or_update_user(new_name="Jane", new_phone="999-123-123-77"))
#insert_many_users(user_data=[("Alice", "1234567890"),("Bob", "9876543210"),("Charlie", "5555555555"),("David", "123")])
#print(get_phonebook_page(limit_val=4, offset_val=5))
print(delete_data_name_phone(username="Charlie", phone="5555555555"))

# Close cursor and connection
cur.close()
conn.close()