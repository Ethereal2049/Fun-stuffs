
#Rule of the game: if there are odd numbers of collisions then B wins, if there are even number of collisions A wins


import pygame

pygame.init()

width,height = 1200,500
color_white = 255,255,255

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("spenner's game")

# Creating font
font_size = 24
final_font_size = 30
font = pygame.font.SysFont('Arial',font_size,True)
font_final = pygame.font.SysFont('Arial',final_font_size,True)

# Load image
letter_A_image = pygame.transform.scale(pygame.image.load('a.png'),(80,60))
letter_B_image = pygame.transform.scale(pygame.image.load('b.png'),(80,60))

# Lists, for the logic determination
chart = [0,0,0,0,0,0]
spot = [1,2,3,4,5,6]


# Initialize the game window
def draw_window():
    k = 100
    window.fill(color_white)
    pygame.draw.line(window,(0,0,0) ,(100,150), (1060,150), 3)
    pygame.draw.line(window,(0,0,0) ,(100,250), (1060,250), 3)
    for f in range(0,7):
        pygame.draw.line(window,(0,0,0) ,(k,150), (k,250), 3)
        k += 160

# Erase texts
def clean():
    message_surface = pygame.Surface((400, 500))
    message_surface.fill((255,255,255))
    window.blit(message_surface, (100, 290))
    pygame.display.update()


# Function for spot 1
def spot_1():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(140,170))
                    chart[0] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(140,170))
                    chart[0] = 'B'
                    pygame.display.update()
                    clean()
                    return



# Function for spot 2
def spot_2():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(300,170))
                    chart[1] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(300,170))
                    chart[1] = 'B'
                    pygame.display.update()
                    clean()
                    return



# Function for spot 3
def spot_3():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(460,170))
                    chart[2] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(460,170))
                    chart[2] = 'B'
                    pygame.display.update()
                    clean()
                    return
                



# Function for spot 4
def spot_4():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(620,170))
                    chart[3] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(620,170))
                    chart[3] = 'B'
                    pygame.display.update()
                    clean()
                    return
                



# Function for spot 5
def spot_5():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(780,170))
                    chart[4] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(780,170))
                    chart[4] = 'B'
                    pygame.display.update()
                    clean()
                    return
                



# Function for spot 6
def spot_6():
    text_letter = font.render("Choose a Letter(A or B): ", True, (0,0,0))
    window.blit(text_letter, (100, 390))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    window.blit(letter_A_image,(950,170))
                    chart[5] = 'A'
                    pygame.display.update()
                    clean()
                    return
                elif event.key == pygame.K_b:
                    window.blit(letter_B_image,(950,170))
                    chart[5] = 'B'
                    pygame.display.update()
                    clean()
                    return
                
# count for collision          
def collision_fun():
    collision = 0
    for i in range(len(chart)-1):
        if chart[i] != chart[i+1]:
            collision += 1
    if chart and chart[0] != chart[-1]:
        if collision == 1:
            text_collision = font_final.render(f"{collision} collision, B won!",True,(0,0,0))
            window.blit(text_collision, (470, 80))
            pygame.display.update()
        else:
            text_collision = font_final.render(f"{collision} collisions, B won!",True,(0,0,0))
            window.blit(text_collision, (470, 80))
            pygame.display.update()
    elif chart and chart[0] == chart[-1]:
        text_collision = font_final.render(f"{collision} collisions, A won!",True,(0,0,0))
        window.blit(text_collision, (470, 80))
        pygame.display.update()
        

# main game function 
def main_game():
        if not spot:
            clean()
            collision_fun()
            return
        text = font.render(f"Choose a Spot{spot}:",True,(0,0,0))
        window.blit(text, (100, 290))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and 1 in spot:
                    window.blit(font.render("1",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(1)
                    spot_1()
                elif event.key == pygame.K_2 and 2 in spot:
                    window.blit(font.render("2",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(2)
                    spot_2()
                elif event.key == pygame.K_3 and 3 in spot:
                    window.blit(font.render("3",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(3)
                    spot_3()
                elif event.key == pygame.K_4 and 4 in spot:
                    window.blit(font.render("4",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(4)
                    spot_4()
                elif event.key == pygame.K_5 and 5 in spot:
                    window.blit(font.render("5",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(5)
                    spot_5()
                elif event.key == pygame.K_6 and 6 in spot:
                    window.blit(font.render("6",True,(0,0,0)), (100, 320))
                    pygame.display.update()
                    spot.remove(6)
                    spot_6()


            


#draw the window
draw_window()

# sperner's game
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    main_game()







    


