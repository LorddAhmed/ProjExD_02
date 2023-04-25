import random
import sys

import pygame as pg
import time

delta = {
    pg.K_UP : (0,-1),
    pg.K_DOWN: (0,+1),
    pg.K_LEFT: (-1,0),
    pg.K_RIGHT:(+1,0)
        }




def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect ) -> tuple[bool,bool]:
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_damaged = pg.image.load("ex02/fig/8.png")
    kk_img_right = pg.image.load("ex02/fig/3.png")
    kk_img_left = pg.transform.flip(kk_img_right, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400
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
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        if check_bound(screen.get_rect(),kk_rct) != (True,True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0],-mv[1])
        # Set kk_image image based on direction
        if vx > 0:
            kk_img = kk_img_right
        else:
            kk_img = kk_img_left
        # Increase size and speed of bomb over time
        if tmr % 1000 == 0:
            bb_rct.inflate_ip(5, 5)
            vx, vy = vx * 1.2, vy * 1.2
        
        if kk_rct.colliderect(bb_rct):
            kk_img = kk_img_damaged
            screen.blit(kk_img, kk_rct)
            pg.display.update()
            time.sleep(3)
            return

        screen.blit(kk_img, kk_rct) # 4 
        bb_rct.move_ip(vx,vy)
        yoko, tate =check_bound(screen.get_rect(),bb_rct)
        if not yoko: 
            vx*= -1
        if not tate:
            vy*=-1
        screen.blit(bomb_img,bb_rct)
        


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()