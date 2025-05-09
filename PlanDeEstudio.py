##Trabajo realizado por Juan Etchart - Gabriel Ferrer.
##Módulos 4, 5 y 6

import json
from UC import UnidadCurricular as UC
class Plan_De_Estudio():
    """
        Creación del plan de estudio.
        -
        Para crear el plan de estudio debe de ingresar la siguiente información:
        - La ruta de acceso al archivo donde se encuentra el plan de estudio.
        - El codigo del plan el correspondiente
        """

    def __init__(self, ruta, codigoPlan:str):
        
        self.ruta = ruta
        self.unidades_curriculares = self.__cargarPlan()
        self.codigoPlan = codigoPlan
        
    
    def __cargarPlan(self):

        dictUC = {}
        with open(self.ruta, "r") as file:
            # print(json.load(file))  
            # try:
                
                for ucCode, ucComponentes in json.load(file).items():

                    # if not "nombre" | "code" | "ucPrevias"| "creditos" in ucComponentes.keys():
                    #     raise algunError("Error dentro del archivo json") 
                    
                    dictUC[ucCode] = UC(nombre=ucComponentes["nombre"],
                                        codigo=ucComponentes["code"],
                                        previas=ucComponentes["ucPrevias"],
                                        creditos=ucComponentes["creditos"])
            # except:
            #     #IMPLEMENTAR ERROR PARA QUE FRENE LA EJECUCIÓN
            #     print("Error al cargar las unidades curriculares, favor revisar el archivo en la ruta: \n", self.ruta)
            #     return None
            # else:    
                return dictUC

    
    def getUC(self):
        """
        Retorna una lista de listas que contiene los codigos de las UCs y los nombres asociados.
        - 
        [ 
        [codigoUC, nombreUC],
        [...], 
        .
        .
        .
        ]
        """
        return  [[codigoUC, self.unidades_curriculares[codigoUC].nombreUC] for codigoUC in self.unidades_curriculares.keys()]
    
    def semestresUC(self, semestre:int = None):

        if semestre == None:
            return self.getUC()
        else:
            return [[codigoUC, self.unidades_curriculares[codigoUC].nombreUC] for codigoUC in self.unidades_curriculares.keys() if int(codigoUC[1]) == semestre]
        
    def nombreUC(self, *codigosTupla:str):
        """
        Retorna una lista con los nombres de las UCs correspondiente a los codigos
        """

        return [self.unidades_curriculares[codigo].nombreUC for codigo in codigosTupla]
