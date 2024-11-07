from GESTION.DAL.db_emp import agregar_usuario, mostrar_empleados, eliminar_empleado
from GESTION.DAL.db_depto import agregar_departamento, actualizar_departamento, buscar_departamento, eliminar_departamento, mostrar_departamentos, asignar_departamento, reasignar_departamento
from GESTION.DAL.db_proyecto import crear_proyecto, actualizar_proyecto, eliminar_proyecto, mostrar_proyecto, asignar_proyecto_a_empleado
from GESTION.CLASES.informe import generar_informes_pdf

from GESTION.CLASES.asignacion import Asignacion
from colorama import Fore
import os
opcion =""
while opcion != '0': 
                os.system('cls')
                print("\nSistema de Gestión de Empleados") 
                print(Fore.BLUE + "[1] Añadir Empleados") 
                print(Fore.BLUE + "[2] Ver Empleados") 
                print(Fore.BLUE + "[3] Eliminar Empleados") 
                print(Fore.GREEN + "[4] Crear Departamento") 
                print(Fore.GREEN + "[5] Editar Departamento")
                print(Fore.GREEN + "[6] Buscar Departamentos")
                print(Fore.GREEN + "[7] Eliminar Departamento")            
                print(Fore.GREEN + "[8] Reasignar Departamento") 
                print(Fore.CYAN + "[9] Crear Proyecto") 
                print(Fore.CYAN + "[10] Editar Proyecto") 
                print(Fore.CYAN + "[11] Eliminar Proyecto") 
                print(Fore.CYAN + "[12] Asignar Proyecto") 
                print(Fore.CYAN + "[13] Generar Informe") 
                print(Fore.LIGHTMAGENTA_EX + "[S] salir")

                opcion = input(Fore.LIGHTWHITE_EX + "Elegir una opcion: ") 

                if opcion == "1": 
                    agregar_usuario()
                elif opcion == "2":
                    mostrar_empleados()
                elif opcion == "3":
                    eliminar_empleado()
                elif opcion == "4":
                     agregar_departamento()
                elif opcion == "5":
                    actualizar_departamento()
                elif opcion == "6":
                    nombre = input("Ingrese el nombre del departamento : ")
                    buscar_departamento(nombre)
                elif opcion == "7":
                    mostrar_departamentos()
                    nombre = input("Ingrese el nombre del departamento a eliminar: ")
                    eliminar_departamento(nombre)
                elif opcion == "8":
                    reasignar_departamento()
                elif opcion == "9":
                    crear_proyecto()
                elif opcion =="10":
                     actualizar_proyecto()
                elif opcion =="11":
                     mostrar_proyecto()
                     nombre_proyec = input("Ingrese el nombre del proyecto a eliminar: ")
                     eliminar_proyecto(nombre_proyec)
                elif opcion == "12":
                    persona = input("ingrese el id_rut:")
                    proyecto = input("ingrese el id_del proyecto a asignar: ")
                    asignar_proyecto_a_empleado(persona, proyecto)
                elif opcion=="13":
                    generar_informes_pdf("informe_departamento.pdf")
                    print("Informe PDF generado en 'informe_departamento.pdf'")
            
                elif (opcion.upper() == "S"):   # si opcion es salir nos despedimos
                    print("Hasta luego.")
                else:
                    print(f"{opcion} no es una opción válida")
                os.system('pause')


