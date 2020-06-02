import pygame
from pygame.locals import *
import random
import time

pygame.init()
clock= pygame.time.Clock()
info = pygame.display.Info()
width, height =info.current_w, info.current_h

print("Width/Height:", width, height)

resolution= ( 930, 580)
window_surface= pygame.display.set_mode(resolution)
pygame.display.set_caption("pING_pONG")

violet_clair=(200,200,252)
cyan=(150,250,200)
violet= (50,50,183)
cyan_clair= (100,150,100)
orange=(207,75,20)
blanc= (230,230,230)
bleu=(10,10,254)
black=(0,0,0)
blacky=(55,165,75)
red=(233,0,0)
bleu=(200,200,150)
jaune= (240,230,50)


positif=random.randint(0,1)
positif= True
#positif=random.randint(0,1)
#positif=bool(positif) # ce qui veut dire que la balle se deplacer vers la droite de l'écran
x,y=465,300 # coordonnées départ pour la balle

z,w=54,250 # pour l'utilisateur
r,s= 866,250 #pour le robot

haut = bas = 0

# Les formes

arial= pygame.font.SysFont( 'arial', 50,True)
limite= pygame.Rect(40,40,850,520)
obstacle1= pygame.Rect(42,42,10,518)
osbtacle2=pygame.Rect(878,42,10,518)
demie_terrain1= pygame.Rect(65,42, 400,518)
demie_terrain2= pygame.Rect(452,42,413,518)
player1=pygame.Rect(z,w,10,100)
robots=pygame.Rect(r,s,10,100)


# def main():
#     open = True
#     while open:
#         loop()

# def loop():
#     events()
#     update()
#     show()



def affichage():
    window_surface.fill(black)
    pygame.draw.rect(window_surface,orange,limite,4)
    pygame.draw.rect(window_surface, violet,obstacle1)
    pygame.draw.rect(window_surface,cyan, osbtacle2)
    pygame.draw.rect(window_surface,blacky, player1)
    pygame.draw.rect(window_surface,blanc, robots)
    pygame.draw.rect(window_surface,cyan_clair,demie_terrain2)
    pygame.draw.rect(window_surface,violet_clair,demie_terrain1)
    pygame.draw.circle(window_surface,bleu, [465,300], 50,3 )
    pygame.draw.circle(window_surface,bleu, [465,300], 100,3 )
    pygame.draw.circle(window_surface,bleu, [465,300], 150,3 )
    pygame.draw.circle(window_surface,bleu,[465,300] ,10 )
    pygame.draw.circle(window_surface,red,[x,y],10 )
    pygame.display.flip()


fps_sec=200 # fps pour la boucle secondaire
fps_prin=400 # fps pour la boucle principal


liste_rebond=list()
libi=list()

speed = 5
dt = 0.01


ouvert=True
while ouvert:
    #Evenement pvy = player velocity y
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                ouvert=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP or event.key== pygame.K_LEFT:
                pvy = speed
            elif event.key==pygame.K_DOWN or event.key== pygame.K_RIGHT:
                pvy = -speed
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key== pygame.K_LEFT:
                pvy = 0
            elif event.key==pygame.K_DOWN or event.key== pygame.K_RIGHT:
                pvy = 0

    #Update
    # paddle1 = Paddle()
    py += pvy
    py = min(py, 40)
    py = max(py, 0)

    z = px; w = py

    x += vitesse_x * dt
    y += vitesse_y * dt

    friction = 0

    if x<52:
        x = 52
        vitesse_x*=-1
    elif x>868 :
        x = 868
        vitesse_x*=-1
    if y<52:
        y = 0
        vitesse_y*=1
    elif y<520:
        y = 0
        vitesse_y*=1

    
    

    #Affichage
    affichage()








