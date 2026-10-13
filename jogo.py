import pygame
import random
from pathlib import Path

pygame.init()

LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rato em busca do queijo')
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 30)

# Carrega os sprites que ficam na mesma pasta deste arquivo
pasta = Path(__file__).resolve().parent
imagem_rato = pygame.image.load(str(pasta / 'rato.png')).convert_alpha()
imagem_queijo = pygame.image.load(str(pasta / 'queijo.png')).convert_alpha()
imagem_rato = pygame.transform.smoothscale(imagem_rato, (55, 55))
imagem_queijo = pygame.transform.smoothscale(imagem_queijo, (50, 50))

rato = imagem_rato.get_rect(center=(LARGURA // 2, ALTURA // 2))
queijo = imagem_queijo.get_rect(topleft=(100, 100))
pontos = 0
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimenta o rato usando as setas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        rato.x -= 5
    if teclas[pygame.K_RIGHT]:
        rato.x += 5
    if teclas[pygame.K_UP]:
        rato.y -= 5
    if teclas[pygame.K_DOWN]:
        rato.y += 5

    rato.clamp_ip(tela.get_rect())

    # Quando o rato toca o queijo, o queijo muda de lugar
    if rato.colliderect(queijo):
        pontos += 1
        while True:
            queijo.x = random.randint(0, LARGURA - queijo.width)
            queijo.y = random.randint(50, ALTURA - queijo.height)
            if not rato.colliderect(queijo):
                break

    tela.fill((255, 255, 255))
    tela.blit(imagem_rato, rato)
    tela.blit(imagem_queijo, queijo)
    texto = fonte.render(f'Queijos: {pontos}', True, (0, 0, 0))
    tela.blit(texto, (10, 10))
    pygame.display.update()
    relogio.tick(60)

pygame.quit()
