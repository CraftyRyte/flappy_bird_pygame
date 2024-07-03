import pygame as pyg
import sys

pyg.init()

# Dimensions and setup
dimensions = [600, 700]
screen = pyg.display.set_mode(dimensions)
pyg.display.set_caption("Flappy Bird")

# Loop and relvars
clock = pyg.time.Clock()
fps = 60
is_running = True

while is_running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            is_running = False
    # Logic
    # Drawing
    screen.fill((255, 255, 255))
    
    # Updates
    pyg.display.update() 
    pyg.display.flip()
            
pyg.quit()
sys.exit()
