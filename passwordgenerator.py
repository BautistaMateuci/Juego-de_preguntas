from secrets import choice

print('Bienvenido al generador de contraseñas random de bauti')
longuitud = int(input('Introduce el maximo: '))
caracteres = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#%&+"

password = ''
password= password.join([choice(caracteres) for i in range (longuitud)])

print(f'tu password es: {password}')