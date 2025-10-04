import pygame
import random

pygame.init()
running = True
width = 930
height = 600
Score = 0
Lives = 1
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

background = pygame.image.load("assets/New_Better_Background.jpg")
background = pygame.transform.scale(background,(width, height))
Aple = pygame.image.load("assets/apple.png")
Aple = pygame.transform.scale(Aple,(100,100))

fruit_names = ["apple","avocado","lemon", "mushroom", "coconut", "onion", "pear",'Bomb','Bomb','Bomb','Bomb','Bomb']
font = pygame.font.SysFont('Papyrus',35)
full_imgs = {}
half_imgs = {}

for name in fruit_names:
    full = pygame.image.load("assets/"+name+".png")
    half = pygame.image.load("assets/"+name+'-half.png')

    full_imgs[name] = pygame.transform.scale(full,(80,80))
    half_imgs[name] = pygame.transform.scale(half,(80,80))
fruits =[] #random fruit will be appended here
def add_Fruit(fruit_list):
    global name,x,y,velocity,gravity
    name = random.choice(fruit_names)
    x = random.randint(50,800)
    y = 450
    velocity = -random.randint(20,28)
    gravity = 0.7

    fruit = {
            'name' : name,
            'x' : x,
            'y' : y,
            'velocity' : velocity,
            'g' : gravity,
            'cut' : False,
            'timer' : 0
    }

    fruit_list.append(fruit)

def draw_Da_fruuit(fruit_list):

    for fruit in fruit_list:
        name = fruit['name']
        x = fruit['x']
        y = fruit['y']

        if fruit['cut'] == False:
            img = full_imgs[name]
        else:
            img = half_imgs[name]

        screen.blit(img,(x,y))
def move_fruits(fruit_list):
    for fruits in fruit_list:
        fruits['velocity'] += fruits['g']
        fruits['y'] += fruits['velocity']

def fruit_clicked(fruit_list,pos,Score,Lives):
    fx,fy = pos

    for fruit in fruit_list:
        if not fruit['cut'] and  fruit['name']!='Bomb':
            if fruit['x']<fx<fruit['x'] + 70 and fruit['y']<fy<fruit['y']+ 80:
                fruit['cut'] = True
                fruit['timer'] = 10
                Score += 1
        if not fruit['cut'] and fruit['name'] == 'Bomb':
            if fruit['x'] < fx < fruit['x'] + 70 and fruit['y'] < fy < fruit['y'] + 80:
                fruit['cut'] = True
                fruit['timer'] = 10
                Lives -= 1
    return Score,Lives
# print(full_imgs)
# print(half_imgs)

def game_score(Score):
    text = 'Score: '+str(Score)
    var = font.render(text,True,'White')
    screen.blit(var,(790,0.1))

def game_lives(Lives):
    text1 = 'Lives: '+str(Lives)
    var = font.render(text1,True,'White')
    screen.blit(var,(10,0.1))

def Game_Over():
    screen.fill('Black')
    text2 = 'Game Over!!!'
    var = font.render(text2,True,'Red')
    screen.blit(var,(375,200))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
spawn_timer = 0
while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            Score,Lives = fruit_clicked(fruits,mouse_pos,Score,Lives)

        if Lives == 0:
            Game_Over()


    screen.blit(background,(0,0))

    spawn_timer += 1
    if spawn_timer >= 50:
        add_Fruit(fruits)
        spawn_timer = 0

    # screen.blit(full_imgs['lemon'],(100,100))
    # screen.blit(half_imgs['lemon'],(200,100))
    game_score(Score)
    game_lives( Lives)
    draw_Da_fruuit(fruits)
    move_fruits(fruits)
    pygame.display.flip()
    pygame.time.delay(20)

    #Upload to Github