
"""
Ejercicio: Combate con Habilidades
==================================

Restricciones:
    - No usar isinstance()
    - No modificar la clase base
    - No acceder directamente a _vida desde afuera

Objetivo:
Crear dos tipos de personajes con habilidades especiales.

Personaje 1: Guerrero
    - Ataque fijo de 10 puntos
    - 20% de probabilidad de hacer ataque crítico (daño doble)

Personaje 2: Sacerdote
    - Ataque débil de 5 a 8 puntos
    - 30% de probabilidad de curarse entre 4 y 10 puntos antes de atacar

Completar el main para simular el combate.
"""

from abc import ABC, abstractmethod
import random


# ==============================
# CLASE BASE (NO MODIFICAR)
# ==============================

class Personaje(ABC):

    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    def recibir_danio(self, cantidad):
        self._vida -= cantidad
        if self._vida < 0:
            self._vida = 0

    def curar(self, cantidad):
        self._vida += cantidad

    def esta_vivo(self):
        return self._vida > 0

    def mostrar(self):
        print(f"{self._nombre} (vida: {self._vida})")

    @abstractmethod
    def atacar(self, objetivo):
        pass


# ==============================
# CLASES HIJAS
# ==============================

# Clase Guerrero
class Guerrero(Personaje): 
    ataque = 10
    
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
    
    def atacar(self, objetivo):
        golpe_critico = random.random() <= 0.2
        if golpe_critico:
            objetivo.recibir_danio(self.ataque * 2)
        else:
            objetivo.recibir_danio(self.ataque)

#Clase Sacerdote
class Sacerdote(Personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)

    def atacar(self, objetivo):
        ataque = random.randint(5, 8)
        curarse = random.random() <= 0.3
        if curarse:
            cantidad_curar = random.randint(4, 10)
            self.curar(cantidad_curar)
        objetivo.recibir_danio(ataque)

# ==============================
# MAIN
# ==============================

def main():

    guerrero = Guerrero("Guerrero", 50)
    sacerdote = Sacerdote("Sacerdote", 50)

    while guerrero.esta_vivo() and sacerdote.esta_vivo():

        guerrero.atacar(sacerdote)
        sacerdote.mostrar()

        if sacerdote.esta_vivo():

            sacerdote.atacar(guerrero)
            guerrero.mostrar()

        print("-" * 20)

    print("Combate terminado")

    if guerrero.esta_vivo():
        print(f"Ganó {guerrero._nombre}")
    else:
        print(f"Ganó {sacerdote._nombre}")


if __name__ == "__main__":
    main()
