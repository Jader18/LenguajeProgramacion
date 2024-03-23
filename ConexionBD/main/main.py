import os
import sys
sys.path.append(r"C:\Users\Jader Mendoza\Desktop\3er año - 1er cuatrimestre\Lenguaje de programacion\Python\ConexionBD")
from dao import daoConnection
from models import clases as c


os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()




def insertarCiudad():
    name = input("Nombre de la ciudad: ")
    ciudad = c.City(name, 1)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.insert(ciudad)
    

def editarCiudad():
    oldId = int(input("ID de la ciudad a editar: "))
    newName = input("Nuevo Nombre: ")
    daoCity = daoConnection.DaoCity(conex)
    ciudad = c.City(newName, 1, oldId)
    daoCity.update(ciudad)


def mostarCiudad():
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)


def eliminarCiudad():
    id = int(input("ID de la ciudad a eliminar: "))
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(id)


def buscarCiudad():
    id = int(input("ID de la ciudad a buscar: "))
    daoCity = daoConnection.DaoCity(conex)
    cities = daoCity.get_by_id(id)
    print(cities)



def Menu():
    print("1. Igresar ciudad")
    print("2. Editar ciudad")
    print("3. Mostrar ciudad")
    print("4. Eliminar ciudad")
    print("5. Buscar ciudad")
    print("6. Salir")

def main():
    opcion = 0

    while(opcion != 6): 
        Menu()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            insertarCiudad()
            os.system("pause")

        elif(opcion == 2):
            editarCiudad()
            os.system("pause")

        elif(opcion == 3):
            mostarCiudad()
            os.system("pause")
        
        elif(opcion == 4):
            eliminarCiudad()
            os.system("pause")

        elif(opcion == 5):
            buscarCiudad()
            os.system("pause")

main()




#control + k + c -- comentar en bloque
#control + k + u -- quitar comentario en bloque

# se comenta para evitar insertar datos repetidos
# #instanciar modelo - City
# city1 = c.City("Managua", 1)
# city2 = c.City("León", 1)
# city3 = c.City("Granada", 1)
# city4 = c.City("Masaya", 1)
# city5 = c.City("Estelí", 1)
# city6 = c.City("Jinotepe", 1)

# #instanciar dao
# daoCity = daoConnection.DaoCity(conex)
# #insertar
# daoCity.insert(city1)
# daoCity.insert(city2)
# daoCity.insert(city3)
# daoCity.insert(city4)
# daoCity.insert(city5)
# daoCity.insert(city6)

# #consultar
# cities = daoCity.get_all()
# for city in cities:
#     print(city)



# #instanciar modelo - Job
# job1 = c.Job("Profesor", 1)
# job2 = c.Job("Granjero", 1)
# job3 = c.Job("Conductor", 1)
# job4 = c.Job("Pintor", 1)
# job5 = c.Job("Mecanico", 1)
# job6 = c.Job("Ingeniero", 1)

# #instanciar dao
# daoJob = daoConnection.Daojob(conex)
# #insertar
# daoJob.insert(job1)
# daoJob.insert(job2)
# daoJob.insert(job3)
# daoJob.insert(job4)
# daoJob.insert(job5)
# daoJob.insert(job6)


# #consultar
# jobs = daoJob.get_all()
# for job in jobs:
#     print(job)



# #instanciar modelo - Employee
# employee1 = c.Employee("Jader Mendoza", 32, 4, 6000, 1)
# employee2 = c.Employee("Juan Perez", 32, 4, 50000, 1)
# employee3 = c.Employee("Pedro Rodriguez", 33, 5, 3800, 1)


# #instanciar dao
# daoEmployee = daoConnection.DaoEmployee(conex)
# #insertar
# daoEmployee.insert(employee1)
# daoEmployee.insert(employee2)
# daoEmployee.insert(employee3)


# #consultar
# employees = daoEmployee.get_all()
# for employee in employees:
#     print(employee)

