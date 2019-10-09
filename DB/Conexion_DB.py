import psycopg2


def abrir(self):
    conexion = psycopg2.connect(database="trabajoFinal", user="postgres", password="12345")
    return conexion


def alta(self):
    cone = self.abrir()
    cursor = cone.cursor()
    datos = ("1094970055", "meliza", "velasuqez", "3146126046", "armenia")
    sql = "insert into docente(docente_id, nombre, apellido, telefono, ciudad) values (%s,%s,%s, %s,%s)"
    cursor.execute(sql, datos)
    cone.commit()
