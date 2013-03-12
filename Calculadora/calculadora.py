'''
Created on 11/03/2013

@author: Alumno
'''
'''
Created on 11/03/2013

@author: Alumno
'''
def main():
    
    print ("")
    print ("CALCULADORA PYTHON")
    print ("******************\n")
      
    valor1 = int(input("Primer valor: "))       # Primer valor
    valor2 = int(input("Segundo valor: "))      # Segundo valor
    calcular = True
   
    def sumar(numero1, numero2):    
        suma = numero1 + numero2
        return suma
    
    def restar(numero1, numero2):
        resta = numero1 - numero2
        return resta
    
    def multiplicar(numero1, numero2):
        multiplica = numero1 * numero2
        return multiplica
    
    def dividir(numero1, numero2):
        divide = numero1 / numero2
        return divide
    
    resultado = 0
    
    while(calcular):
        opcion = input("Seleccione operacion: ")
        if (opcion == "+"):                     # Suma
            resultado = sumar(valor1,valor2)
            calcular = False
            
        elif (opcion == "-"):                   # Resta
            resultado = restar(valor1, valor2)
            calcular = False
            
        elif opcion == "*":                     # Multiplicacion
            resultado = multiplicar(valor1, valor2)
            calcular = False
                
        elif opcion == "/":                     # Division
            resultado = dividir(valor1, valor2)
            calcular = False
        
        else:                                   # Opcion incorrecta
            print ("Seleccione una operacion correcta")
    
    print("Resultado: " + str(resultado))
    
    # Para volver a ejercutar la calculadora 
    eleccion = input('Quieres realizar otra operacion (SI/NO)?')
    if(eleccion == "SI"):
        eleccion = main()
    elif(eleccion == "NO"):
        print ("ADIOS")
    else:
        print ("Eleccion incorrecta")   
main()