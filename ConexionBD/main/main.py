import os
import sys
sys.path.append(r"C:\Users\Jader Mendoza\Desktop\3er año - 1er cuatrimestre\Lenguaje de programacion\Python\ConexionBD")
from dao import daoConnection
from models import clases as c


os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()


#funcion para validar que el status sea valido (solamente puede ser 1 o 2)

    



#CIUDAD 
def InsertarCiudad():
    os.system('cls')
    name = input("Nombre ciudad: ")
    ciudad = c.City(name, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    #insertar
    daoCity.insert(ciudad)

def MostrarCiudad():
    os.system('cls')
    daoCity = daoConnection.DaoCity(conex)
    print("Ciudades de la base de datos: ")
    #mostrar
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def ElimiarCiudad():
    os.system('cls')
    MostrarCiudad()
    NameElimiar = input("ID de la ciudad a eliminar: ")
    
    daoCity = daoConnection.DaoCity(conex)
    #eliminar
    daoCity.delete(NameElimiar)



def validar_status(status):
    if status == 1 or status == 2:
        return True
    else:
        return False
    



def EditarCiudad():
    os.system('cls')
    MostrarCiudad()
    oldID = input("ID de la ciudad a editar: ")
    newName = input("Nuevo Nombre: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))


    if validar_status(newStatus):
        print("Status valido")
        daoCity = daoConnection.DaoCity(conex)
        ciudad = c.City(newName, newStatus, oldID)
        daoCity.update(ciudad)
    else:
        print("Status inválido. Debe ser 1 o 2.")


def BuscarCiudad():
    os.system('cls')
    nameBuscar = input("Nombre de la ciudad a buscar: ")
    
    daoCity = daoConnection.DaoCity(conex)
    #buscar
    cities = daoCity.get_by_id(nameBuscar)
    print(cities)

def menuCiudad():
    os.system('cls')
    print("----MENU CIUDAD----")
    print("1. Ingresar ciudad")
    print("2. mostrar ciudades")
    print("3. eliminar ciudad")
    print("4. editar ciudad")
    print("5. buscar ciudad")
    print("6. salir")

def mainCiudad():
    opcion= 0
    while(opcion != 6):
        menuCiudad()
        opcion = int(input("Ingresa una opcion: "))
        if (opcion == 1):
            InsertarCiudad()
            os.system("pause")
        elif (opcion == 2):
            MostrarCiudad()
            os.system("pause")
        elif (opcion == 3):
            ElimiarCiudad()
            os.system("pause")
        elif (opcion == 4):
            EditarCiudad()
            os.system("pause")    
        elif (opcion == 5):
            BuscarCiudad()
            os.system("pause")





#TRABAJOs
def InsertarTrabajo():
    os.system('cls')
    name = input("Nombre Trabajo: ")
    trabajo = c.Job(name, 1, any)

    daoJob = daoConnection.DaoJob(conex)
    #insertar
    daoJob.insert(trabajo)

def MostrarTrabajo():
    os.system('cls')
    daoJob = daoConnection.DaoJob(conex)
    print("Trabajos de la base de datos: ")
    #mostrar
    jobs = daoJob.get_all()
    for job in jobs:
        print(job)

def ElimiarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    NameElimiar = input("ID del trabajador a eliminar: ")
        
    daoJob = daoConnection.DaoJob(conex)
    #eliminar
    daoJob.delete(NameElimiar)

def EditarTrabajo():
    os.system('cls')
    MostrarTrabajo()
    oldId = int(input("ID del Trabajo a editar: "))
    newName = input("Nuevo Nombre: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))


    if validar_status(newStatus):
        print("Status valido")
        daoJob = daoConnection.DaoJob(conex)
        trabajo = c.Job(newName, newStatus, oldId)
        daoJob.update(trabajo)
    else:
        print("Status inválido. Debe ser 1 o 2.")


def BuscarTrabajo():
    os.system('cls')
    NameBuscar = input("Nombre del trabajo a buscar: ")
    
    daoJob = daoConnection.DaoJob(conex)

    job = daoJob.get_by_id(NameBuscar)
    print(job)

def menuTrabajo():
    os.system('cls')
    print("----Menu Trabajo----")
    print("1. Ingresar trabajo")
    print("2. Mostrar trabajos")
    print("3. Eliminar trabajo")
    print("4. Editar trabajo")
    print("5. Buscar trabajo")
    print("6. Salir")

def mainTrabajo():
    opcion= 0
    while(opcion != 6):
        menuTrabajo()
        opcion = int(input("Ingresa una opcion: "))
        if (opcion == 1):
            InsertarTrabajo()
            os.system("pause")
        elif (opcion == 2):
            MostrarTrabajo()
            os.system("pause")
        elif (opcion == 3):
            ElimiarTrabajo()
            os.system("pause")
        elif (opcion == 4):
            EditarTrabajo()
            os.system("pause")    
        elif (opcion == 5):
            BuscarTrabajo()
            os.system("pause")





#EMPLEADOS
def InsertarEmpleado():
    os.system('cls')
    nombre = input("Nombre del Empleado: ")
    MostrarCiudad()
    ciudadid = input("Ingrese el ID de la ciudad del empleado: ")
    MostrarTrabajo()
    jobid = input("Ingrese el ID del cargo del empleado: ")
    salario = input("Ingrese el salario del empleado: ")

    empleado = c.Employee(nombre, ciudadid, jobid, salario, 1, any)
    daoEmployee = daoConnection.DaoEmployee(conex)
    #insertar
    daoEmployee.insert(empleado)

def MostrarEmpleado():
    os.system('cls')

    daoEmployee = daoConnection.DaoEmployee(conex)
    print("Empleados de la base de datos: ")
    #mostrar empleados
    employees = daoEmployee.get_all()
    for employee in employees:
        print(employee)

def ElimiarEmpleado():
    os.system('cls')
    MostrarEmpleado()
    EmpleadoElimiar = input("ID del trabajador a eliminar: ")
        
    daoEmployee = daoConnection.DaoEmployee(conex)
    #eliminar
    daoEmployee.delete(EmpleadoElimiar)

def EditarEmpleado():
    os.system('cls')
    MostrarEmpleado()
    oldId = int(input("ID del empleado a editar: "))
    newName = input("Nuevo Nombre: ")
    newCityid = input("Nueva ID de ciudad: ")
    newJobid = input("Nueva ID de trabajo: ")
    newSalary = input("Nuevo salario: ")
    newStatus = int(input("Ingrese el nuevo estado: 1) Activo || 2) Inactivo: "))

    if validar_status(status):
        print("Status valido")
        daoEmployee = daoConnection.DaoEmployee(conex)
        empleado = c.Employee(newName, newCityid, newJobid, newSalary, newStatus, oldId)
        daoEmployee.update(empleado)
    else:
        print("Status inválido. Debe ser 1 o 2.")


def BuscarEmpleado():
    os.system('cls')
    nameBuscar = input("escriba el nombre del empleado que quiere buscar:")

    daoEmployee = daoConnection.DaoEmployee(conex)
    #buscar e imprimir
    employee = daoEmployee.get_by_id(nameBuscar)
    print(employee)

def MenuEmpleado():
    os.system('cls')
    print("----MENU Empleados----")
    print("1. Ingresar empleado")
    print("2. Mostrar empleados")
    print("3. Eliminar empleado")
    print("4. Editar empleado")
    print("5. Buscar empleado")
    print("6. Salir")

def mainEmpleado():
    opcion= 0
    while(opcion != 6):
        MenuEmpleado()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            InsertarEmpleado()
            os.system("pause")
        elif (opcion == 2):
            MostrarEmpleado()
            os.system("pause")
        elif (opcion == 3):
            ElimiarEmpleado()
            os.system("pause")
        elif (opcion == 4):
            EditarEmpleado()
            os.system("pause")    
        elif (opcion == 5):
            BuscarEmpleado()
            os.system("pause")



#MAIN MENU
def MenuPrincipal():
    print("----MENU PRINCIPAL----")
    print("1. Registros Ciudades")
    print("2. Registros Trabajos")
    print("3. Registros Empleados")
    print("4. Salir")

def main():
    opcion= 0
    while(opcion != 4):
        os.system('cls')
        MenuPrincipal()
        opcion = int(input("Ingresa una opcion: "))
        if (opcion == 1):
            mainCiudad()
            os.system("pause")
        elif (opcion == 2):
            mainTrabajo()
            os.system("pause")
        elif (opcion == 3):
            mainEmpleado()
            os.system("pause")       
        
                        
main()