##Trabajo realizado por Juan Etchart.
##Módulos 4, 5 y 6

from PlanDeEstudio import IBIO2026
from UC import UnidadCurricular as UC

# class Persona():
#     def __init__(self, nombre:str, apellido:str):
        
#         self.nombre = nombre
#         self.apellido = apellido
        
        



class Estudiante():
    """
        Creación del usuario estudiante.
        -
        Para cerar el usuario debe ingresar:
        - Nombre del estudiante;
        - Apellido del estudiante;
        - Cédula de identidad del estudiante;
            - Sin espacios ni guiónes.
            - Una vez creado el usuario no podrá cambiar este parámetro
        - Año de ingreso del estudiante.
            - Una vez creado el usuario no podrá cambiar este parámetro
        """
    def __init__(self, nombre:str, apellido:str, CI:int, ingreso:int):
        

        self.nombre = nombre
        self.apellido = apellido
        self._ci = CI 
        self._ingreso = ingreso
        self.uc = {} #diccionario donde la key corresponde al codigo de la uc el valor corresponde al estado de la uc
                      #Donde: "Examen" UC en examen, "Cursando" UC en curso, "Aprobada" UC aprobada.
        
    
    
    def getCi(self):
        return f"{self._ci}"
    
    def getUC(self, estado:bool = True):
        
        if estado == False:
            return (codigos for codigos in self.uc.keys())
        else:
            return self.uc
    
    def matricularUC(self, planEstudio: IBIO2026, *ucMatriculada:str):
        """
        Documentar
        -
        """

        
        # listaUcPlan = planEstudio.unidades_curriculares.keys()
        # if ucMatriculada in listaUcPlan:

        for codigoUC in ucMatriculada:

                sinPrevias = True
                listaPrevias = planEstudio.unidades_curriculares[codigoUC].previasUC
                
                if  listaPrevias == None:
                    self.uc[codigoUC] = "Cursando"
                    continue

                for codigoPrevia in listaPrevias:

                    if self.uc[codigoPrevia] == "Aprobada":
                        print("hasta aqui bien, la previa se encuentra aprobada")
                        continue #debería de continuar con el siguiente codigo de la lista de previas
                    else:
                        nombreUC, nombrePrevia = planEstudio.nombreUC(codigoUC,codigoPrevia)
                        print(f"la UC {codigoUC,nombreUC} tiene como previa {codigoPrevia,nombrePrevia}")
                        print(f"ó {codigoPrevia, nombrePrevia} está en {self.uc[codigoPrevia]}")
                        sinPrevias = False
                        break  

                if sinPrevias:        
                    self.uc[codigoUC] = "Cursando"
                else:
                    print("IMPLEMENTAR UN ERROR QUE NO PERMITA MATRICULAR")
                # self.uc[codigoUC] = "Aprobada"
        
        # else:
        #     print("las unidades curriculares no se encuentran dentro del plan de estudio")
        #Agregar estudiante al txt "codigoUC-cursandoUC.txt"
        pass
    
    def inscripcionExamen(self, *ucExamen:str):
        """
        Inscripción a examen
        -
        """

        for codigoUC in ucExamen:        
            if codigoUC in self.getUC(estado = False) and self.uc[codigoUC] != "Aprobada":
                self.uc[codigoUC] = "Examen"
                #Agregar estudiante al txt "codigoUC-examenUC.txt"
            else:
                print("La uc no se encuentra dentro de su lista de ucs o ya se encuentra aprobada")
            
        
        pass


    


