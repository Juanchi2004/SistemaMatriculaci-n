##Trabajo realizado por Juan Etchart.
##Módulos 4, 5 y 6

from PlanDeEstudio import IBIO2026
from UC import UnidadCurricular as UC

# class Persona():
#     def __init__(self, nombre:str, apellido:str):
        
#         self.nombre = nombre
#         self.apellido = apellido
        
class SuperPersona():
    #Herencia de parametros comunes dentro de los siguientes objetos, menos SDM (El ultimo)
    pass        



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
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
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
        SistemaDeMatriculacion.matricularUC(estudiante, planEstudio, ucMatriculada)

    def desmatricularUC(self, estudiante:Estudiante, *ucDesmatriculada:str):
        """
        DOCUMENTAR:
        -
        """

        for codigoUC in ucDesmatriculada:

            if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] != "Aprobado":

                estudiante.uc.pop(codigoUC)
                self._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC, borrar=True)
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
                self._txtExamenUC(estudiante=estudiante, ucCode=codigoUC)
                #Adaptarlo al csv
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

    def _csvCursandoUC(self, estudiante: Estudiante, ucCode:str, borrar:bool = False):
        """
        DOCUMENTAR:
        -
        """
        import csv
        ruta = ucCode + "-CursandoUC.csv"
        
        with open(ruta, "a", newline='') as file:
            escritor = csv.writer(file)
            
            
            with open(ruta, "r") as archivoLeido:
                #si el archivo está recien creado no tendrá contenido, por lo cual se se escribe el formato de los datos
                lectura_archivo = list(csv.reader(archivoLeido, delimiter=",")) #Crea una lista con el contenido dentro del csv
                if lectura_archivo == []:
                
                    escritor.writerow(["Ci","Nombre","Apellido"])
                    lectura_archivo = list(csv.reader(archivoLeido, delimiter=",")) #"actualiza" el estado del archivo leído(?)
                
            listasCi = [ci[0] for ci in lectura_archivo[1:]]# no se como hacer de otra forma esta cag*da, no me funciona el lectura_archivo[1:][0] para hacerlo todo en una sola linea

            if not estudiante.getCi() in listasCi and not borrar:

                escritor.writerow([estudiante.getCi(),estudiante.nombre,estudiante.apellido])
            elif estudiante.getCi() in listasCi and borrar:

                #Mi intención era con el indice aputnar a esa "fila" y borrarla directamente del csv pero no lo estoy pudiendo lograr.

                indice = listasCi.index(estudiante.getCi()) + 1
                with open(ruta, "w", newline="") as reemplazo:
                    del lectura_archivo[indice] 
                    csv.writer(reemplazo).writerows(lectura_archivo)
                    
                    # escritor.writerows(lectura_archivo)

            else: 
                print(f"El estudiante ya se enceuntra cursando la UC {ucCode}")
        
        #IMPLEMENTAR EL ESTADO=False PARA ELIMINAR EL ESTUDIANTE DEL CSV
        #Demasiado engorrozo pero funciona (por lo menos hasta ahora je)



class Coordinador():
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        
    
class SistemaDeMatriculacion():
    def __init__(self, plan:IBIO2026):
        self.planEstudio = plan
        pass


    @classmethod
    def matricularUC(cls, estudiante:Estudiante, planEstudio: IBIO2026, ucMatriculada:tuple):
        """
        DOCUMENTAR
        -
        """
        for codigoUC in ucMatriculada:

            listaPrevias = planEstudio.unidades_curriculares[codigoUC].previasUC
            sinPrevias = True

            if listaPrevias == None:
                estudiante.uc[codigoUC] = "Cursando"
                SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC)
                #escriba en el csv correspondiente a la UC y al estudiante
                continue

            for codigoPrevia in listaPrevias: #Verificacion de la las previas (podria hacerse en una funcion _Validar uc)

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
                SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC)

            else:
                print("IMPLEMENTAR UN ERROR QUE NO PERMITA MATRICULAR")    
        #Agregar estudiante al txt "codigoUC-cursandoUC.txt"
        pass

    
    @classmethod
    def _csvCursandoUC(self, estudiante: Estudiante, ucCode:str, borrar:bool = False):
        """
        DOCUMENTAR:
        -
        """
        import csv
        ruta = ucCode + "-CursandoUC.csv"
        
        with open(ruta, "a", newline='') as file:
            escritor = csv.writer(file)
            
            
            with open(ruta, "r") as archivoLeido:
                #si el archivo está recien creado no tendrá contenido, por lo cual se se escribe el formato de los datos
                lectura_archivo = list(csv.reader(archivoLeido, delimiter=",")) #Crea una lista con el contenido dentro del csv
                if lectura_archivo == []:
                
                    escritor.writerow(["Ci","Nombre","Apellido"])
                    lectura_archivo = list(csv.reader(archivoLeido, delimiter=",")) #"actualiza" el estado del archivo leído(?)
                
            listasCi = [ci[0] for ci in lectura_archivo[1:]]# no se como hacer de otra forma esta cag*da, no me funciona el lectura_archivo[1:][0] para hacerlo todo en una sola linea

            if not estudiante.getCi() in listasCi and not borrar:

                escritor.writerow([estudiante.getCi(),estudiante.nombre,estudiante.apellido])
            elif estudiante.getCi() in listasCi and borrar:

                #Mi intención era con el indice aputnar a esa "fila" y borrarla directamente del csv pero no lo estoy pudiendo lograr.

                indice = listasCi.index(estudiante.getCi()) + 1
                with open(ruta, "w", newline="") as reemplazo:
                    del lectura_archivo[indice] 
                    csv.writer(reemplazo).writerows(lectura_archivo)
                    
                    # escritor.writerows(lectura_archivo)

            else: 
                print(f"El estudiante ya se enceuntra cursando la UC {ucCode}")
        
        #IMPLEMENTAR EL ESTADO=False PARA ELIMINAR EL ESTUDIANTE DEL CSV
        #Demasiado engorrozo pero funciona (por lo menos hasta ahora je)

    def _csvExamenUC(self, estudiante: Estudiante, ucCode:str, estado:bool = True):
        """
        DOCUMENTAR:
        -
        """
        
        import csv
        ruta = ucCode + "-ExamenUC.csv"

        with open(ruta, "a", newline='') as file:
            escritor = csv.writer(file)
            
            with open(ruta, "r") as archivoLeido:
                lectura_archivo = list(csv.reader(archivoLeido, delimiter=",")) #Crea una lista con el contenido dentro del csv
                if lectura_archivo == []:
                    escritor.writerow(["Ci","Nombre","Apellido"])
                    lectura_archivo = list(csv.reader(archivoLeido, delimiter=","))
            
            listasCi = [ci[0] for ci in lectura_archivo[1:]]
            if not estudiante.getCi() in listasCi:
                escritor.writerow([estudiante.getCi(),estudiante.nombre,estudiante.apellido])
            else: 
                print(f"El estudiante ya se enceuntra en el examen de la UC {ucCode}")
        #IMPLEMENTAR EL ESTADO=False PARA ELIMINAR EL ESTUDIANTE DEL CSV