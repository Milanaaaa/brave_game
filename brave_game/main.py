import pygame


def inter(x1, y1, x2, y2, db1, db2):
    if x1 > x2 - db1 and x1 > x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
        return 1
    else:
        return 0


pygame.init()

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))
player = pygame.Surface((40, 40))
zet = pygame.Surface((40, 40))
arrow = pygame.Surface((20, 40))

player.set_colorkey((255, 255, 255))
arrow.set_colorkey((0, 0, 0))
zet.set_colorkey((0, 0, 0))

img_a = pygame.image.load('hrab_serd_images/arrow.png')
img_p = pygame.image.load('hrab_serd_images/player_merida.png')
img_z = pygame.image.load('hrab_serd_images/target.png')
img_bg = pygame.image.load('hrab_serd_images/bg_shooter.png')

count = 0
my_font = pygame.font.SysFont('monospace', 15)

a_x = 1000
a_y = 1000
strike = False

z_x = 0
z_y = 0
step=0.05

p_x = 180
p_y = 300

right = True

done = False
while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        # if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
        #     p_y += 10
        # if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
        #     p_y -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            p_x -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            p_x += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                a_x = p_x
                a_y = p_y - 40
    if strike:
        a_y -= 0.5
        if a_y < 0:
            strike = False
            a_x = 1000
            a_y = 1000

    if inter(a_x, a_y, z_x, z_y, 20, 40):
        count += 1
        step+=0.02
        strike = False
        a_x = 1000
        a_y = 1000

    if right:
        z_x += step
        if z_x > 400:
            z_x -= step
            right = False
    else:
        z_x -= step
        if z_x < 0:
            z_x += step
            right = True

    string = my_font.render('Очков: ' + str(count), 0, (255, 0, 0))

    screen.blit(img_bg, (0, 0))
    arrow.blit(img_a, (0, 0))
    player.blit(img_p, (0, 0))
    zet.blit(img_z, (0, 0))
    screen.blit(string, (0, 50))
    screen.blit(arrow, (a_x, a_y))
    screen.blit(zet, (z_x, z_y))
    screen.blit(player, (p_x, p_y))
    window.blit(screen, (0, 0))
    pygame.display.update()

pygame.quit()
