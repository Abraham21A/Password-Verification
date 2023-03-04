"""Verificador de contraseña / Password Verification"""

# Inicializa el contador a 3, lo que son los intentos para pobrar el programa
contador = 3

# Mientras el contador sea mayor que cero
while contador > 0:
   # Pide al usuario que ingrese una contraseña
  my_password = input("Ingrese Una contraseña: ")

  # Si el primer caracter de la contraseña es un número
  if my_password[0].isnumeric():
    # Pide al usuario que ingrese la contraseña nuevamente para confirmarla
    confirm_password = input("Ingrese la contraseña nuevamente: ")
    # Si la contraseña original y la confirmación coinciden
    if my_password == confirm_password:
      # Muestra un mensaje de contraseña correcta y sale del bucle while
      print("Contraseña correcta")
      break
    else:
      # Si la contraseña original y la confirmación no coinciden, muestra un mensaje de error y disminuye el contador en 1
      print("Las contraseñas no coinciden")
      contador -= 1
  else:
    # Si el primer caracter de la contraseña no es un número, muestra un mensaje de error y disminuye el contador en 1
    print("La contraseña debe comenzar con un numero")
    contador -= 1

  # Si el contador llega a cero, muestra un mensaje de error y sale del programa
  if contador == 0:
    print("Ha excedido el número de intentos permitidos. El programa se cerrará ahora.")
    exit()

