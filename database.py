import sqlite3

class Database():
    _instance = None  # Atributo de clase para almacenar la única instancia

    def __new__(cls, db_name="dbDAO.db"):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db_name="dbDAO.db"):
        if not self._initialized:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self.create_tables()
            self._initialized = True  # Marca la instancia como inicializada
        

    def create_tables(self):


        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                            id_cliente INTEGER PRIMARY KEY,
                            nombre TEXT,
                            apellido TEXT,
                            direccion TEXT,
                            telefono TEXT
                            )
            ''')
        

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS autos (
                vin INTEGER PRIMARY KEY,
                marca TEXT,
                modelo TEXT,
                anio INTEGER,
                precio REAL,
                estado TEXT,
                cliente_id TEXT,
                FOREIGN KEY(cliente_id) REFERENCES clientes(id_cliente)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendedores (
                            id_vendedor INTEGER PRIMARY KEY,
                            nombre TEXT,
                            apellido TEXT,
                            comision FLOAT(5,2)
                            )
            ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                            id_venta INTEGER PRIMARY KEY,
                            id_auto INTEGER,
                            id_cliente INTEGER,
                            fecha DATE,
                            id_vendedor INTEGER
                            )
            ''')
        
        self.connection.commit()
    
    def agregar_cliente(self,id_cliente,nombre,apellido,direccion,telefono):

        self.cursor.execute('''INSERT INTO clientes (id_cliente,nombre,apellido,direccion,telefono) 
                            VALUES(?,?,?,?,?)
                            ''',(id_cliente,nombre,apellido,direccion,telefono))
        self.connection.commit()

    
    def get_clientes(self):
        
        self.cursor.execute("SELECT id_cliente,nombre,apellido,direccion,telefono FROM clientes")
        return self.cursor.fetchall()
    



    def agregar_auto(self,vin,marca,modelo,anio,precio,estado,cliente_id):

        self.cursor.execute('''INSERT INTO autos (vin,marca,modelo,anio,precio,estado,cliente_id) 
                            VALUES(?,?,?,?,?,?,?)
                            ''',(vin,marca,modelo,anio,precio,estado,cliente_id))
        self.connection.commit()

    def get_autos(self):
        
        self.cursor.execute("SELECT vin,marca,modelo,anio,precio,estado,cliente_id FROM autos")
        return self.cursor.fetchall()
    
    def agregar_vendedor(self,id_cliente,nombre,apellido,comision):

        self.cursor.execute('''INSERT INTO vendedores (id_vendedor,nombre,apellido,comision) 
                            VALUES(?,?,?,?)
                            ''',(id_cliente,nombre,apellido,comision))
        self.connection.commit()

    
    def get_vendedores(self):
        
        self.cursor.execute("SELECT id_vendedor,nombre,apellido,comision FROM vendedores")
        return self.cursor.fetchall()
    
    
    def agregar_venta(self,id_venta,id_auto,id_cliente,fecha,id_vendedor):

        self.cursor.execute('''INSERT INTO ventas (id_venta,id_auto,id_cliente,fecha,id_vendedor) 
                            VALUES(?,?,?,?,?)
                            ''',(id_venta,id_auto,id_cliente,fecha,id_vendedor))
        self.connection.commit()

    
    def get_ventas(self):
        
        self.cursor.execute("SELECT id_venta,id_auto,id_cliente,fecha,id_vendedor FROM ventas")
        return self.cursor.fetchall()

    
    def close(self):
        self.connection.close()