import random

juego = ['piedra','papel','tijera']

toca = random.choice(juego)

nombre = input('como te llamas?')
def jugamos(toca):
    piedrapapeltijera = input(f'Bienvenido, {nombre} elije entre piedra, papel, tijera \n')
    
    if toca.upper() == piedrapapeltijera.upper():
        print('Empate')
    elif toca.upper() == 'PIEDRA' and piedrapapeltijera.upper() == 'PAPEL':
        print('Gano el Jugador')
    elif toca.upper() == 'PAPEL' and piedrapapeltijera.upper() == 'TIJERA':
            print('Gano el Jugador')
    elif toca.upper() == 'TIJERA' and piedrapapeltijera.upper() == 'PIEDRA':
            print('Gano el Jugador')                
    elif toca.upper() == 'PAPEL' and piedrapapeltijera.upper() == 'PIEDRA':
        print('Gano la maquina')
    elif toca.upper() == 'TIJERA' and piedrapapeltijera.upper() == 'PAPEL':
        print('Gano la maquina')   
    elif toca.upper() == 'PIEDRA' and piedrapapeltijera.upper() == 'TIJERA':
        print('Gano la maquina')
    else:
        print('elegiste una posibilidad que no existe :(')
        jugamos(toca)
        
        
jugamos(toca)