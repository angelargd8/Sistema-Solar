# Práctica # 5: Sistema solar
# Autor: Angela Garcia, código: 307014, correo: angelargd8@gmail.com
# descripcion:  Demostrar los conocimientos adquiridos durante el informe
# Python 3.7
# recursos: Python, pygame
# sin modificaciones
import pygame
import math
import random
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
class Planeta:
  def __init__(self, nombre, r, d, a, c, centrosol_x, centrosol_y ):
    self.nombre = nombre
    self.radio = r
    self.distancia = d 
    self.angulo = a
    self.color = c
    self.centro_x = centrosol_x
    self.centro_y = centrosol_y
    self.pos_x = 0 #la ultima posicion del centro de un planeta, origen del radio
    self.pos_y = 0      
  def paint(self, screen):
    if self.nombre == "Sol":
        self.pos_x = self.centro_x
        self.pos_y = self.centro_y
    else:
           self.pos_x = round( (self.distancia + self.radio)*math.cos(self.angulo) + self.centro_x )
           self.pos_y = round( (self.distancia + self.radio)*math.sin(self.angulo) + self.centro_y )

    pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radio)
    font = pygame.font.Font(None, 20)
    #para los nombres del planetas y propiedades
    text = font.render(self.nombre, 1, (255,255,255)) #renderizar convertir las letras en grafico
    text2 = font.render(str(self.distancia) + " M. de KM", 1, (255,255,255))
    text3 = font.render(str(self.radio) + " Radio en KM",1, (255,255,255))#color blancoo
    screen.blit(text2, (self.pos_x-20, self.pos_y-17)) 
    screen.blit(text, (self.pos_x-30, self.pos_y-30))
    screen.blit(text3,(self.pos_x-10, self.pos_y-1))
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False #para el ciclo
clock = pygame.time.Clock()
#medidas partidas en 4, solo jupiter dentro de 5,  saturno, urano y neptuno dentro de 6
#el tamaño esta dividido dentro de 1000
x = int(SCREEN_WIDTH/2)
y = int(SCREEN_HEIGHT/2)
sol =  Planeta("Sol", 60, 0, 0, (random.randint(240,255), random.randint(240,255), 0), x, y) 
mercurio = Planeta("Mercurio", 2, 65 + sol.radio, random.randint(0,360), (200,200,200), x, y ) #random para ubicar los planetas en una posicion
venus = Planeta("Venus", 6, 77 + sol.radio, random.randint(0,360), (127,127,127), x, y)
tierra = Planeta("Tierra", 6, 88 + sol.radio, random.randint(0,360), (0,255,255), x, y)
luna =Planeta("Luna",2, 4 + tierra.radio, random.randint(0,360),(random.randint(240,255), random.randint(240,255), random.randint(240,255)), x, y)
marte = Planeta("Marte", 3, 133+ sol.radio, random.randint(0,360), (255,0,0), x, y)
jupiter = Planeta("Jupiter", 36, 163 + sol.radio, random.randint(0,360), (100,40,0), x, y) #tamaño /6
saturno = Planeta("Saturno", 29, 241+ sol.radio, 0, (115,0,0), x, y) #tamaño /7
urano = Planeta("Urano", 13, 342+ sol.radio, 0, (200,200,200), x, y) #tamaño /9
neptuno = Planeta("Neptuno", 12, 426+ sol.radio, 0, (0,0,255), x, y) #tamaño /11
planetas = [mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno]
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  screen.fill((0, 0, 0)) # color del fondo de la pantalla, color negro
  sol.color = (random.randint(75,255), random.randint(75,255), 0) #rgb
  sol.paint(screen)
  i=1
  while i <=200:
      i=i+1
      pygame.draw.circle(screen, (random.randint(1,200), random.randint(1,200), 0), (random.randint(0,SCREEN_WIDTH), random.randint(0,SCREEN_HEIGHT)) , 1)
  #pygame.draw.circle(screen, (random.randint(240,255), random.randint(240,255), 0), (x, y) ,  60)
  #se divide dentro de 2 ya que así se ubica en la mitad de la pantalla
  #la intensidad del color con random, sin cambiar el amarillo (segundo parametro) con rgb
  #tercero es la posicion del sol respecto a la pantalla
  #el 100 es el radio del solito
  for p in planetas:
    p.angulo = p.angulo + 0.01 #para que se muevan al mismo tiempo y cambiar el angulo, para ver la animacion
    p.paint(screen)  
    if p == tierra:
        luna.angulo= luna.angulo + 0.03 #0.03 por la velocidad
        luna.centro_x = tierra.pos_x
        luna.centro_y = tierra.pos_y
        luna.color = (random.randint(240,255), random.randint(240,255), random.randint(240,255))
        luna.paint(screen)        
  pygame.display.flip() #para que dibuje en el display, la pantalla
  clock.tick(40) #pulso del relojm


