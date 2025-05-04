import SistemaDeMatriculacion as SdM
from UC import *
from PlanDeEstudio import *
# ibio2026 = PdE()
# matAvanzada = Uc()

plan = IBIO2026(ruta="Sistema dematriculaciones paraIngeniería Biomédica v2.0/datos.json", codigoPlan="IBIO2026")

juanchi = SdM.Estudiante("juan", "etchart", 54852194, 2022, plan)
# josecito = SdM.Estudiante("gabo", "ferrer", 12345678, 2020, plan)
# anita = SdM.Estudiante("Anna", "Caballero", 65487917, 2022, plan)
# morocho = SdM.Estudiante("Ignacio", "Rivero", 54887917, 2022, plan)

secretaria = SdM.Secretaria("Jessica", "Arocena")


secretaria.matricularUC(juanchi, plan, "S1UC1","S1UC2")

# secretaria.desmatricularUC(juanchi, "S1UC2")
# secretaria.inscripcionExamen(juanchi, "S1UC1")
# secretaria.desinscripcionExamen(juanchi, "S1UC1")
# # secretaria.matricularUC(josecito, plan, "S1UC1")
# # secretaria.matricularUC(anita, plan, "S1UC1")
# # secretaria.matricularUC(morocho, plan, "S1UC1", "S1UC2")

# secretaria.desmatricularUC(josecito, "S1UC1")

SdM.SistemaDeMatriculacion._editarUC_escolaridad(juanchi)
