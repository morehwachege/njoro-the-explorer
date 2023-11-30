import pygame 
from .player import Player
from .cloud import Cloud
from .fruits import Apple
from .enemies import Stump, Hawk
import sys
import time
from .collisions import detect_collision

class GameState:
    def __init__(self, screen, WINDOW_WIDTH, WINDOW_HEIGHT, FPS):
        self.state = 'intro'
        self.screen = screen
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        # background
        self.bg = pygame.image.load('assets/images/jungle.jpg')
        self.bg = pygame.transform.scale(self.bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # add clouds
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1500)
        self.clouds = pygame.sprite.Group()
     
        # add stumps
        self.ADDSTUMP = pygame.USEREVENT + 3
        stump_time = 5000
        pygame.time.set_timer(self.ADDSTUMP, stump_time)
        self.stumps = pygame.sprite.Group()

        # add apples
        self.ADDAPPLE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDAPPLE, 3500)
        self.apples = pygame.sprite.Group()


        # add hawks
        self.ADDHAWK = pygame.USEREVENT + 5
        pygame.time.set_timer(self.ADDHAWK, 2000)
        self.hawks = pygame.sprite.Group()

        self.gravity = 2
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(300, 100, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.all_sprites.add(self.player)
        self.FPS = FPS
        self.i = 0

        # for the timer
        self.start_time = pygame.time.get_ticks() 
        self.elapsed_time = 0
        self.paused_time = 0

    def intro(self):
            "Intro screen"
            intro_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(intro_surface, (7, 0, 82, 20), [0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
            njoro_img = pygame.transform.scale(pygame.image.load('./assets/images/hyena.png').convert_alpha(), (800, 600))
            self.screen.blit(njoro_img, (400, 170))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if play.collidepoint(event.pos):
                #         self.state = "main_game"

            self.screen.blit(intro_surface, (0, 0))
            pygame.display.flip()


    def main_game(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (self.i, 0))
        self.screen.blit(self.bg, (self.WINDOW_WIDTH + self.i, 0))
        if (self.i ==- self.WINDOW_WIDTH):
            self.screen.blit(self.bg,(self.WINDOW_WIDTH + self.i,0))
            self.i = 0
        self.i -= 4
        self.player.animate()
        # end run regardless


        keys = pygame.key.get_pressed()
        collided_stumps = pygame.sprite.spritecollide(self.player, self.stumps, dokill=False)
        if collided_stumps:
            if pygame.sprite.spritecollide(self.player, self.stumps, dokill=False, collided=pygame.sprite.collide_mask):
                self.state = "crashed"
        else:
            pass

        collided_apples = pygame.sprite.spritecollide(self.player, self.apples, dokill=False)
        if collided_apples:
            if pygame.sprite.spritecollide(self.player, self.apples, dokill=True, collided=pygame.sprite.collide_mask):
                pass
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == self.ADDSTUMP:
                new_stump = Stump(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                self.stumps.add(new_stump)
                self.all_sprites.add(new_stump)

            if event.type == self.ADDCLOUD:
                new_cloud = Cloud(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                self.clouds.add(new_cloud)
                self.all_sprites.add(new_cloud)

            if event.type == self.ADDAPPLE:
                new_apple = Apple(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                self.apples.add(new_apple)
                self.all_sprites.add(new_apple)
            
            if event.type == self.ADDHAWK:
                new_hawk = Hawk(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
                self.hawks.add(new_hawk)
                self.all_sprites.add(new_hawk)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == "main_game":
                        self.state = "paused"
        self.update_timer()
        self.draw_timer()
        self.player.move()
        self.player.jump(self.gravity)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        pygame.display.update()

    def game_paused(self, font):
        " Draw Pause Screen"
        pause_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, (0, 0, 0, 20), [0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        pygame.draw.rect(pause_surface, 'gray', [500, 150, 600, 50], 0, 10)
        save = pygame.draw.rect(pause_surface, 'dark green', [500, 400, 250, 60], 0, 15)
        quit_game = pygame.draw.rect(pause_surface, 'dark red', [850, 400, 250, 60], 0, 15)
        play = pygame.draw.rect(pause_surface, 'lime', [500, 500, 600, 60], 0, 15)

        pause_surface.blit(font.render('Game Paused: Space bar to resume', True, 'black'), (570, 160)) 
        pause_surface.blit(font.render('Save', True, 'black'), (600, 415))
        pause_surface.blit(font.render('Quit', True, 'white'), (950, 415))
        pause_surface.blit(font.render('Play', True, 'black'), (770, 515))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == "paused":
                        self.state = "main_game"
                        self.paused_time = pygame.time.get_ticks()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.collidepoint(event.pos):
                    self.state = "main_game"

        self.screen.blit(pause_surface, (0, 0))
        pygame.display.update()

        return play

    def crashed(self, font):
        "Happens when player collides with enemy sprite"
        crash_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.rect(crash_surface, (0, 0, 0, 20), [0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT])
        message = pygame.draw.rect(crash_surface, 'gray', [500, 150, 600, 50], 0, 10)
        crash_surface.blit(font.render('You crashed! Click reload to try again', True, 'black'), (550, 162))

        w = 200
        h = 200
        # crash_surface.blit 
        reload_img = pygame.transform.scale(pygame.image.load('./assets/images/reload.png'), (w, h))
        replay = pygame.draw.rect(crash_surface, 'orange', [650, 500, 200, 60], 0, 15)
        crash_surface.blit(font.render('Replay', True, 'black'), (700, 515))
        self.screen.blit(crash_surface, (0, 0))
        # reload image
        self.screen.blit(reload_img, ((self.WINDOW_WIDTH / 2) - reload_img.get_width(), (self.WINDOW_HEIGHT / 2) - reload_img.get_height()))
        pygame.display.update()
        
        
        return replay

    def update_timer(self):
        """ Calculate elapsed time in seconds """
        current_time = pygame.time.get_ticks()
        if self.state == "main_game":
            self.elapsed_time = (current_time - (self.paused_time - self.start_time )) // 1000  # Convert to seconds
        # else:if self.state == "main_game":
            self.elapsed_time = (current_time - (self.paused_time - self.start_time )) // 1000  # Convert to seconds
        # else:
        #     self.elapsed_time = (current_time - self.paused_time) // 1000


    def draw_timer(self):
        """Format the time """
        hours = self.elapsed_time // 3600
        minutes = (self.elapsed_time % 3600) // 60
        seconds = self.elapsed_time % 60
        time_str = f"{hours:02d}hrs:{minutes:02d}mins:{seconds:02d}s"
        font = pygame.font.Font(None, 36)
        text = font.render(time_str, True, (255, 255, 255))

        text_rect = text.get_rect(left=10, top=10)
        self.screen.blit(text, text_rect)

    def state_manager(self, font):
        if self.state == "intro":
            self.intro()
            pygame.time.delay(000)
            self.state = "main_game"
            
        elif self.state == "main_game":
            self.main_game()
        elif self.state == "paused":
            self.game_paused(font)
        elif self.state == "crashed":
            self.crashed(font)
