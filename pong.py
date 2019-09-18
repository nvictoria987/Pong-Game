import pygame, sys
from pygame.locals import *

pygame.init()

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 50

#images
background_image= pygame.image.load('background.png')
paddle_image=pygame.image.load('paddle.png')
point_sound=pygame.mixer.Sound('point.wav')

#paddlstretched=pygame.transform.scale(paddle_image, (PADDLELENGTH,PADDLEEDGE))


#Global Variables
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICK=10
PADDLELENGTH=60
PADDLEEDGE=10
ai_speed= 5

paddlestretched=pygame.transform.scale(paddle_image, (PADDLELENGTH,PADDLEEDGE))
paddlestretched2=pygame.transform.scale(paddle_image, (PADDLEEDGE,PADDLELENGTH))

#COLORS
TEAL=(0,128,128)
PURPLE=(128,0,128)
WHITE=(255,255,255)
BLACK=(0,0,0)




def paddle(paddle, color):
    if paddle.bottom> WINDOWHEIGHT-LINETHICK:
        paddle.bottom= WINDOWHEIGHT-LINETHICK
    elif paddle.top< LINETHICK:
        paddle.top=LINETHICK

    pygame.draw.rect(DISPLAYSURF,color, paddle )

def verticalpaddle (paddle, color):
    if paddle.left > WINDOWHEIGHT - LINETHICK:
        paddle.left = WINDOWHEIGHT - LINETHICK
    elif paddle.right < LINETHICK:
        paddle.right = LINETHICK
    pygame.draw.rect(DISPLAYSURF, color, paddle)



def background():
    # background
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background_image,[0,0])
    for i in range(0,WINDOWHEIGHT,15):
        pygame.draw.line(DISPLAYSURF, BLACK, (WINDOWWIDTH/2,(i-5)*3+5), ((WINDOWWIDTH/2), i*3), int(LINETHICK / 2))





