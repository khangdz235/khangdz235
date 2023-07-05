import pygame
import time

pygame.init()

screen = pygame.display.set_mode((550,600))

GREY = (0,0,0)
WHITE = (255, 255, 255)

running = True


font = pygame.font.SysFont('sans', 45)
text_1 = font.render('+', True, GREY)
text_2 = font.render('+', True, GREY)
text_3 = font.render('-', True, GREY)
text_4 = font.render('-', True, GREY)
text_5 = font.render('Start', True, GREY)
text_6 = font.render('Reset', True, GREY)

total_secs = 0
total = 0
is_Start= False

while running:
    screen.fill(GREY)


    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    
    
    



    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,50,50,50))
    pygame.draw.rect(screen, WHITE, (100,200,50,50))
    pygame.draw.rect(screen, WHITE, (200,200,50,50))
    pygame.draw.rect(screen, WHITE, (350,50,100,50))
    pygame.draw.rect(screen, WHITE, (350,150,100,50))
    pygame.draw.rect(screen, WHITE, (100,500,350,50))

    screen.blit(text_1, (113,45))
    screen.blit(text_2, (213,45))
    screen.blit(text_3, (120,190))
    screen.blit(text_4, (220,190))
    screen.blit(text_5, (355,50))
    screen.blit(text_6, (350,150))
    
    pygame.draw.circle(screen, WHITE, (270,370), 100)

    pygame.draw.line(screen, GREY, (270,270), (270,370))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if (100 < mouse_x < 150) and (50 < mouse_y < 100):
                    total_secs += 60
                    print("press + min")
                if (100 < mouse_x < 150) and (200 < mouse_y < 250):
                    total_secs -= 60
                    print("press - min")
                if (200 < mouse_x < 250) and (50 < mouse_y < 100):
                    total_secs += 1
                    print("press + second")
                if (200 < mouse_x < 250) and (200 < mouse_y <250):
                    total_secs -= 1
                    print("press - second")
                if (350 < mouse_x < 450) and (50 < mouse_y < 100):
                    is_Start = True
                    print("total_secs:" +  str(total_secs))
                    print("Start")
                if (350 < mouse_x < 450) and (150 < mouse_y < 200):
                    total_secs = 0
                    is_Start = False
                    print("Reset")
                print("total_secs:" + str(total_secs))


    if is_Start:
        total_secs -= 1
        if total_secs == 0:
            print("Het gio")
        time.sleep(1)
    

    if total_secs < 0:
        is_Start = False
        total_secs = 0



    mins = total_secs/60
    mins = int(mins)

    secs = total_secs - mins*60



    time_str = str(mins) + ":" + str(secs)
    text_min = font.render(time_str, True, WHITE)
    screen.blit(text_min, (120,120))


    


    pygame.display.flip()

pygame.quit()

