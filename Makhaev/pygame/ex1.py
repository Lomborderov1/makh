from pygame import *

display.set_caption("Моя программа!")
window = display.set_mode((500, 500))
background = transform.scale(image.load('as.jpeg'),(500,500))

run = True
while run:
    time.delay(50)
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()