ouvert=True
while ouvert:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                ouvert=False

    vitesse_x=random.randint(1,4)
    vitesse_y=random.randint(1,4)

    print(vitesse_x,vitesse_y)

    clock.tick(fps_prin)
    if positif :
        while not x>868 and ( not r-10<x<r+20 or not s-10<y<s+120 ):
            for event in pygame.event.get():
                if  event.type==pygame.KEYDOWN: # Voir les deux images.
                    if event.key==pygame.K_p:
                        ouvert=False
                    elif event.key==pygame.K_UP or event.key== pygame.K_LEFT:
                        bouge=True
                        # pour que ca bouge en continue
                        while bouge:
                            player1=pygame.Rect(z,w,10,110)
                            affichage()
                            x+=vitesse_x
                            y+= vitesse_y
                            if w<=40:
                                w+=0
                            else:
                                w-=5
                            print("")
                            # pour pouvoir arreter le machin
                            for event in pygame.event.get():
                                if event.type== pygame.KEYUP:
                                    if event.key== pygame.K_UP or event.key==pygame.K_LEFT:
                                        bouge=False
                            clock.tick(fps_sec)
                            print(clock.get_fps())
                            if  x>868 or (  r-10<x<r+20 and  s-10<y<s+120 ):
                                break
                            clock.tick(fps_sec)
                            print(clock.get_fps())

                            if y<=50:
                                y+=vitesse_y
                                x+=vitesse_x
                            elif y>=550:
                                y-=vitesse_y
                                x+=vitesse_x
                                liste_rebond.append(vitesse_y)
                                liste_rebond.append(vitesse_x)
                            else:
                                if len(liste_rebond)==0:
                                    x+=vitesse_x
                                    y+= vitesse_y
                                    print('ici')
                                else:
                                    print(liste_rebond)
                                    y-=liste_rebond[0]
                                    x+=liste_rebond[1]
                                    if x>=r or y<=50:
                                        liste_rebond.clear()
                                        print('nada')


                    elif event.key== K_DOWN or event.key== pygame.K_RIGHT :
                        bouge=True
                        # pour que ca bouge en continue
                        while bouge:

                            player1=pygame.Rect(z,w,10,110)
                            affichage()
                            x+=vitesse_x
                            y+= vitesse_y
                            if w>=450:
                                w+=0
                            else:
                                w+=5
                            print("descend")
                            pygame.display.flip()
                            # pour pouvoir arreter le machin
                            for event in pygame.event.get():
                                if event.type== pygame.KEYUP:
                                    if event.key== pygame.K_DOWN or event.key==pygame.K_RIGHT:
                                        bouge=False

                            if  x>868 or (  r-10<x<r+20 and  s-10<y<s+120 ):
                                break
                            clock.tick(fps_sec)
                            print(clock.get_fps())
                            if y<=50:
                                y+=vitesse_y
                                x+=vitesse_x
                            elif y>=550:
                                y-=vitesse_y
                                x+=vitesse_x
                                liste_rebond.append(vitesse_y)
                                liste_rebond.append(vitesse_x)
                            else:
                                if len(liste_rebond)==0:
                                    x+=vitesse_x
                                    y+= vitesse_y
                                    print('ici')
                                else:
                                    print(liste_rebond)
                                    y-=liste_rebond[0]
                                    x+=liste_rebond[1]
                                    if x>=r or y<=50:
                                        liste_rebond.clear()
                                        print('nada')

            if y<=50:
                y+=vitesse_y
                x+=vitesse_x
            elif y>=550:
                print('sup')
                y-=vitesse_y
                x+=vitesse_x
                liste_rebond.append(vitesse_y)
                liste_rebond.append(vitesse_x)
            else:
                if len(liste_rebond)==0:
                    x+=vitesse_x
                    y+= vitesse_y
                    print('ici')
                else:
                    print(liste_rebond)
                    y-=liste_rebond[0]
                    x+=liste_rebond[1]
                    if x>=r or y<=50:
                        liste_rebond.clear()
                        print('nada')

            affichage()
            clock.tick(fps_prin)
            #print(clock.get_fps())
        pygame.draw.circle(window_surface,jaune,[x,y],10 )
        pygame.display.flip()
        positif =False
    else:
        while not x<60 and ( not z-10<x<z+20 or not w-10<y<w+120 ):
            for event in pygame.event.get():
                if  event.type==pygame.KEYDOWN: # Voir les deux images.
                    if event.key==pygame.K_p:
                        ouvert=False
                    elif event.key==pygame.K_UP or event.key== pygame.K_LEFT:

                        bouge=True
                        # pour que ca bouge en continue
                        while bouge:
                            player1=pygame.Rect(z,w,10,100)
                            affichage()
                            x-=vitesse_x
                            y-= vitesse_y
                            if w<=40:
                                w+=0
                            else:
                                w-=5
                            print("monte")
                            pygame.display.flip()
                            # pour pouvoir arreter le machin
                            for event in pygame.event.get():
                                if event.type== pygame.KEYUP:
                                    if event.key== pygame.K_UP or event.key==pygame.K_LEFT:
                                        bouge=False


                            if  x<60 or (  z-10<x<z+20 and w-10<y<w+120 ):
                                break

                            clock.tick(fps_sec)
                            print(clock.get_fps())

                            if y<=50:
                                    y+=vitesse_y
                                    x-=vitesse_x
                            elif y>=550:
                                    y-=vitesse_y
                                    x-=vitesse_x
                                    liste_rebond.append(vitesse_y)
                                    liste_rebond.append(vitesse_x)
                            else:
                                if len(liste_rebond)==0:
                                        x-=vitesse_x
                                        y+= vitesse_y
                                        print('ici')
                                else:
                                    print(liste_rebond)
                                    y-=liste_rebond[0]
                                    x-=liste_rebond[1]
                                    if x>=r or y<=50:
                                        liste_rebond.clear()
                                        print('nada')
                                        time.sleep(1000)

                    elif event.key== K_DOWN or event.key== pygame.K_RIGHT :
                        bouge=True
                        # pour que ca bouge en continue
                        while bouge:

                            player1=pygame.Rect(z,w,10,100)
                            affichage()
                            x-=vitesse_x
                            y-= vitesse_y
                            if w>=450:
                                w+=0
                            else:
                                w+=5
                            print("descend")
                            pygame.display.flip()
                            # pour pouvoir arreter le machin
                            for event in pygame.event.get():
                                if event.type== pygame.KEYUP:
                                    if event.key== pygame.K_DOWN or event.key==pygame.K_RIGHT:
                                        bouge=False

                            if  x<60 or (  z-10<x<z+20 and w-10<y<w+120 ):
                                    break
                            clock.tick(fps_sec)
                            print(clock.get_fps())

                            if y<=50:
                                    y+=vitesse_y
                                    x-=vitesse_x
                            elif y>=550:
                                    y-=vitesse_y
                                    x-=vitesse_x
                                    liste_rebond.append(vitesse_y)
                                    liste_rebond.append(vitesse_x)
                            else:
                                if len(liste_rebond)==0:
                                        x-=vitesse_x
                                        y+= vitesse_y
                                        print('ici')
                                else:
                                    print(liste_rebond)
                                    y-=liste_rebond[0]
                                    x-=liste_rebond[1]
                                    if x>=r or y<=50:
                                        liste_rebond.clear()
                                        print('nada')
            if y<=50:
                y+=vitesse_y
                x-=vitesse_x
            elif y>=550:
                y-=vitesse_y
                x-=vitesse_x
                liste_rebond.append(vitesse_y)
                liste_rebond.append(vitesse_x)
            else:
                if len(liste_rebond)==0:
                    x-=vitesse_x
                    y+= vitesse_y
                    print('boooo')
                else:
                    print(liste_rebond)
                    y-=vitesse_y
                    x+=vitesse_x
                    if x>=r or y<=50:
                        liste_rebond.clear()
                        print( "ECRASEEEEEEEEEEEEEEEEEEE")


            clock.tick(fps_prin)
            #print(clock.get_fps())
            affichage()

        pygame.draw.circle(window_surface,jaune,[x,y],10 )
        pygame.display.flip()

        positif =True

