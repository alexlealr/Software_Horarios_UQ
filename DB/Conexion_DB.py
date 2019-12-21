import psycopg2

class AgregarDatos(object):

    def abrir():
        conexion = psycopg2.connect(database="trabajoFinal", user="postgres", password="12345")
        return conexion


    def alta():
        cone = abrir()
        cursor = cone.cursor()
        datos = ("1094970055", "meliza", "velasuqez", "3146126046", "armenia")
        sql = "insert into docente(docente_id, nombre, apellido, telefono, ciudad) values (%s,%s,%s, %s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
