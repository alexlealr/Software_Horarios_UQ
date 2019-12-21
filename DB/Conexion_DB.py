import psycopg2


class AgregarDatos(object):

    def abrir(self):
        conexion = psycopg2.connect(database="trabajoFinal", user="postgres", password="12345")
        return conexion

    def add_docent(self, docent):
        cone = self.abrir(self)
        cursor = cone.cursor()
        datos = (docent.identification, docent.state, docent.semester_act, docent.horas_acom, docent.type_contra,
                 docent.person_identification, docent.pregrado, docent.postgrado)
        sql = "insert into docente(identificacion, estado, semestreactul, horas_acomul, tipocontrato, " \
              "persona_identificacion, pregrado, posgrado) values (%s,%s,%s, %s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
