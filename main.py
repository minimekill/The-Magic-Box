# KidsCanCode - Game Development with Pygame video series
# Jumpy! (a platform game) - Part 4
# Video link: https://youtu.be/G8pYfkIajE8
# Jumping

import pygame as pg
import random
from settings import *
from sprites import *
import decision_tree as dt


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.mode = 'decision_tree'

    def new(self):
        # start a new game
        self.im_special = 550

        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.copycat_enemy = Enemy(550, 320, 30, 40)
        self.bigbox_enemy = Enemy(520, 280, 80, 80)
        self.enemies.add(self.copycat_enemy, self.bigbox_enemy)
        self.player = Player(self)
        self.all_sprites.add(self.player, self.copycat_enemy, self.bigbox_enemy)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for enemy in ENEMY_LIST:
            e = Enemy(*enemy)
            self.all_sprites.add(e)
            self.enemies.add(e)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            

    def update(self):
        # Game Loop - Update

        self.all_sprites.update()
        # check if the obstacle is behind the player and then reset it
        if self.im_special <= 0:
            self.im_special = 550
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            enemy_hit = pg.sprite.spritecollide(self.player, self.enemies, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
            if enemy_hit:
                self.player.pos = vec(WIDTH / 4, HEIGHT)
                self.player.vel.y = 0
                self.im_special = 550
                if self.mode is 'decision_tree':
                    dt.change_parameter()

    def events(self):
        if self.mode is 'decision_tree':
            for enemy in self.enemies:
                if dt.to_jump_or_not_to_jump(self.player.pos.x, enemy.rect.x):
                    self.player.jump()
        #self.copycat_enemy.__init__(self.im_special, 320, 30, 40)
        self.bigbox_enemy.__init__(self.im_special, 280, 80, 80)
        self.im_special -= 3
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()



pg.quit()
