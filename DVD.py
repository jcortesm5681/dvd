import pygame
import os
import random

def load_images():
    ruta = os.path.dirname(__file__)
    images = [pygame.image.load(os.path.join(ruta, f'dvd{i}.png')) for i in range(8)]
    return images

def convert_images(images):
     
    return [image.convert() for image in images]


def choose_new_image(current_image, images):
    # Filtrar la lista de imágenes para excluir la imagen actual
    available_images = [img for img in images if img != current_image]
    # Seleccionar aleatoriamente de las imágenes restantes

    return random.choice(available_images)

def toggle_fullscreen(screen, fullscreen):
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("DVD Logo")
    return screen

def dvd_simulation(images ):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pantalla_completa= True
    info = pygame.display.Info()
    window_width = info.current_w
    window_height = info.current_h
    sumax= True
    sumay= True

    # Convert images after video mode is set
    images = convert_images(images)

    clock = pygame.time.Clock()
    

    
    move_x, move_y = 1, 1
    #current_image = images[0]
    current_image=random.choice(images)
    image_width, image_height = current_image.get_size()
    x = random.randint(0, window_width-image_width)
    y = random.randint(0, window_height-image_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    running = False
                if event.key == pygame.K_f:
                    # Si se presiona la tecla "f", alternamos entre pantalla completa y ventana
                    pantalla_completa = not pantalla_completa
                    toggle_fullscreen(screen, pantalla_completa)
                    info = pygame.display.Info()
                    window_width = info.current_w
                    window_height = info.current_h
                    x = random.randint(0, window_width-image_width)
                    y = random.randint(0, window_height-image_height)
                    

        x += move_x
        y += move_y

        


        if (x<0): 
            sumax=True
            current_image = choose_new_image(current_image, images)
        if (x+image_width>window_width): 
            sumax=False
            current_image = choose_new_image(current_image, images)
        if(y<0):
            sumay=True
            current_image = choose_new_image(current_image, images)
        if(y+image_height>window_height):
            sumay=False
            current_image = choose_new_image(current_image, images)
         
        if (sumax): 
            move_x=1
        if(sumax==False):
            move_x=-1
        if (sumay):
           move_y=1
        if (sumay==False):
            move_y=-1
 

        screen.fill((0, 0, 0))
        screen.blit(current_image, (x, y))
        pygame.display.flip()
        clock.tick(150)
        

    pygame.quit()

images = load_images()
dvd_simulation(images)
