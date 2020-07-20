import pygame
import random

#Serpiente cuerpo
class cuerpo:
    def __init__(self,ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana

    def dibujar(self):
        pygame.draw.rect(self.ventana, (0, 225, 0), (self.x, self.y, 10, 10))

    def moverse(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


#Manzanas_comida
class manzanas:
    def __init__(self, ventana):
        self.x = random.randrange(40)*10
        self.y = random.randrange(40)*10
        self.ventana = ventana

    def dibujar(self):
        pygame.draw.rect(self.ventana, (225, 0, 0), (self.x, self.y, 10, 10))

    def nueva_manzana(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10


def refrescar(ventana):
    ventana.fill((0, 0, 0))
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()

def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente) - i - 1].x = serpiente[len(serpiente) - i - 2].x
        serpiente[len(serpiente) - i - 1].y = serpiente[len(serpiente) - i - 2].y


#funcion principal
def main():
    global serpiente, comida, score, instrucciones, puntajes, indice
    #
    instrucciones = open("INSTRUCCIONES.txt","r")
    for cadena in instrucciones:
        print(cadena)

    instrucciones.close()
    print()
    #
    ventana = pygame.display.set_mode((400, 400))
    ventana.fill((0, 0, 0))
    comida = manzanas(ventana)
    serpiente = [cuerpo(ventana)]
    score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                if event.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                if event.key == pygame.K_DOWN:
                    serpiente[0].dir = 2
                if event.key == pygame.K_UP:
                    serpiente[0].dir = 3


        serpiente[0].moverse()
        refrescar(ventana)
        pygame.display.update()
        pygame.time.delay(115)
        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))
            score += 1
        seguir_cabeza()

        # Traspasar muros
        if serpiente[0].x >= 400:
            print(f"Game over!    Score: ", score)
            run = False
            #serpiente[0].x = 0
        if serpiente[0].x < 0:
            print(f"Game over!    Score: ", score)
            run = False
            #serpiente[0].x = 390
        if serpiente[0].y >= 400:
            print(f"Game over!    Score: ", score)
            run = False
            #serpiente[0].y = 0
        if serpiente[0].y < 0:
            print(f"Game over!    Score: ", score)
            run = False
            #serpiente[0].y = 390


    puntajes = []

    historial = open("Puntajes.txt", "a")
    historial.write("Puntaje: "+ str(score))
    historial.write("\n")
    historial.close()

    historial = open("Puntajes.txt", "r")
    for x in historial:
        letras, numerot = x.split(":")
        numero = int(numerot)
        puntajes.append(numero)

    historial.close()

    print()

    def indice_mayor(lista):
        mayor = lista[0]
        indice = 0
        for i in range(len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
                indice = i
        return indice

    print("MAYOR PUNTAJE HASTA AHORA: ", puntajes[indice_mayor(puntajes)])





if __name__ == '__main__':
    main()
    pygame.quit()