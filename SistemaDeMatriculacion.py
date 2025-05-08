##Trabajo realizado por Juan Etchart.
##Módulos 4, 5 y 6

from PlanDeEstudio import Plan_De_Estudio
import json
        

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
    def __init__(self, nombre:str, apellido:str, CI:int, ingreso:int, plan:Plan_De_Estudio):
        
        
        self.nombre = nombre
        self.apellido = apellido
        self._ci = CI 
        self._ingreso = ingreso
        self.codigoPlan = plan.codigoPlan
        
        
        expediente = SistemaDeMatriculacion._cargar_escolaridad(self)

        self.uc =  expediente[str(self._ci)]["UC"]
        self.creditos = expediente[str(self._ci)]["creditos"]
                    #diccionario donde la key corresponde al codigo de la uc el valor corresponde al estado de la uc
                    #Donde: "Examen" UC en examen, "Cursando" UC en curso, "Aprobado" UC aprobada.
        
    
    
    def getCi(self) -> str:
        """
        Retorna la cédula de identidad del estudiante
        """
        return f"{self._ci}"
    
    def getUC(self, estado:bool = True) -> dict | tuple:
        """
        Cuando se llama a este método sin modificar el estado (True) retorna el diccionario de las unidades curriculares junto a sus estados.
        - "Cursando"
        - "Examen"
        - "Aprobado"
        
        Si el estado es modificado (False) se retorna unicamente una tupla con los codigos de las unidades curriculares.
        """
        if estado == False:
            return (codigos for codigos in self.uc.keys())
        else:
            return self.uc
    
    def matricularUC(self, planEstudio: Plan_De_Estudio, *ucMatriculada:str):
        """
        Matricula al estudiante en las unidades curriculares que desea
        -
        Datos solicitados:
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a cursar.
            - Si este archivo no existe lo crea.
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.matricularUC(self, planEstudio, ucMatriculada)
    
    def inscripcionExamen(self, *ucExamen:str):
        """
        Inscribe al estudiante al examen de la unidad curricular que desea.
        -
        Datos solicitados:
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a rendir examen.
            - Si este archivo no existe lo crea.
        - Quita al estudiante del archivo .csv al cual se agrega cuando este está cursando la unidad curricular.
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.inscripcionExamen(self, ucExamen)


    