class Secretaria():
    def __init__(self):
        pass

    def modificacionCI(self, estudiante:Estudiante, nuevaCI:int):
        estudiante._ci = nuevaCI

    def apruebaUC(self, estudiante:Estudiante, *ucaprobada:str):
        """
        ucaprobadas contiene los codigos de las ucs correspondientes al plan de estudio.
        """
        for codigoUC in ucaprobada:
            if codigoUC in estudiante.getUC(estado=False):
                estudiante.uc[codigoUC] = "Aprobado"
            else:
                print(f"la UC {codigoUC} no fue cursada")

        #Eliminar estudiante del txt "codigoUC-cursandoUC.txt"
    
    def matricularUC(self, estudiante:Estudiante, planEstudio: IBIO2026, *ucMatriculada:str):
        """
        DOCUMENTAR
        -
        """
        for codigoUC in ucMatriculada:

            listaPrevias = planEstudio.unidades_curriculares[codigoUC].previasUC
            sinPrevias = True

            if listaPrevias == None:
                estudiante.uc[codigoUC] = "Cursando"
                self._txtCursandoUC(estudiante=estudiante, ucCode=codigoUC)
                #escriba en el txt correspondiente a la UC y al estudiante
                continue

            for codigoPrevia in listaPrevias:

                if estudiante.uc[codigoPrevia] == "Aprobada":
                    print("hasta aqui bien, previa aprobada")
                    continue
                else:
                    nombreUC, nombrePrevia = planEstudio.nombreUC(codigoUC,codigoPrevia)
                    print(f"la UC {codigoUC,nombreUC} tiene como previa {codigoPrevia,nombrePrevia}")
                    print(f"ó {codigoPrevia, nombrePrevia} está en {estudiante.uc[codigoPrevia]}")
                    sinPrevias = False
                    break
            
            if sinPrevias:        
                estudiante.uc[codigoUC] = "Cursando"
            else:
                print("IMPLEMENTAR UN ERROR QUE NO PERMITA MATRICULAR")    
        #Agregar estudiante al txt "codigoUC-cursandoUC.txt"
        pass

    def desmatricularUC(self, estudiante:Estudiante, *ucDesmatriculada:str):
        """
        DOCUMENTAR:
        -
        """

        for codigoUC in ucDesmatriculada:

            if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] != "Aprobado":

                estudiante.uc.pop(codigoUC)
                #Eliminar al estudiante del txt "codigoUC-cursandoUC-nombreUC.txt"
            else:
                print(f"La UC {codigoUC} no se encuentra matriculada al estudiante")
                #IMPLEMENTAR ERROR
        pass

    def inscripcionExamen(self, estudiante: Estudiante, *ucExamen:str):
        """
        DOCUMENTAR:
        -
        """

        for codigoUC in ucExamen:        
            if codigoUC in estudiante.getUC(estado = False) and estudiante.uc[codigoUC] != "Aprobada":
                estudiante.uc[codigoUC] = "Examen"
                #Agregar estudiante al txt "codigoUC-examenUC.txt"
            else:
                print("La UC no se encuentra dentro de su lista de ucs o ya se encuentra aprobada")

        pass
    
    def desinscripcionExamen(self, estudiante: Estudiante, *ucQuitar:str):
        """
        DOCUMENTAR:
        -
        """

        for codigoUC in ucQuitar:

            if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] == "Examen":

                estudiante.uc[codigoUC] = "Cursando"
                #Quitar estudiante del txt "codigoUC-examenUC.txt" 
            
            else:
                print(f"La UC {codigoUC} no se encuentra en examen o no está dentro de las UCs cursadas por el estudiante")
                #Implementar aviso(?)

    def _txtCursandoUC(self, estudiante: Estudiante, ucCode:str, estado:bool = True):
        """
        DOCUMENTAR:
        -
        """

        ruta = ucCode + "-CursandoUC.txt"

        with open(ruta, "r") as file:
            file = file.readlines()
            if not estudiante.getCi() in file:
                exit
        
        with open(ruta, "+a") as file:
            print(file.readlines())
            if not estudiante.getCi() in file.readlines():
                file.write( estudiante.getCi() + "," + estudiante.nombre + "," + estudiante.apellido + "\n")
            else: 
                print(f"El estudiante ya se enceuntra cursando la UC {ucCode}")


        pass

    # def asignePlanDeEstudio(self, estudiante:Estudiante, planEstudio:PdE):
    #     """
    #     La secretaria puede asignar el plan de estudio.
    #     """

class Coordinador():
    def __init__(self):
        pass

