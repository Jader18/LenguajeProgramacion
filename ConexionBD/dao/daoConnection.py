import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()
        
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    
class DaoCity:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM cities'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM cities WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, city):
        query = 'INSERT INTO cities (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (city.name, city.status))
    
    def update(self, city):
        query = 'UPDATE cities SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (city.name, city.status, city.id))
    
    def delete(self, id):
        query = 'DELETE FROM cities WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    

class Daojob:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM jobs'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM jobs WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, job):
        query = 'INSERT INTO jobs (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (job.name, job.status))
    
    def update(self, job):
        query = 'UPDATE jobs SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (job.name, job.status, job.id))
    
    def delete(self, id):
        query = 'DELETE FROM jobs WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    


class DaoEmployee:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM employees'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM employees WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, employee):
        query = 'INSERT INTO employees (name, ciudad_id, job_id, salary, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (employee.name, employee.ciudad_id, employee.job_id, employee.salary, employee.status))
    
    def update(self, employee):
        query = 'UPDATE employees SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (employee.name, employee.status, employee.id))
    
    def delete(self, id):
        query = 'DELETE FROM employees WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    

