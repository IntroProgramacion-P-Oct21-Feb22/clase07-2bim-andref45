"""
    @reroes
    Ejemplo de manejo  de Excepciones
    http://docs.python.org.ar/tutorial/3/errors.html
    salida

Ingreso de datos de empleado

Ingreso su nombre :
René
Traceback (most recent call last):
  File "ejemplo2.py", line 16, in <module>
    print("Los datos ingresados son %s %s" % (nombre, apellido))
NameError: name 'apellido' is not defined
"""
print("Ingreso de datos de empleado\n")
contador = 1
while contador <= 5:
    nombre = input("Ingreso su nombre : \n")
    apellido = input("Ingreso su apellido :\t")
    print("Los datos \ningresados son \n%s \n%s\n" % (nombre, apellido))
    contador = contador + 1
print ("Proceso terminado")

