#ejemplo de clases en python


class Persona:
    #se usan doble _ antes y despues de init para definir los parametros de la clase, es parte de la sintaxis
    #self se usa siempre, para hacer referencia a las propiedades de la clase.  
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad 

    def saludar(self): 
        #opcion 1 para imprimir
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

        #opcion 2 para imprimir
        print("Hola, soy ", self.nombre, " y tengo ", self.edad, "años")

#crear un objeto persona
persona1 = Persona("Duran", 79)
persona1.saludar()

persona2 = Persona("Jader", 21)
persona2.saludar()

class Estudiante(Persona): 
    def __init__(self, nombre, edad, grado): 
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self): 
        print(f"{self.nombre} esta eestudiando el grado {self.grado}.")

estudiante1 = Estudiante("Gabriela", 29, "Maestria")
estudiante1.saludar()
estudiante1.estudiar()
