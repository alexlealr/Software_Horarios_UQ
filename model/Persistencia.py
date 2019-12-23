import DB.Conexion_DB
import model.Docent
from model.Docent import Docent
from model.Context.Context import Context

class Persistencia(object):

    def new_Docent(self, identification: str, state: str, semester_act: str, horas_acom: int, type_contra: str,
                   person_identification: int, pregrado: str, postgrado: str):
        docente = Docent(identification, state, semester_act, horas_acom, type_contra,
                         person_identification, pregrado, postgrado)
        Context.new_docent(docente)
