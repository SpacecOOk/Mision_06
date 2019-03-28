#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Dibujar circulos con Pygame
import math
import pygame
import random

ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)
MORADO = (210, 0, 215)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        k = r/R
        periodo = r//math.gcd(r, R)
        for angulo in range(0,360*periodo,1):
            a = math.radians(angulo)
            x = int(R*(((1-k)*math.cos(a)) + l*(k*(math.cos(((1-k)/k)*a)))))
            y = int(R*(((1-k)*math.sin(a)) - l*(k*(math.sin(((1-k)/k)*a)))))
            #x = y = int( radio*math.cos(a))
            #y = int( radio*math.sin(a))

            pygame.draw.circle(ventana,NEGRO, (ANCHO//2+x,ALTO//2-y), 2)
            pygame.draw.circle(ventana, MORADO, (213 + x, 160 - y), 1)
            pygame.draw.circle(ventana, MORADO, (426 + x, 160 - y), 1)
            pygame.draw.circle(ventana, MORADO, (213 + x, 320 - y), 1)
            pygame.draw.circle(ventana, MORADO, (426 + x, 320 - y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    r = int(input("dame r"))
    R = int(input("dame R"))
    l = float(input("dame L"))
    dibujar(r, R, l)


main()