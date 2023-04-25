import random
import sys

import pygame as pg

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bomb_img = pg.Surface((20, 20))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_img.set_colorkey((0, 0, 0))
    x,y = random.randint(0,1600), random.randint(0,900)
    vx,vy = +1,+1
    bb_rct = bomb_img.get_rect()
    bb_rct.center = x,y
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bb_rct.move_ip(vx,vy)
        screen.blit(bomb_img,bb_rct)
        draw_sfc = pg.Surface((100,100))
        pg.draw.circle(draw_sfc, (255,0,0), (50,50), 50)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()