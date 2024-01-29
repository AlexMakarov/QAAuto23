import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'C:\\Users\\Alexandr\\desktop\\work\\QAAuto23' + r'\\become_qa_auto.db')
        self.cursor = self.connection.cursor()
    

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQlite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"Select address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
              products.description, orders.order_date \
              FROM orders \
              JOIN customers ON orders.customer_id = customers.id \
              JOIN products ON orders.product_id = products.id"   
           
              
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

    
    def insert_customer(self, customer_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}', '{postalCode}','{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_postalcode(self):
        query = f"SELECT postalCode FROM customers "
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    
    def create_table(self):
        self.cursor.execute("DROP TABLE customers2")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS customers2 (id INTEGER PRIMARY KEY, name TEXT, address TEXT, city TEXT, postalCode TEXT, country TEXT)")
        query = ("INSERT INTO customers2 (id, name, address, city, postalCode, country) VALUES(1, 'Artem', 'Bethovena Str 5', 'Kyiv', '3030', 'Ukraine')")
        self.cursor.execute(query)
          
        self.cursor.execute("INSERT INTO customers2 VALUES(2, 'Anna', 'Savchenko Str 6', 'Dnipro', '5040', 'Ukraine')")
    
        self.connection.commit()
    

    def union_tables(self, city):
        query = f"SELECT * FROM customers WHERE city = '{city}' UNION SELECT * FROM customers2 WHERE city = '{city}' "
        
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    

