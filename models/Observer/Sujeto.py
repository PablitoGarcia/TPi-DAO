class Sujeto: 
    def __init__(self): 
        self._suscriptores = [] 

    def suscribir(self, suscriptor): 
        self._suscriptores.append(suscriptor) 

    def desuscribir(self, suscriptor): 
        self._suscriptores.remove(suscriptor) 

    def notificar(self): 
        for suscriptor in self._suscriptores: 
            suscriptor.refrescar()