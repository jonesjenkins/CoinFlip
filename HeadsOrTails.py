import random
import pygame

pygame.init()

screen_width = 600
screen_height = 600
small_font = pygame.font.SysFont("arial", 25)
med_font = pygame.font.SysFont("arial", 50)
large_font = pygame.font.SysFont("arial", 100)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
clock = pygame.time.Clock()

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Heads or Tails')

def main_screen():
    main = True
    button = pygame.Rect((screen_width / 2) - 60, 350, 120, 60)
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.collidepoint(event.pos):
                        main = False
                        coin_flip()
        game_display.fill(black)
        title_text = large_font.render('Heads or Tails', False, white)
        title_text_size = title_text.get_rect()
        game_display.blit(title_text, ((screen_width / 2) - (title_text_size.width / 2), 150))
        pygame.draw.rect(game_display, white, button)
        flip_button = med_font.render('Flip', False, red)
        flip_button_size = flip_button.get_rect()
        game_display.blit(flip_button, ((screen_width / 2) - (flip_button_size.width / 2), 350))
        pygame.display.update()
        clock.tick(5)


def coin_flip():
    finished = False
    coin_side = random.randint(0, 1)
    print(coin_side)
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)
        if not coin_side:
            side = 'Heads'
        elif coin_side:
            side = 'Tails'
        title_text = large_font.render(side, False, black)
        title_text_size = title_text.get_rect()
        game_display.blit(title_text, ((screen_width / 2) - (title_text_size.width / 2), 150))
        pygame.display.update()
main_screen()
coin_flip()