#Main function
def main():
    pygame.init()
    global DISPLAYSURF
    global bally, ballx

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pong')

    ai_speed = 2

    #STARTING POSITONS
    computer= (WINDOWHEIGHT-PADDLELENGTH) /2
    user= (WINDOWHEIGHT-PADDLELENGTH) /2
    computer2=(WINDOWHEIGHT-PADDLEEDGE) -LINETHICK
    user2= (WINDOWHEIGHT-PADDLEEDGE) -LINETHICK
    computer3 = LINETHICK
    user3 =  LINETHICK

    #CREATING THE SHAPES
    computerpaddle= pygame.Rect(PADDLEEDGE, computer, LINETHICK, PADDLELENGTH)
    userpaddle=pygame.Rect(WINDOWWIDTH-PADDLEEDGE-LINETHICK, user, LINETHICK, PADDLELENGTH)
    computerpaddle2 = pygame.Rect(PADDLELENGTH, computer2, PADDLELENGTH, PADDLEEDGE)
    userpaddle2 = pygame.Rect(WINDOWHEIGHT - PADDLELENGTH - LINETHICK, user2, PADDLELENGTH, PADDLEEDGE)
    computerpaddle3 = pygame.Rect(PADDLELENGTH, computer3, PADDLELENGTH, PADDLEEDGE)
    userpaddle3 = pygame.Rect(WINDOWHEIGHT - PADDLELENGTH - LINETHICK, user3, PADDLELENGTH, PADDLEEDGE)

    moveleft = False
    moveright = False
    moveup = False
    movedown = False

    ballx = int(WINDOWWIDTH / 2 - LINETHICK / 2)
    bally = int(WINDOWHEIGHT / 2 - LINETHICK / 2)

    ballDirX=-1
    ballDiry= 0

    scoreforcomp=0
    scoreforuser=0

    font = pygame.font.Font(pygame.font.get_default_font(), 25)
    score_comp = font.render(str(scoreforcomp), False, BLACK)
    score_user = font.render(str(scoreforuser), False, BLACK)

    background()
    paddle(computerpaddle, TEAL)
    paddle(userpaddle, PURPLE)
    verticalpaddle(computerpaddle2, TEAL)
    verticalpaddle(userpaddle2, PURPLE)
    verticalpaddle(computerpaddle3, TEAL)
    verticalpaddle(userpaddle3, PURPLE)
    DISPLAYSURF.blit(paddlestretched2, userpaddle)
    DISPLAYSURF.blit(paddlestretched, userpaddle2)
    DISPLAYSURF.blit(paddlestretched, userpaddle3)
    DISPLAYSURF.blit(paddlestretched2, computerpaddle)
    DISPLAYSURF.blit(paddlestretched, computerpaddle2)
    DISPLAYSURF.blit(paddlestretched, computerpaddle3)

    ball=pygame.draw.circle(DISPLAYSURF, PURPLE, (ballx, bally), 15, 0)

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveup=True
                    movedown=False

                elif event.key == K_DOWN:
                    movedown= True
                    moveup=False
                elif event.key == K_LEFT:
                    moveleft=True
                    moveright= False
                elif event.key == K_RIGHT:
                    moveright=True
                    moveleft-False

            elif event.type == KEYUP:
                if event.key == K_UP:
                   moveup=False

                elif event.key == K_DOWN:
                   movedown=False
                elif event.key == K_LEFT:
                    moveleft=False
                elif event.key == K_RIGHT:
                    moveright=False


        #ballmoving(ballDirX, ballDiry)

        ballx += ballDirX
        bally += ballDiry
        if movedown and userpaddle.bottom < WINDOWHEIGHT:
            userpaddle.top += ai_speed
        if moveup and userpaddle.top > 0:
            userpaddle.top -= ai_speed
        if moveleft and userpaddle2.left and userpaddle3.left >WINDOWWIDTH/2:
            userpaddle2.left -= ai_speed
            userpaddle3.left -=ai_speed
        if moveright and userpaddle2.right and userpaddle3.right < WINDOWWIDTH :
            userpaddle2.right +=ai_speed
            userpaddle3.right += ai_speed


        if userpaddle.collidepoint(ballx,bally):
            ballDirX-=1
            ballDiry-=1
        if userpaddle2.collidepoint(ballx,bally):
            ballDirX+=1
            ballDiry-=1
        if userpaddle3.collidepoint(ballx,bally):
            ballDirX+=1
            ballDiry+=1
        if computerpaddle.collidepoint(ballx,bally):
            ballDirX+=1
            ballDiry+=1
        if computerpaddle2.collidepoint(ballx, bally):
            ballDirX += 1
            ballDiry -= 1
        if computerpaddle3.collidepoint(ballx,bally):
            ballDirX-=1
            ballDiry+=1


        if ballx> WINDOWWIDTH:
            ballx = int(WINDOWWIDTH/2)
            bally = int(WINDOWHEIGHT/2)
            scoreforcomp+=1
            point_sound.play()
        if bally<0 and ballx < WINDOWWIDTH/2:
            ballx = int(WINDOWWIDTH / 2)
            bally = int(WINDOWHEIGHT / 2)
            scoreforuser+=1
            point_sound.play()
        elif bally<0 and ballx >WINDOWWIDTH/2:
            ballx = int(WINDOWWIDTH / 2)
            bally = int(WINDOWHEIGHT / 2)
            scoreforcomp += 1
            point_sound.play()
        if bally>WINDOWHEIGHT and ballx< WINDOWWIDTH/2:
            ballx = int(WINDOWWIDTH / 2)
            bally = int(WINDOWHEIGHT / 2)
            scoreforuser += 1
        elif bally>WINDOWHEIGHT and ballx>WINDOWWIDTH/2:
            ballx = int(WINDOWWIDTH / 2)
            bally = int(WINDOWHEIGHT / 2)
            scoreforcomp += 1
            point_sound.play()
        if ballx<0:
            ballx = int(WINDOWWIDTH / 2)
            bally = int(WINDOWHEIGHT / 2)
            scoreforuser+=1
            point_sound.play()
        if bally <= computerpaddle.centery :
            computerpaddle.centery-=ai_speed
        elif bally >= computerpaddle2.centery:
            computerpaddle.centery +=ai_speed
        if ballx <= computerpaddle2.left:
            computerpaddle2.centerx -=ai_speed
            computerpaddle3.centerx -= ai_speed
        if ballx >=computerpaddle2.right and computerpaddle2.right < WINDOWWIDTH/2 and computerpaddle3.right< WINDOWWIDTH/2:
            computerpaddle2.centerx +=ai_speed
            computerpaddle3.centerx+=ai_speed






        background()

        paddle(computerpaddle, TEAL)
        paddle(userpaddle, PURPLE)
        verticalpaddle(computerpaddle2, TEAL)
        verticalpaddle(userpaddle2, PURPLE)
        verticalpaddle(computerpaddle3, TEAL)
        verticalpaddle(userpaddle3, PURPLE)
        DISPLAYSURF.blit(paddlestretched2, userpaddle)
        DISPLAYSURF.blit(paddlestretched, userpaddle2)
        DISPLAYSURF.blit(paddlestretched, userpaddle3)
        DISPLAYSURF.blit(paddlestretched2, computerpaddle)
        DISPLAYSURF.blit(paddlestretched, computerpaddle2)
        DISPLAYSURF.blit(paddlestretched, computerpaddle3)
        score_comp = font.render( str(scoreforcomp), False, BLACK)
        DISPLAYSURF.blit(score_comp, ((150) , (WINDOWHEIGHT / 2)))
        score_user=font.render(str(scoreforuser),False,BLACK)
        DISPLAYSURF.blit(score_user,(250,(WINDOWHEIGHT/2)))
        ball = pygame.draw.circle(DISPLAYSURF, PURPLE, (ballx, bally), 15, 0)





        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()