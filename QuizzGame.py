preguntas= [      
  ["¿Qué selección de fútbol ha ganado más Mundiales?: (A) Brasil   (B) Alemania   (C)Argentina "],
  ["¿Cuándo se celebró el primer mundial de fútbol?: (A) 1930   (B) 1830  (C) 1900    "],
  ["¿Cuáles son los colores primarios?: (A) Verde, Amarrillo y Azul    (B) Amarillo, Azul y Rojo   (C) Verde, Amarillo y Rojo   (D) Rojo, Azul y Verde"],
  ["¿Cuántos gramos hay en una Onza?: (A) 32gr.   (B) 28gr.   (C) 500gr.   (D) 250gr."],
  ["¿Cuántos días tiene febrero en un año bisiesto?: (A) 29   (B) 30   (C) 31   (D) 27"],
  ["¿Qué elemento tiene como símbolo la letra Ag?: (A) Oro   (B) Argón   (C) Plata   (D) Manganeso"],
  ["¿Cuál es la capital de Canadá?: (A) Toronto   (B) Ontario   (C) Ottawa   (D) Montreal"],
  #========================================================HISTORIA==========================================================================================
  ['El periodo en el que aparecieron la agricultura y los asentamientos sedentarios se llama: (A) Neolitico  (B) Edad Media  (C) Paleolitico'],
  ['¿Cuándo se inventó la escritura? (A) Hace 20 mil años  (B) En el IV milenio a.C   (C) En el año 0'],
  ['¿Cómo se llamaban los gobernantes del antiguo Egipto?  (A) Faraones  (B)Basileos  (C)Alcades'],
  [' Según las leyendas de la antiguedad, ¿quiénes fundaron a Roma?  (A) Aquiles y Odiseo  (B) Alejandro Magno y Ptolomeo (C) Romulo y Remo'],
  ['¿Contra quiénes se enfrentaron los griegos en las Guerras Médicas del siglo V a.C.? (A) Los celtas (B) Los persas (C) Los hebreos'],
  ['¿Cuál de estos emperadores fue alumno del filósofo griego Aristóteles? (A)Carlomagno (B)Trajano (C)Alejandro Magno'],
  ['El primer emperador romano que se hizo cristiano fue: (A)Constantino I, el grande (B)Marco Aurelio (C)Neron'],
  #========================================================GEOGRAFIA==========================================================================================
  ['¿Cuál es la capital de Turquía? (A) Ankara (B) Enkara (C) Riyad'],
  ['¿Cuál es el nombre del desierto de México? (A) Senora (B) Sonora (C) Señora'],
  ['¿Cuantos continentes hay en el mundo? (A) 6 (B) 5 (C) 7'],
  ['¿En qué isla italiana está Pelarmo? (A) Sicilia (B) Palermo no esta en una isla (C)Pelarmo no existe'],
  ['¿Cuál es el desierto cálido más grande de la tierra? (A) Atacama (B) Sahara ' ],
  [' ¿Qué río discurre por Roma? (A) Tiber (B) Amazonas  (C) Po'],
  ['¿En que pais se encuentra Barcelona? (A) España (B) Cataluña (C)Andorra'],


]

respuestas1 = ['A','A','B','B','A','C','C',
               'A','B','A','C','B','C','A',
               'A','B','C','C','B','A','A']
print(respuestas1)

def futbol():
    print(f'Bienvenido a las quizz de Futbol {nombre}, empezamos :)!')
    i = 0
    puntos = 0
    for i in range(0, 7):
        print(preguntas[i])
        respuesta = input('Introduce tu respuesta \n ')
        if respuesta.upper() == respuestas1[i]:
            print('Correcto! :D')
            puntos = puntos + 1
        else:
            print('Incorrecto :(')
    print(f'Gracias por jugar {nombre} tu puntuacion fue de {puntos}')
    
def geografia():
    print(f'Bienvenido a las quizz de Geografia {nombre}, empezamos :)!')
    i = 7
    puntos = 0
    for i in range(7, 14):
        print(preguntas[i])
        respuesta = input('Introduce tu respuesta \n ')
        if respuesta.upper() == respuestas1[i]:
            print('Correcto! :D')
            puntos = puntos + 1
        else:
            print('Incorrecto :(')
    print(f'Gracias por jugar {nombre} tu puntuacion fue de {puntos}')
    
def historia():
    print(f'Bienvenido a las quizz de Historia {nombre}, empezamos :)!')
    i = 0
    puntos = 0
    for i in range(14, 21):
        print(preguntas[i])
        respuesta = input('Introduce tu respuesta \n ')
        if respuesta.upper() == respuestas1[i]:
            print('Correcto! :D')
            puntos = puntos + 1
        else:
            print('Incorrecto :(')
    print(f'Gracias por jugar {nombre} tu puntuacion fue de {puntos}')
    
nombre = input('Hola bienvenido al juego de preguntas de bauti, pruebalo las veces que quieras, aceptamos cualquier consejos :) \n porfa introduce tu nombre aqui: ')
def JugarQuizz(nombre):
    modo = str(input(f'Bienvenido al juego {nombre}, espero lo disfrutes  :D !, elige entre futbol, geografia o historia y comenzemos \n'))
    if modo.capitalize() == 'Futbol':
        futbol()
    elif modo.capitalize() == 'Geografia':
        geografia()
    elif modo.capitalize() == 'Historia':
        historia()
    else:
        print('No tenemos esa modalidad disponible aun, vuelve pronto!! :(')
        JugarQuizz(nombre)

JugarQuizz(nombre)




















def futbol():
    print(f'Bienvenido a las quizz de futbol {nombre}, empezamos :)!')
    i = 0
    puntos = 0
    for i in range(0, 7):
        print(preguntas[i])
        respuesta = input('Introduce tu respuesta \n ')
        if respuesta == respuestas1[i]:
            print('Correcto! :D')
            puntos = puntos + 1
        else:
            print('Incorrecto :(')
    print(f'Gracias por jugar {nombre} tu puntuacion fue de {puntos}')        
        
