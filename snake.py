import pygame
from random import randint

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

try:
    print(pygame.init())
except:
    print('Erro!')

largura = 640
altura = 480
tamanho = 10 # Pixels

relogio = pygame.time.Clock() 
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 50)

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x,pos_y, tamanho, tamanho])

def texto(msg, cor):
    texto1 = font.render(msg, True, azul)
    fundo.blit(texto1, [largura/2, altura/2])    
    
def jogo():
    loop = True
    pos_x = randint( 0,(largura-tamanho)/10 ) * 10
    pos_y = randint(0,(altura-tamanho)/10 ) * 10
    maca_x = randint( 0,(largura-tamanho)/10 ) * 10
    maca_y = randint(0,(altura-tamanho)/10 ) * 10
    
    velocidade_x = 0
    velocidade_y = 0

    CobraXY = []
    CobraComp = 1

    while loop:
        for event in pygame.event.get():                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                elif event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                elif event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_y = -tamanho
                    velocidade_x = 0
                elif event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_y = tamanho
                    velocidade_x = 0
            elif event.type == pygame.QUIT:
                loop = False            
        fundo.fill(branco)        

        pos_x += velocidade_x
        pos_y += velocidade_y

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        
        CobraXY.append(CobraInicio)
                                
        if len(CobraXY)>CobraComp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            break
             
        

        cobra(CobraXY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randint( 0,(largura-tamanho)/10 ) * 10
            maca_y = randint( 0,(altura-tamanho)/10 ) * 10
            CobraComp += 1
        
        maca(maca_x, maca_y)
        relogio.tick(15) # 15 frames/segundos
        pygame.display.update()
        if pos_x >= largura:
            pos_x = 0
        if pos_x < (0-tamanho):
            pos_x = largura - tamanho
        if pos_y >= altura:
            pos_y = 0
        if pos_y < (0-tamanho):
            pos_y = altura - tamanho    
            

jogo()

texto('GAME OVER', vermelho)
pygame.quit()


