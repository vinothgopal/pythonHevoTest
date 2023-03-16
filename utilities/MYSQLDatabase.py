import mysql.connector

class MySQLDatabase:
    def _init_(self, host, port, user, password, database):
        self.host = host
        self.port= port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name):
        cursor = self.connection.cursor()
        create_query = f"CREATE TABLE {table_name}(id SERIAL PRIMARY KEY,name VARCHAR(50) NOT NULL,age INTEGER,last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        cursor.execute(create_query)
        self.connection.commit()
        print("Table created successfully!")

    def insert_record(self, table_name, name, age):
        cursor = self.connection.cursor()
        insert_query = f"INSERT INTO {table_name}(name, age) VALUES ('{name}', {age})"
        cursor.execute(insert_query)
        self.connection.commit()
        print(f"record inserted name :{name} age {age}")

    def update_record(self, table_name, old_value, new_value):
        cursor = self.connection.cursor()
        update_query = f"update {table_name} set name='{new_value}' where name='{old_value}'"
        cursor.execute(update_query)
        self.connection.commit()
        print(f"record updated name :{old_value} age {new_value}")

    def drop_table(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.connection.commit()

    def fetch_all_details_from_mysql(self,table_name):
        try:
            cursor = self.connection.cursor()
            select_query = f"select * from {table_name}"
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        except:
            print("unable to fetch the table values")

