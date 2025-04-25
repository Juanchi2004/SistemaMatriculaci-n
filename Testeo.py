import SistemaDeMatriculacion as SdM
from UC import *
from PlanDeEstudio import *
# ibio2026 = PdE()
# matAvanzada = Uc()

juanchi = SdM.Estudiante("juan", "etchart", 54852194, 2022)
secretaria = SdM.Secretaria()

plan = IBIO2026(ruta="C:/Users/juanc/OneDrive/Desktop/UTEC/7°moSemestre/ProgramacionAvanzada/Sistema dematriculaciones paraIngeniería Biomédica v2.0/datos.json")

# print(juanchi.getCi())

secretaria.matricularUC(juanchi, plan, "S1UC1", "S1UC2", "S2UC1")

# print(juanchi.getUC())

# secretaria.desmatricularUC(juanchi, "S1UC1")

# print(juanchi.getUC())


# print(juanchi.getUC())
# print((plan.semestresUC()))

# juanchi.matricularUC(plan, "S1UC1", "S1UC2", "S2UC1")
# print(juanchi.getUC())
# juanchi.inscripcionExamen("S1UC1", "S1UC2")
# print(juanchi.getUC())

# codigoUC="S1UC1"
# ruta = codigoUC+"-ExamenUC.txt"

# with open(ruta, "a") as file:
#     file.write("hola como estas \n")
#     file.write("45665432112\n")