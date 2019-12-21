class Docent(object):
    __identification: str
    __state: str
    __semester_act: str
    __horas_acom: int
    __type_contra: str
    __person_identification: int
    __pregrado: str
    __postgrado: str

    def __init__(self, identification: str, state: str, semester_act: str, horas_acom: int, type_contra: str,
               person_identification: int, pregrado: str, postgrado: str):
        self.identification = identification
        self.state = state
        self.semester_act = semester_act
        self.horas_acom = horas_acom
        self.type_contra = type_contra
        self.person_identification = person_identification
        self.pregrado = pregrado
        self.postgrado = postgrado