class Secretaria():
    """
    Creación del usuario de Secretaría.
    -
    Para crear el usuario deberá ingresar:
    - Nombre de la persona.
    - Apellido de la persona.
    """
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        pass

    def apruebaUC(self, estudiante:Estudiante, plan:Plan_De_Estudio ,*ucaprobada:str):
        """
        Aprueba la unidad curricular del estudiante.
        -
        Este método solicita:
        - El Estudiante a aprobar la materia.
        - El plan de estudio al cual pertenece el estudiante.
        - El o los codigos de las unidades curriculares a aprobar.
        -------
        - Esta acción es posible si la unidad curricular del estudiante se encuentra en estado "Cursando".
        - Actualiza la escolaridad del estudiante automaticamente
        """
        return SistemaDeMatriculacion.apruebaUC(estudiante, plan, ucaprobada)

        #Eliminar estudiante del txt "codigoUC-CursandoUC.csv"
        #IMPLEMENTARLO BIEN
    
    def matricularUC(self, estudiante:Estudiante, planEstudio: Plan_De_Estudio, *ucMatriculada:str):
        """
        Matricula al estudiante en las unidades curriculares que desea
        -
        Datos solicitados:
        - Estudiante a matricular
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a cursar.
            - Si este archivo no existe lo crea.
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.matricularUC(estudiante, planEstudio, ucMatriculada)

    def desmatricularUC(self, estudiante:Estudiante, *ucDesmatriculada:str):
        """
        Desmatricula al estudiante de una unidad curricular a la cual está matriculado.
        -
        Datos solicitados:
        - Estudiante a desmatricular.
        - El o los codigos de las unidades curriculares correspondientes.
        ----
        El método tambien realiza las siguientes acciones:
        - Elimina al estudiante del archivo .csv correspondiente al la unidad curricular
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.desmatricularUC(estudiante, ucDesmatriculada)

    def inscripcionExamen(self, estudiante: Estudiante, *ucExamen:str):
        """
        Inscribe al estudiante al examen de la unidad curricular que se desea.
        -
        Datos solicitados:
        - El estudiante a inscribir a examen.
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a rendir examen.
            - Si este archivo no existe lo crea.
        - Quita al estudiante del archivo .csv al cual se agrega cuando este está cursando la unidad curricular.
        - Actualiza la escolaridad del estudiante.
        """

        return SistemaDeMatriculacion.inscripcionExamen(estudiante, ucExamen)
    
    def desinscripcionExamen(self, estudiante: Estudiante, *ucQuitar:str):
        """
        Desinscribe al estudiante del examen de la unidad curricular que se desea.
        -
        Datos solicitados:
        - El estudiante a desinscribir al examen.
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Quita al estudiante del archivo .csv al cual se agrega cuando este se inscribe a un examen.
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.desinscripcionExamen(estudiante, ucQuitar)

    def apruebaExamen(self, estudiante: Estudiante, plan:Plan_De_Estudio ,*coduigoExamen:str):
        """
        Aprueba el examen de la unidad curricular rendido por el estudiante.
        -
        Este método solicita:
        - El Estudiante a aprobar el examen.
        - El plan de estudio al cual pertenece el estudiante.
        - El o los codigos de las unidades curriculares a aprobar.
        -------
        - Esta acción es posible si la unidad curricular del estudiante se encuentra en estado "Examen".
        - Actualiza la escolaridad del estudiante automaticamente
        """
        return SistemaDeMatriculacion.apreubaExamenUC(estudiante, plan, coduigoExamen)

    def getCursandoUC(self, codigoUC:str) -> list:
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran cursando la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        return SistemaDeMatriculacion.getCursandoUC(codigoUC)
    
    def getExamenUC(self, codigoUC:str) -> list:
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran en examen de la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        return SistemaDeMatriculacion.getExamenUC(codigoUC)        

class Coordinador():
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
   
    def matricularUC(self, estudiante:Estudiante, planEstudio: Plan_De_Estudio, *ucMatriculada:str):
        """
        Matricula al estudiante en las unidades curriculares que desea
        -
        Datos solicitados:
        - Estudiante a matricular
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a cursar.
            - Si este archivo no existe lo crea.
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.matricularUC(estudiante, planEstudio, ucMatriculada)

    def desmatricularUC(self, estudiante:Estudiante, *ucDesmatriculada:str):
        """
        Desmatricula al estudiante de una unidad curricular a la cual está matriculado.
        -
        Datos solicitados:
        - Estudiante a desmatricular.
        - El o los codigos de las unidades curriculares correspondientes.
        ----
        El método tambien realiza las siguientes acciones:
        - Elimina al estudiante del archivo .csv correspondiente al la unidad curricular
        - Actualiza la escolaridad del estudiante.
        """
        return SistemaDeMatriculacion.desmatricularUC(estudiante, ucDesmatriculada)

    def getCursandoUC(self, codigoUC:str):
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran cursando la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        return SistemaDeMatriculacion.getCursandoUC(codigoUC)
    
    def getExamenUC(self, codigoUC:str):
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran en examen de la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        return SistemaDeMatriculacion.getExamenUC(codigoUC)        

    
class SistemaDeMatriculacion():
    def __init__(self, plan:Plan_De_Estudio):
        self.planEstudio = plan
        pass


    @classmethod
    def matricularUC(cls, estudiante:Estudiante, planEstudio: Plan_De_Estudio, ucMatriculada:tuple):
        """
        Matricula al estudiante en las unidades curriculares que desea
        -
        Datos solicitados:
        - Estudiante a matricular
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a cursar.
            - Si este archivo no existe lo crea.
        - Actualiza la escolaridad del estudiante.
        """
        for codigoUC in ucMatriculada:

            listaPrevias = planEstudio.unidades_curriculares[codigoUC].previasUC
            sinPrevias = True

            if listaPrevias == None:
                estudiante.uc[codigoUC] = "Cursando"
                SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC)
                SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                #escriba en el csv correspondiente a la UC y al estudiante
                continue

            for codigoPrevia in listaPrevias: #Verificacion de la las previas (podria hacerse en una funcion _Validar uc)

                try:
                    if estudiante.uc[codigoPrevia] == "Aprobado":
                        continue
                    else:
                        nombreUC, nombrePrevia = planEstudio.nombreUC(codigoUC,codigoPrevia)
                        print(f"la UC {codigoUC,nombreUC} tiene como previa {codigoPrevia,nombrePrevia}")
                        print(f"ó {codigoPrevia, nombrePrevia} está en {estudiante.uc[codigoPrevia]}")
                        sinPrevias = False
                        break #Se devería arrojar un error aqui para justamente cortar el avance del programa.
                except:
                    print(f"No se encontró {codigoPrevia} en el estudiante")
                    sinPrevias = False
                    break
            if sinPrevias:        
                estudiante.uc[codigoUC] = "Cursando"
                SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC)
                SistemaDeMatriculacion._editarUC_escolaridad(estudiante)

            else:
                return False    
        return True

    @classmethod
    def desmatricularUC(cls, estudiante:Estudiante, ucDesmatriculada:tuple):
        """
        Desmatricula al estudiante de una unidad curricular a la cual está matriculado.
        -
        Datos solicitados:
        - Estudiante a desmatricular.
        - El o los codigos de las unidades curriculares correspondientes.
        ----
        El método tambien realiza las siguientes acciones:
        - Elimina al estudiante del archivo .csv correspondiente al la unidad curricular
        - Actualiza la escolaridad del estudiante.
        """

        for codigoUC in ucDesmatriculada:

            try:
                if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] == "Cursando":

                    del estudiante.uc[codigoUC]
                    SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC, borrar=True)
                    SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                    #Eliminar al estudiante del txt "codigoUC-cursandoUC-nombreUC.txt"
                else:
                    print(f"La UC {codigoUC} no se encuentra matriculada al estudiante")
                    return False
                #IMPLEMENTAR ERROR
            except:
                    print(f"No se encontró {codigoUC} en el estudiante")
                    break
        return True

    @classmethod
    def apruebaUC(cls, estudiante:Estudiante, plan:Plan_De_Estudio ,ucAprobada:tuple):
        """
        Aprueba la unidad curricular del estudiante.
        -
        Este método solicita:
        - El Estudiante a aprobar la materia.
        - El plan de estudio al cual pertenece el estudiante.
        - El o los codigos de las unidades curriculares a aprobar.
        -------
        - Esta acción es posible si la unidad curricular del estudiante se encuentra en estado "Cursando".
        - Actualiza la escolaridad del estudiante automaticamente
        """

        for codigoUC in ucAprobada:
            try:
                if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] == "Cursando":
                    estudiante.uc[codigoUC] = "Aprobado"
                    estudiante.creditos += plan.unidades_curriculares[codigoUC].creditosUC
                    SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                    SistemaDeMatriculacion._csvCursandoUC(estudiante, codigoUC, borrar=True)
                else:
                    print(f"La UC {codigoUC} no fue cursada o en su defecto ya está aprobada")
            except:
                    print(f"No se encontró {codigoUC} en el estudiante")
                    break
        #IMPLEMENTARLO BIEN

    @classmethod
    def inscripcionExamen(cls, estudiante: Estudiante, ucExamen:tuple):
        """
        Inscribe al estudiante al examen de la unidad curricular que se desea.
        -
        Datos solicitados:
        - El estudiante a inscribir a examen.
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Agrega al archivo .csv correspondiente a la unidad curricular a rendir examen.
            - Si este archivo no existe lo crea.
        - Quita al estudiante del archivo .csv al cual se agrega cuando este está cursando la unidad curricular.
        - Actualiza la escolaridad del estudiante.
        """

        for codigoUC in ucExamen:        
            try:
                if codigoUC in estudiante.getUC(estado = False) and estudiante.uc[codigoUC] != "Aprobado":
                    estudiante.uc[codigoUC] = "Examen"
                    SistemaDeMatriculacion._csvExamenUC(estudiante=estudiante, ucCode=codigoUC)
                    SistemaDeMatriculacion._csvCursandoUC(estudiante=estudiante, ucCode=codigoUC, borrar=True)
                    SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                    #Adaptarlo al csv
                else:
                    print(f"La UC {codigoUC} no se encuentra dentro de su lista de ucs o ya se encuentra aprobada")
            except:
                    print(f"No se encontró {codigoUC} en el estudiante")
                    break
        pass
    
    @classmethod
    def desinscripcionExamen(cls, estudiante: Estudiante, ucQuitar:tuple):
        """
        Desinscribe al estudiante del examen de la unidad curricular que se desea.
        -
        Datos solicitados:
        - El estudiante a desinscribir al examen.
        - Plan de estudio al cual corresponde el estudiante.
        - El o los codigos de las unidades curriculares
        --------
        El método también realiza las siguientes acciones:
        - Quita al estudiante del archivo .csv al cual se agrega cuando este se inscribe a un examen.
        - Actualiza la escolaridad del estudiante.
        """

        for codigoUC in ucQuitar:
            try:
                if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] == "Examen":

                    estudiante.uc[codigoUC] = "Cursando"
                    SistemaDeMatriculacion._csvExamenUC(estudiante, codigoUC, borrar = True)
                    SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                
                else:
                    print(f"La UC {codigoUC} no se encuentra en examen o no está dentro de las UCs cursadas por el estudiante")
                    return False
                #Implementar aviso(?)
            except:
                    print(f"No se encontró {codigoUC} en el estudiante")
                    break

        return True

    @classmethod
    def apreubaExamenUC(cls, estudiante: Estudiante, plan:Plan_De_Estudio ,ucQuitar:tuple):
        """
        Aprueba el examen de la unidad curricular rendido por el estudiante.
        -
        Este método solicita:
        - El Estudiante a aprobar el examen.
        - El plan de estudio al cual pertenece el estudiante.
        - El o los codigos de las unidades curriculares a aprobar.
        -------
        - Esta acción es posible si la unidad curricular del estudiante se encuentra en estado "Examen".
        - Actualiza la escolaridad del estudiante automaticamente
        """
        for codigoUC in ucQuitar:
            try:
                if codigoUC in estudiante.getUC(estado=False) and estudiante.uc[codigoUC] == "Examen":
                    estudiante.uc[codigoUC] = "Aprobado"
                    estudiante.creditos += plan.unidades_curriculares[codigoUC].creditosUC
                    SistemaDeMatriculacion._editarUC_escolaridad(estudiante)
                    SistemaDeMatriculacion._csvExamenUC(estudiante, codigoUC, borrar=True)
                else:
                    print(f"La UC {codigoUC} no fue cursada o en su defecto ya se encuentra aprobada")
            except:
                print(f"No se encontró {codigoUC} en el estudiante")
                break
        
        pass

    @classmethod
    def getCursandoUC(cls, codigoUC:str)->list:
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran cursando la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        
        try:
            from csv import reader
            ruta = codigoUC + "-CursandoUC.csv"
            with open(ruta, "r") as file:
                file = list(reader(file,delimiter=","))
            return file
        except:
                print(f"No se encontró {codigoUC} en el estudiante")
                pass
    
    @classmethod
    def getExamenUC(cls, codigoUC:str) -> list:
        """
        Retorna una lista de listas con los estudiantes los cuales se encuentran en examen de la unidad curricular.
        -
        Este método solicita:
        - Codigo de la unidad curricular.

        La lista de listas tiene la siguiente estructura:
        - Cada fila corresponde a un estudiante
        - Columnas.
            - La columna cero corresponde a las cédulas de identidad de los estudiantes.
            - La columna uno corresponde a los nombres de los estudiantes.
            - La columna dos corresponde a los apellidos de los estudiantes.
        """
        
        try:
            from csv import reader
            ruta = codigoUC + "-ExamenUC.csv"
            with open(ruta, "r") as file:
                file = list(reader(file,delimiter=","))
            return file
        except:
                print(f"No se encontró {codigoUC} en el estudiante")
                pass        

    @classmethod
    def _csvCursandoUC(cls, estudiante: Estudiante, ucCode:str, borrar:bool = False):
        """
        Este método crea y/o modifica el contenido del archivo .csv correspondiente a la uc en curso.
        -
        Datos solicitados:
        - Estudiante al cual se desea agregar o quitar del archivo.
        - Codigo de la unidad curricular para acceder al archivo.
        - *borrar*:
            - *True* - Si se desea borrar el estudiante del registro.
            - *False* - Si se desea agregar el estudiante al registro.
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
                print(f"CI:({estudiante.getCi()}).No se pudo realizar la acción sobre el CSV-cursandoUC de la UC {ucCode}")
        
        #Demasiado engorrozo pero funciona (por lo menos hasta ahora je)

    @classmethod
    def _csvExamenUC(cls, estudiante: Estudiante, ucCode:str, borrar:bool = False):
        """
        Este método crea y/o modifica el contenido del archivo .csv correspondiente a la uc en examen.
        -
        Datos solicitados:
        - Estudiante al cual se desea agregar o quitar del archivo.
        - Codigo de la unidad curricular para acceder al archivo.
        - *borrar*:
            - *True* - Si se desea borrar el estudiante del registro.
            - *False* - Si se desea agregar el estudiante al registro.
        """
        import csv
        ruta = ucCode + "-ExamenUC.csv"
        
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
                print(f"CI:({estudiante.getCi()}).No se pudo realizar la acción sobre el CSV-examen de la UC {ucCode}")
        
        #Demasiado engorrozo pero funciona (por lo menos hasta ahora je)

    @classmethod
    def _cargar_escolaridad(cls, estudiante: Estudiante) -> dict:
        """
        Crea el archivo *.json* donde se alojará la información del estudiante.
        -
        Este método solicita:
        - Un objeto estudiante.
        ----
        ----
        Estructura de la escolaridad:
        - *Cédula de identidad*:{
            -    "nombre": *Nombre del estudiante*,
            -    "apellido": *Apellido del estudiante*,
            -    "año_ingreso": *Año de ingreso del estudiante*,
            -    "plan": *Codigo del plan de estudio al cual pertenece*,
            -    "creditos": *Acumulación de creditos*,
            -    "UC":{} *Diccionario con los codigos de las UCs y sus estados*
            }

        """

        ruta = estudiante.getCi()+"-ESCOLARIDAD-"+estudiante.nombre[0]+"-"+estudiante.apellido+".json"

        escolaridad = {
            estudiante.getCi():{
                "nombre": estudiante.nombre,
                "apellido": estudiante.apellido,
                "año_ingreso": estudiante._ingreso,
                "plan": estudiante.codigoPlan,
                "creditos": 0,
                "UC":{}
            }
        }

        with open(ruta, mode= "a+") as file:
            file.seek(0) #colocando el cursor en el origen del archivo

            try:
                datos = json.load(file)
            except:
                file.seek(0)
                json.dump(escolaridad, file, indent=4)
                
                file.flush()
                file.seek(0)
                
                datos = json.load(file)
            
            return datos            
            
    @classmethod
    def _editarUC_escolaridad(cls, estudiante:Estudiante):
        """
        Edita el archivo de la escolaridad del estudiante.
        """
        ruta = estudiante.getCi()+"-ESCOLARIDAD-"+estudiante.nombre[0]+"-"+estudiante.apellido+".json"

        try:
            with open(ruta, "r+") as file:
                fileLoad = json.load(file)
                fileLoad[estudiante.getCi()]["UC"] = estudiante.getUC()
                fileLoad[estudiante.getCi()]["creditos"] = estudiante.creditos
                file.seek(0) #coloco el cursor en el punto cero
                
                json.dump(fileLoad, file, indent=4)  
                file.truncate()
                file.seek(0)
                
                # fileLoad = json.load(file)
        except:
            print(f"Algo inesperado ha ocurrido al editar el expediente:{ruta}")
        pass
