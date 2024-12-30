import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

# Screen setup
size = pygame.display.Info()
x = size.current_w
y = size.current_h - 50
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Simple Buttons")

# Colors and fonts
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
RED = (255, 0, 0)

font = pygame.font.Font(None, 40)

# Background and other images
bc_image = pygame.image.load("Pista.jpg")
bc_image2 = pygame.image.load("download (4).jpg")
bc_image2 = pygame.transform.scale(bc_image2,(x,y))
bc_image = pygame.transform.scale(bc_image, (x, y))
op_image = pygame.image.load("Pista.jpg")
op_x = 1830
op_y = 10
op_rect = op_image.get_rect(topright=(op_x, op_y))

sound = False

# Utility function for displaying text
def text(context, colour, xpos, ypos):
   msg = font.render(context, True, colour)
   screen.blit(msg, (xpos, ypos))

car_collsion = pygame.mixer.Sound("collision-83248.mp3")
car_collsion.set_volume(0)
# Function to handle the main game
def play_game():
   # Game variables
   car_w, car_h = 200, 200
   car_speed = 10
   maincar_w, maincar_h = 200, 200
   maincar_x = (x - maincar_w) // 2
   maincar_y = y - maincar_h - 10
   maincar_s = 20

   Road = pygame.image.load("Pista.jpg")
   Road = pygame.transform.scale(Road, (x, y))

   maincar = pygame.image.load("car_6-removebg-preview.png")
   maincar = pygame.transform.scale(maincar, (car_w, car_h))

   back_btn = pygame.image.load("game-buttons-wood-stone-gamer-interface_107791-10116.png")
   back_btn = pygame.transform.scale(back_btn,(50,50))
   backbtn_rect = back_btn.get_rect(center=(1860,10))

   car1 = pygame.image.load("car_1-removebg-preview.png")
   car1 = pygame.transform.scale(car1, (car_w, car_h))
   car2 = pygame.image.load("car_2-removebg-preview.png")
   car2 = pygame.transform.scale(car2, (car_w, car_h))
   car3 = pygame.image.load("car_3-removebg-preview.png")
   car3 = pygame.transform.scale(car3, (car_w, car_h))
   car4 = pygame.image.load("car_4-removebg-preview.png")
   car4 = pygame.transform.scale(car4, (car_w, car_h))

   cars = []
   score_value = 0

   bg_y1 = 0
   bg_y2 = -y
   game_running = True

   # Function to generate new cars
   def mul_cars():
       while True:
           car_type = random.choice([car1, car2, car3, car4])
           car_x = random.randint(0, x - car_w)
           car_y = -60
           overlap = False
           for car in cars:
               if (
                   car_x in range(car["x"] - car_w, car["x"] + car_w)
                   and car_y in range(car["y"] - car_h, car["y"] + car_h)
               ):
                   overlap = True
                   break
           if not overlap:
               return {"type": car_type, "x": car_x, "y": car_y}

   # Function to display score
   def show_score(value, colour):
       msg = font.render("Score: " + str(value), True, colour)
       screen.blit(msg, (10, 10))

   while game_running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   maincar_x -= maincar_s
               if event.key == pygame.K_RIGHT:
                   maincar_x += maincar_s
           if event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               if backbtn_rect.collidepoint(mouse_x, mouse_y):
                   game()

       # Generate new cars
       if random.random() < 0.02:
           cars.append(mul_cars())

       # Move background
       bg_y1 += 0.5
       bg_y2 += 0.5
       if bg_y1 >= y:
           bg_y1 = -y
       if bg_y2 >= y:
           bg_y2 = -y

       # Move cars and check for collisions
       for car in cars:
           car["y"] += car_speed
           if car["y"] > y:
               cars.remove(car)
               score_value += 1
               car_collsion.play()

       # Draw everything
       screen.blit(Road, (0, bg_y1))
       screen.blit(Road, (0, bg_y2))
       screen.blit(maincar, (maincar_x, maincar_y))
       for car in cars:
           screen.blit(car["type"], (car["x"], car["y"]))

       # Check for collisions
       maincar_rect = pygame.Rect(maincar_x, maincar_y, car_w, car_h)
       for car in cars:
           car_rect = pygame.Rect(car["x"], car["y"], car_w, car_h)
           if maincar_rect.colliderect(car_rect):
               return  # End game if collision occurs

       # Show score
       show_score(score_value, RED)
       screen.blit(back_btn,(1860,10))
       pygame.display.update()
       clock.tick(30)


def sett():
    box_1 = pygame.Rect(800, 350, 50, 50)
    back_btn = pygame.Rect(800, 460, 150, 50)
    bg_m = pygame.mixer.Sound("retro-game-arcade-236133.mp3")
    settings = True
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if box_1.collidepoint(mouse_x, mouse_y):
                    # bg_m.play()
                    car_collsion.set_volume(1)
                if back_btn.collidepoint(mouse_x,mouse_y):
                    game()

        screen.blit(bc_image2,(0,0))
        pygame.draw.rect(screen, WHITE, box_1, 5)
        pygame.draw.rect(screen, WHITE, back_btn, 5)
        text("Sound",RED,865,360)
        text("Back",RED,840,470)
        pygame.display.update()


# Main function
def game():
   running = True
   while running:
       screen.blit(bc_image, (0, 0))

       # Buttons
       play_btn = pygame.Rect(300, 250, 150, 50)
       set_btn = pygame.Rect(300, 350, 150, 50)

       pygame.draw.rect(screen, WHITE, play_btn, 5)
       pygame.draw.rect(screen, WHITE, set_btn, 5)
       text("Play", WHITE, 347, 260)
       text("Settings", WHITE, 320, 360)

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               if play_btn.collidepoint(mouse_x, mouse_y):
                   play_game()  # Start the game
               if set_btn.collidepoint(mouse_x, mouse_y):
                   sett()  # Add settings functionality here

       pygame.display.flip()


game()
