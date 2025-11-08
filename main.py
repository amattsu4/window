from pygame import*
init()

window_size = (800, 600)
window = display.set_mode(window_size)
display.set_caption("Завдання")
timer = time.Clock()
FPS = 60
game = True
player = Rect(0, 0, 100, 100)
big_rock = transform.scale(image.load('big_rock.png'),(100,100))#
window.blit
full_g_block = transform.scale(image.load('full_g_block.png'),(500,100))#
full_g_block = transform.scale(image.load('full_g_block.png'),(500,100))#
full_h_block= transform.scale(image.load('full_h_block.png'),(100,300))#
full_h_block= transform.scale(image.load('full_h_block.png'),(100,300))#
little_rock = transform.scale(image.load('little_rock.png'),(400,200))#
while game:
    for e in event.get():
        if e .type == QUIT:
            game = False
    window.fill((0,0,0))
    draw.rect(window,(255, 0, 0), player)
    window.blit(big_rock, (90, 465))#
    window.blit(full_g_block,(-39, 550))
    window.blit(full_g_block,(400, 550))
    window.blit(full_h_block,(700, 300))
    window.blit(full_h_block,(400, 300))
    window.blit(little_rock,(400, 200))
    keys = key.get_pressed()
    if keys[K_w]:
        player.y -=5

    if keys[K_s]:
        player.y +=5

    if keys[K_a]:
        player.x -=5  

    if keys[K_d]:
        player.x +=5

    timer.tick(FPS)
    display.update()
