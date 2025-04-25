##Trabajo realizado por Juan Luis Etchart
##Implementación de la clase UnidadCurricular

class UnidadCurricular():
    
    def __init__(self, nombre:str, codigo:str, previas:list ,creditos:int , instExamen:int = None):
        """
        Creación de la Unidad Curricular (UC).
        -
        Para crear la esta unidad curricular debe ingresar la siguiente información:
        - Nombre de la UC;
        - Código de la UC;
            - Formato: SxUCx (dónde las "x" son el número correspondiente)
        - Una lista con los códigos de las UCs previas;
        - Creditos que aportan al aprobar ésta UC;
        - Cantidad de las instancias a examen que habilita esta UC;
        """
        self.nombreUC = nombre
        self.codigoUC = codigo.upper()
        self.previasUC = previas
        self.creditosUC = creditos
        self.instanciaExamenUC = instExamen

    def semestre(self):
            return int(self.codigoUC[1])

    def __str__(self):
        return f"{self.nombreUC}"