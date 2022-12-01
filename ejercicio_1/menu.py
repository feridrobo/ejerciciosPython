numero1=int()
numero2=int()
nombre_usuario=str()

# Funcion Principal
def principal():
  while(True):
    mensaje='''
    seleccione la opcion: \n
    i. ingrese (dato dos numeros enteros y el nombre del usuario)\n 
    ii. realizar operaciones(suma, resta, multiplicacion y division)\n 
    iii. salir del programa
    '''
    print(mensaje)
    dato = input(" digite i o ii o iii: ")
    if dato.__eq__("i"):
        numero1=int(input("digite el numero 1:  "))
        numero2=int(input("digite el numero 2 : "))
        nombre_usario=input("escriba su nombre: ")
        recibir_datos(numero1,numero2,nombre_usario)
      
    elif dato.__eq__("ii"):
        texto = '''
        seleccione la opcion:\n 
        1. sumar\n
        2. restar\n 
        3. multiplicar\n 
        4. division\n 
        '''

        print(texto)

        dato = input("digite un numero para la operacion que desee realizar: ")

        if dato.__eq__("1"):
           resultado =  suma(numero1,numero2)
        elif dato.__eq__("2"):
           resultado = resta(numero1,numero2)
        elif dato.__eq__("3"):
           resultado= multiplicacion(numero1,numero2)
        elif dato.__eq__("4"):
           resultado = division(numero1,numero2)
        else:
            print("*****digite una opcion valida*****")
            
        notificacion(resultado)
        par_impar(resultado)
    elif dato.__eq__("iii"):
        break   
            
    
           
# Funcion Recibir datos   
def recibir_datos(num1,num2,nombre): 
  numero1=num1
  numero2=num2
  nombre_usuario=nombre 
  print("numero 1 es: "+ str(num1) +" Numero 2 es: "+str(num2 ) +" Numero 3 es: "+nombre )
  print("Se guardaron los datos exitosamente")

# Funcion sumar 
def suma(nume1,nume2):
    resultado = nume1 + nume2
    print(str(nume1) +" +  "+ str(nume2 )+" = " +  str(resultado ))
    
    return resultado
       
# Funcion Restar
def resta(nume1,nume2):
    resultado = nume1 - nume2
    print(str(nume1) +" - "+str(nume2 )+" = " + str(resultado ))
    return nume1 - nume2

# Funcion Dividir
def division(nume1,nume2):
    resultado = nume1 / nume2
    print(str(nume1) +" / "+ str(nume2) +" = " +  str(resultado) )
    return nume1 / nume2

# Funcion Multiplica
def multiplicacion(nume1,nume2):
    resultado = nume1 * nume2
    print(str(nume1) +" * "+ str(nume2) +" = " +  str(resultado) )
    return resultado

# Mostrar si el vaalor del resultaod es par o impar
def par_impar(resultado):
    if resultado % 2  == 0:
        print("el resultado es par ")
    elif resultado == 0 :
        print(" el resultado es 0 ")
    else: 
        print("el resultado es impar ")
        
# Mosttrar alerta de que el resultado se guardo correctamente en la base de datos
def notificacion(resultado):
    if resultado != 0:
        print("el resultado se guardo correctamente el la base de datos") 
    elif resultado == 0:
        print("el resultado no se guardo en la base de datos por que es cero") 
    else:
        print("el resultado es error")     

# llamar funcio principal
principal() 

             
  
