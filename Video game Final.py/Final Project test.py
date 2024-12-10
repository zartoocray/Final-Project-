import pygame
import os 

pygame.init()

# Getting object to move  
BACKGROUND_HEIGHT = 600 
BACKGROUND_WIDTH = 1100
BACKGROUND = pygame.display.set_mode((BACKGROUND_WIDTH,BACKGROUND_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/Box","Boxrun1.png")),
           pygame.image.load(os.path.join("Assets/Box","BoxRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("BoxJump.png"))]
SLIDING = [pygame.image.load(os.path.join("Assets/Box","Boxrun1.png")),
          pygame.image.load(os.path.join("Assets/Box","Boxrun2.png"))]
SMALL_MONSTER = [pygame.image.load(os.path.join("Assets/Monster","SmallMonster1.png")),
                pygame.image.load(os.path.join("Assets/Monster","SmallMonster2.png")),
                pygame.image.load(os.path.join("Assets/Monster","SmallMonster3.png"))]
LARGE_MONSTER = [pygame.image.load(os.path.join("Assets/Monster","SmallMonster1.png")),
                pygame.image.load(os.path.join("Assets/Monster","SmallMonster2.png")),
                pygame.image.load(os.path.join("Assets/Monster","SmallMonster3.png"))]
GHOST = [pygame.image.load(os.path.join("Assets/Ghost","Ghost1.png")),
        pygame.image.load(os.path.join("Assets/Ghost","Ghost2.png"))]
CLOUD = [pygame.image.load(os.path.join("Assets/Cloud","Cloud.png"))]

BG = pygame.image.load("Assets/Other","Track.png")

class Box:
        X_POS = 80
        Y_POS = 310
        Y_POS_SLIDE = 340
        JUMP_VEL = 8.5

        def _init_(self):
                self.slide_img = SLIDING 
                self.run_img = RUNNING 
                self.run_img = JUMPING 

                self.box_slide = False 
                self.box_run = False 
                self.box_jump = True 

                self.step_index = 0
                self.jump_vel = self.JUMP_VEL
                self.image = self.run_img(0)
                self.box_rect = self.image.get_rect()
                self.box_rect.x = self.X_POS 
                self.box_rect.y = self.Y_POS  

        def update(self,userInput):
                if self.box_slide:
                        self.duck()
                if self.box_run:
                        self.run()
                if self.box_jump:
                        self.jump()
                
                if self.step_index >= 10:
                        self.step_index = 0 

                if userInput[pygame.K_UP] and not self.box_jump:
                        self.box_slide = False 
                        self.box_run = False 
                        self.box_jump = True 
                elif userInput[pygame.K_DOWN] and not self.box_jump:
                        self.box_slide = True
                        self.box_run = False 
                        self.box_jump = False 
                elif not (self.firl_jump or userInput[pygame.K_DOWN]):
                         self.box_slide = False 
                         self.box_run = True  
                         self.box_jump = False  
                
                def slide(self):
                        self.image = self.run_img(self.step_index // 5)
                        self.box_rect = self.image.get_rect()
                        self.box_rect.x = self.X_POS 
                        self.box_rect.y = self.Y_POS_SLIDE
                        self.step_index += 1 
                def run(self):
                        self.image = self.run_img(self.step_index // 5)
                        self.box_rect = self.image.get_rect()
                        self.box_rect.x = self.X_POS 
                        self.box_rect.y = self.Y_POS 
                        self.step_index += 1 
                    
        
                def jump(self):
                        self.image = self.jump_img
                        if self.box_jump:
                                self.box_rect.y -= self.jump_vel * 4 
                                self.jump_vel -= 0.8
                        if self.jump_vel < - self.JUMP_VEL:
                                self.box_jump = False 
                                self.jump_vel = self.JUMP_VEL 
                
                def draw(self, SCREEN):
                        SCREEN.blit(self.image,(self.box_rect.x, self.box_rect.y))



def main():
        run = True 
        clock = pygame.time.Clock()
        player = Box()

        while run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                          run = False
                BACKGROUND.fill((255,255,255))
                userInput = pygame.key.get_pressed()

                player.draw(BACKGROUND)
                player.update(userInput)

                clock.ticK(30)
                pygame.display.update()





main()
        
