

import pygame

import random
import threading
import time



class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread = threading.Thread(target= self.__setInterval  )
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime += self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()


# # # # # # # # # # # # # # # # # # # #
class MyGame :
# # # # # # # # # # # # # # # # # # # #
    t = pygame.init()
    displayWidth = 800
    displayHeight = 600
    timer = None
    ourScreen =  pygame.display.set_mode((displayWidth ,displayHeight  ))
    pygame.display.set_caption('파이게임')
    finish = False
    # colorBlue  = True
    # myImg = pygame.image.load('sulto.png')



    #
    life = 10;
    score = 0;
    #


    myfont = pygame.font.SysFont("monospace", 28)


    def myImgDraw(self,x,y) :
        self.ourScreen.blit(self.myImg,(x,y))

    # imgPositionX = displayWidth * 0.5
    # imgPositionY = displayHeight * 0.5



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def attack(self,x,y):


        pygame.draw.rect(self.ourScreen, (255, 0, 255), pygame.Rect(x-15, y-30, 30, 30))

        self.life -= 1

        # if(self.life ==0) :
        #     self.finish  = True



    #
    def scoreDraw(self):

        scoretext = self.myfont.render("Score = " + str(self.score), 1, (0, 0, 0)   )
        self.ourScreen.blit(scoretext, (self.displayWidth-100, 40))
    #




    #
    def attackedLife(self):
        for i in range(self.life) :
            pygame.draw.rect( self.ourScreen, (255, 0, 0), pygame.Rect(40 * i, 40, 40, 40))

    #


    ddongs = [[1,0],[30,0],[40,0],[100,0],[400,0],[600,0]]

    def ddongMaker(self):

        for i in range(8) :
            newDdong = [random.randrange(40,800-40),0]
            self.ddongs.append( newDdong )

    def ddongDraw(self, x, y):
        pygame.draw.rect(self.ourScreen, (0, 0, 0), pygame.Rect(x, y, 5, 30))

#



    def ddongTimer(self) :
        print('ddong timer')
        self.timer = setInterval(1,self.ddongMaker  )


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


    rect_x= displayWidth/2
    rect_y = displayHeight -60
    clock = pygame.time.Clock()






    #

    def __init__(self) :



        self.ddongTimer()
        while not self.finish :
            for event in pygame.event.get():
                if event.type  == pygame.QUIT :
                    self.finish = True

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE  :
            #     colorBlue = not colorBlue
            # if colorBlue : color = (0,128,255)
            # else : color = (255,255,255)
            pressed=  pygame.key.get_pressed()
            # if pressed[pygame.K_UP] : rect_y = rect_y - 3
            if pressed[pygame.K_RIGHT] and self.rect_x <= self.displayWidth-60  : self.rect_x += 10
            # if pressed[pygame.K_DOWN]: rect_y += 3
            if pressed[pygame.K_LEFT] and self.rect_x >= 0 : self.rect_x -= 10
            #

            self.ourScreen.fill( (255,255,255)  )
            #     화면 업데이트를 한다
            # myImgDraw(rect_x, rect_y)
            # pygame.draw.circle(ourScreen,(0,128,255) , (10,10) ,60 )

            #
            self.attackedLife()
            #


            self.scoreDraw()
            pygame.draw.rect(self.ourScreen, (0, 128, 255), pygame.Rect(self.rect_x, self.rect_y, 60, 60))



            # for idx, ddong in enumerate(self.ddongs) :
            #     self.ddongDraw(ddong[0],ddong[1])
            #
            #     if ddong[1] > self.displayHeight :
            #         del self.ddongs[idx]
            #
            #     if ddong[1] == 0:
            #         ddong[1] += 1
            #     else:
            #         if (ddong[1] < 50):
            #             ddong[1] = ddong[1] + ddong[1] / 10
            #         else:
            #             ddong[1] = ddong[1] + 5
            #


            for idx, ddong in enumerate(self.ddongs)  :


                #
                if ddong[0] >= self.rect_x and ddong[0] <= self.rect_x+60   and ddong[1] > self.displayHeight-65 and ddong[1] <= self.displayHeight-60   :
                    print('d---------' )
                    print(ddong[1])
                    self.attack(ddong[0],ddong[1])

                    del self.ddongs[idx]
                #



                elif ddong[1] > self.displayHeight :
                    del self.ddongs[idx]
                    self.score += 1




                else :
                    self.ddongDraw(ddong[0],ddong[1])
                    if ddong[1] == 0 :
                        ddong[1] += 1
                    else :
                        if(ddong[1] < 50):
                            ddong[1] = ddong[1] + ddong[1]/10
                        else :
                            ddong[1] = ddong[1] + 5







            pygame.display.flip()
            self.clock.tick(1000)

        print(self.ddongs)

        self.timer.cancel()
        pygame.quit()
        quit()

MyGame()