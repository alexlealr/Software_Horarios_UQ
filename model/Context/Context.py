from DB.Conexion_DB import AgregarDatos


class Context(object):
    def new_docent(self, docente):
        db = AgregarDatos()
        db.add_docent(docente)
