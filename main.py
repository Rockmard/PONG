from random import randint
import pygame
from pygame.locals import *
from barre import *
from score import *
from balle  import *
from button import *
from shop import *


# Initialisation globale
pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w,info.current_h), FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('LOADING...')
pygame_icon = pygame.image.load('./src/icon.png')
pygame.display.set_icon(pygame_icon)
pygame.key.set_repeat(10,1)
logo = pygame.image.load('./src/logov3.png').convert()
surface_logo = pygame.Surface((168,168))
surface_logo.blit(logo,(0,0))
pygame.mouse.set_visible(False)
# Gestion de l'audio
try :
    audio_device = True
    pygame.mixer.music.load("./src/loading-theme.ogg")
    pygame.mixer.music.set_volume(0.5)
    volume_int = 50
except :
    audio_device = False
    volume_int = '?'
########################


# Gestion du début avec logo
def fade():
    # paramètrage
    fade = pygame.Surface((screen.get_size()[0],screen.get_size()[1]))
    fade.fill((0,0,0))
    font_co = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(40))
    if audio_device : pygame.mixer.music.play()

    # logo + texte
    for alpha in range(300):
        fade.set_alpha(alpha)
        screen.blit(rescale_img(logo,(rescaling_x(logo.get_height()),rescaling_y(logo.get_width()))),((screen.get_size()[0]//2)-rescaling_x(84),(screen.get_size()[1]//2)-rescaling_y(84)))
        text_co  = font_co.render('DEMACIA AND CO.',False,(255,255,255))
        text_co2 = font_co.render('PRESENTS',False,(255,255,255))
        screen.blit(text_co,((screen.get_size()[0]//2)-rescaling_x(250),(screen.get_size()[1]//2)+rescaling_y(100)))
        screen.blit(text_co2,((screen.get_size()[0]//2)-rescaling_x(160),(screen.get_size()[1]//2)+rescaling_y(150)))
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(5)
    # affichage menu + lancement main theme
    pygame.mouse.set_visible(True)
    pygame.display.set_caption('MENU')
    if audio_device : pygame.mixer.music.load("./src/main-theme.ogg")
############################


# Gestion du rescale
def rescaling_x(data):
    if screen.get_size()[0] < 1600 : x = data*(screen.get_size()[0]/1600.0) # weidth too low
    else :                           x = data*(1600.0/screen.get_size()[0]) # weidth too high
    return x

def rescaling_y(data):
    if screen.get_size()[1] < 900  : y = data*(screen.get_size()[1]/900.0)  # height too low
    else :                           y = data*(900.0/screen.get_size()[1])  # height too high
    return y

def rescaling_font(size):
    if screen.get_size()[0] < 1600 : font_size = int(size*screen.get_size()[0]/1600)   # weidth too low
    else :                           font_size = int(size*1600.0/screen.get_size()[0]) # weidth too high
    return font_size

def autoscale(obj,x,y,w,h,sign = ''):
    if len(sign) < 1:
        obj.set_coord((screen.get_size()[0]//2-rescaling_x(w),screen.get_size()[1]-rescaling_y(h)))
        obj.set_taille((rescaling_x(x),rescaling_y(y)))
    else :
        obj.set_coord((screen.get_size()[0]//2+rescaling_x(w),screen.get_size()[1]-rescaling_y(h)))
        obj.set_taille((rescaling_x(x),rescaling_y(y)))

# - Gestion de la redimension
def rescale_img(img,taille):
    t = int(taille[0]) , int(taille[1])
    return pygame.transform.scale(img,t)
####################


'''
# Gestion du fond
bg = pygame.image.load('./src/bg3.jpg').convert()
bg_taille = screen.get_size()

def draw_background():
    screen.blit(rescale_img(bg,bg_taille),(0,0))
#################
'''


# Gestion des barres
barreg  = Barre((30,200),30,300,screen.get_size()[1]-200)
barred  = Barre((30,200),screen.get_size()[0]-60,300,screen.get_size()[1]-200)
barreIA = Barre_IA((30,200),screen.get_size()[0]-60,300,screen.get_size()[1]-200)
barre1  = pygame.Surface(barreg.get_taille())
barre2  = pygame.Surface(barred.get_taille())
barre3  = pygame.Surface(barreIA.get_taille())
barre1.fill((250,250,250))
barre2.fill((250,250,250))
barre3.fill((250,250,250))

def draw_barres(b,b2):
    screen.blit(barre1,pygame.Rect((b[0],b[1]), (30,200)))
    screen.blit(barre2,pygame.Rect((b2[0],b2[1]), (30,200)))

def draw_barres_IA(b,b2):
    screen.blit(barre1,pygame.Rect((b[0],b[1]), (30,200)))
    screen.blit(barre3,pygame.Rect((b2[0],b2[1]), (30,200)))
####################


# Gestion de la balle
su = pygame.Surface((30, 30))
ball  = Ball(10,800,800,su,(screen.get_size()[0], screen.get_size()[1]))
bball = Bill_Ball(10,800,800,su,(screen.get_size()[0], screen.get_size()[1]))

def draw_ball(b) :
    screen.blit(ball.surface,pygame.Rect((b[0],b[1]), (30, 30)))

def draw_bball(b):
    screen.blit(bball.surface,pygame.Rect((b[0],b[1]), (30, 30)))

def hide():
    su.fill((0,0,0))

def show():
    su.fill((255,255,255))
#####################


# Gestion du score
score = Score()
font = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(56))

def draw_score():
    font = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(56))
    score_gauche = str(score.get_score(1))
    score_droit  = str(score.get_score(2))
    textscore_gauche = font.render(score_gauche,False,(255,255,255))
    textscore_droit = font.render(score_droit,False,(255,255,255))
    screen.blit(textscore_gauche,(screen.get_size()[0]//2-156,25))
    screen.blit(textscore_droit,(screen.get_size()[0]//2+100,25))
##################


# Gestion du titre
font_title = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(76))

def draw_title():
    font_title = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(76))
    titre = font_title.render('PONG',False,(255,255,255))
    screen.blit(titre,(screen.get_size()[0]//2-rescaling_x(150),rescaling_y(50)))
##################


# Gestion de l'affichage du volume
font_volume = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(20))

def draw_volume():
    font_volume = pygame.font.Font("src/PKMN RBYGSC.ttf", rescaling_font(20))
    if audio_device : volume_text = font_volume.render(str(volume_int),False,(255,255,255))
    else : volume_text = font_volume.render('?',False,(255,255,255))
    if   volume_int == '?' : screen.blit(volume_text,(screen.get_size()[0]//2-rescaling_x(11),volume.get_coord()[1]+rescaling_y(40)))
    elif volume_int == 100 : screen.blit(volume_text,(screen.get_size()[0]//2-rescaling_x(25),volume.get_coord()[1]+rescaling_y(40)))
    elif volume_int == 0   : screen.blit(volume_text,(screen.get_size()[0]//2-rescaling_x(11),volume.get_coord()[1]+rescaling_y(40)))
    else                   : screen.blit(volume_text,(screen.get_size()[0]//2-rescaling_x(20),volume.get_coord()[1]+rescaling_y(40)))
##################


# Gestion des boutons
# - Créer les objets
# ex →   obj = Button((position_x,position_y),(width,height),"dossier/nomdelimage.extension")
classic_pong = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(720)),"buttons/PLAY.png")
fun          = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(600)),"buttons/FUN.png")
invisiball   = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(720)),"buttons/INVISIBALL.png")
ia           = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(600)),"buttons/IA.png")
cursed_ball  = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(480)),"buttons/CURSED BALL.png")
bill_ball    = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(360)),"buttons/BILL BALL.png")
settings     = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(480)),"buttons/SETTINGS.png")
skins        = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(720)),"buttons/SKINS.png")
volume       = Button((rescaling_x(100),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x( 50),screen.get_size()[1]-rescaling_y(600)),"buttons/VOLUME.png")
plus         = Button((rescaling_x(100),rescaling_y(100)),(screen.get_size()[0]//2+rescaling_x(100),screen.get_size()[1]-rescaling_y(600)),"buttons/+.png")
minus        = Button((rescaling_x(100),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(200),screen.get_size()[1]-rescaling_y(600)),"buttons/-.png")
quitter      = Button((rescaling_x(300),rescaling_y(100)),(screen.get_size()[0]//2-rescaling_x(150),screen.get_size()[1]-rescaling_y(120)),"buttons/QUIT.png")
# - Charger l'image
classic_pong_img = pygame.image.load(classic_pong.get_image()).convert()
fun_img          = pygame.image.load(fun.get_image()).convert()
invisiball_img   = pygame.image.load(invisiball.get_image()).convert()
ia_img           = pygame.image.load(ia.get_image()).convert()
cursed_ball_img  = pygame.image.load(cursed_ball.get_image()).convert()
bill_ball_img    = pygame.image.load(bill_ball.get_image()).convert()
settings_img     = pygame.image.load(settings.get_image()).convert()
skins_img        = pygame.image.load(skins.get_image()).convert()
volume_img       = pygame.image.load(volume.get_image()).convert()
plus_img         = pygame.image.load(plus.get_image()).convert()
minus_img        = pygame.image.load(minus.get_image()).convert()
quit_img         = pygame.image.load(quitter.get_image()).convert()
# - Stockage des informations de bases des boutons -> autoscale
taille1 = (300,100)
taille2 = (100,100)
pos1    = (150,720)
pos2    = (150,600)
pos3    = (150,480)
pos4    = (150,360)
pos5    = (150,120)
pos6    = (50 ,600)
pos7    = (100,600)
pos8    = (200,600)

def draw_buttons():
    if pygame.display.get_caption()[0] == 'MENU':
        screen.blit(rescale_img(classic_pong_img,classic_pong.get_taille()),classic_pong.get_coord())
        screen.blit(rescale_img(fun_img,fun.get_taille()),fun.get_coord())
        screen.blit(rescale_img(settings_img,settings.get_taille()),settings.get_coord())
        screen.blit(rescale_img(quit_img,quitter.get_taille()),quitter.get_coord())
    elif pygame.display.get_caption()[0] == 'FUN':
        screen.blit(rescale_img(invisiball_img,invisiball.get_taille()),invisiball.get_coord())
        screen.blit(rescale_img(ia_img,ia.get_taille()),ia.get_coord())
        screen.blit(rescale_img(cursed_ball_img,cursed_ball.get_taille()),cursed_ball.get_coord())
        screen.blit(rescale_img(bill_ball_img,bill_ball.get_taille()),bill_ball.get_coord())
    elif pygame.display.get_caption()[0] == 'SETTINGS':
        screen.blit(rescale_img(skins_img,skins.get_taille()),skins.get_coord())
        screen.blit(rescale_img(volume_img,volume.get_taille()),volume.get_coord())
        screen.blit(rescale_img(plus_img,plus.get_taille()),plus.get_coord())
        screen.blit(rescale_img(minus_img,minus.get_taille()),minus.get_coord())
#####################


# Gestion des skins
# - Créer les objets
none    = Skins((30,30),(screen.get_size()[0]//2-120,screen.get_size()[1]-720),0,0,None)
notch   = Skins((30,30),(screen.get_size()[0]//2-60,screen.get_size()[1]-720),1,10,"ball_skins/notch.png")
lgbt    = Skins((30,30),(screen.get_size()[0]//2,screen.get_size()[1]-720),2,50,"ball_skins/lgbt.png")
ukraine = Skins((30,30),(screen.get_size()[0]//2+60,screen.get_size()[1]-720),3,100,"ball_skins/ukraine.png")
spman   = Skins((30,30),(screen.get_size()[0]//2+120,screen.get_size()[1]-720),4,200,"ball_skins/spiderman.png")
# - Créer la surface
selection    = pygame.Surface((40,40))
demo_none    = pygame.Surface(none.get_taille())
demo_notch   = pygame.Surface(notch.get_taille())
demo_lgbt    = pygame.Surface(lgbt.get_taille())
demo_ukraine = pygame.Surface(ukraine.get_taille())
demo_spman   = pygame.Surface(spman.get_taille())
# - Charger l'image
selection_img = pygame.image.load("ball_skins/selection.png")
demo_none.fill((255,255,255))
notch_img   = pygame.image.load(notch.get_texture()).convert()
lgbt_img    = pygame.image.load(lgbt.get_texture()).convert()
ukraine_img = pygame.image.load(ukraine.get_texture()).convert()
spman_img   = pygame.image.load(spman.get_texture()).convert_alpha()

def draw_demo(dt,dc,dc2,dc3,dc4,dc5):
    screen.blit(demo_none,pygame.Rect(dc2,dt))
    screen.blit(demo_notch,pygame.Rect(dc,dt))
    demo_notch.blit(notch_img,(0,0))
    screen.blit(demo_lgbt,pygame.Rect(dc3,dt))
    demo_lgbt.blit(lgbt_img,(0,0))
    screen.blit(demo_ukraine,pygame.Rect(dc4,dt))
    demo_ukraine.blit(ukraine_img,(0,0))
    screen.blit(demo_spman,pygame.Rect(dc5,dt))
    demo_spman.blit(spman_img,(0,0))

def draw_selection():
    # obtenir les coordonnées du là où la selection devra apparaitre
    if   shop.is_selected(0): coord_selection = (none.get_coord()[0]-5,none.get_coord()[1]-5)       # None
    elif shop.is_selected(1): coord_selection = (notch.get_coord()[0]-5,notch.get_coord()[1]-5)     # Notch
    elif shop.is_selected(2): coord_selection = (lgbt.get_coord()[0]-5,lgbt.get_coord()[1]-5)       # lgbt
    elif shop.is_selected(3): coord_selection = (ukraine.get_coord()[0]-5,ukraine.get_coord()[1]-5) # Ukraine
    elif shop.is_selected(4): coord_selection = (spman.get_coord()[0]-5,spman.get_coord()[1]-5)     # Spiderman
    # afficher la selection
    screen.blit(selection,pygame.Rect(coord_selection,(40,40)))
    selection.blit(selection_img,(0,0))

def put_skins():
    if shop.is_selected(none.get_idskin()): # None
        su.fill((255,255,255))
    elif shop.is_selected(notch.get_idskin()): # Notch
        skin_img = pygame.image.load(notch.get_texture()).convert()
        su.blit(skin_img,(0,0))
    elif shop.is_selected(lgbt.get_idskin()): # lgbt
        skin_img = pygame.image.load(lgbt.get_texture()).convert()
        su.blit(skin_img,(0,0))
    elif shop.is_selected(ukraine.get_idskin()): # Ukraine
        skin_img = pygame.image.load(ukraine.get_texture()).convert()
        su.blit(skin_img,(0,0))
    elif shop.is_selected(spman.get_idskin()): # Spiderman
        skin_img = pygame.image.load(spman.get_texture()).convert()
        su.blit(skin_img,(0,0))
#####################


# Gestion des coins et du shop
c = Coins('coins.txt')
c.create()
coins_img = pygame.image.load('src/coins.png').convert()
font_coins = pygame.font.Font("src/PKMN RBYGSC.ttf",rescaling_font(35))
font_error = pygame.font.Font("src/PKMN RBYGSC.ttf",rescaling_font(35))

shop = Shop("saves.csv")
shop.create()

def draw_coins(coins):
    font_coins = pygame.font.Font("src/PKMN RBYGSC.ttf",rescaling_font(35))
    screen.blit(rescale_img(coins_img,(rescaling_x(coins_img.get_height()),rescaling_y(coins_img.get_width()))),(rescaling_x(25),screen.get_size()[1]-rescaling_y(100)))
    coins_text = font_coins.render(coins,False,(255,255,255))
    screen.blit(coins_text,(rescaling_x(130),screen.get_size()[1]-rescaling_y(70)))

alpha = 0
missing_coins = 0

def draw_no_coins(skin_price,coins,alpha) :
    font_error = pygame.font.Font("src/PKMN RBYGSC.ttf",rescaling_font(35))
    error_text = font_error.render(str(-1*(int(coins) - skin_price)) + ' missing !', False ,(alpha,alpha,alpha))
    screen.blit(error_text,((screen.get_size()[0] // 2) - rescaling_x(150), screen.get_size()[1] - rescaling_y(70)))
###################


# Paramètres communs entre les fenêtres
def global_settings():
    # GLOBAL VARIABLES
    global fullscreen
    global play
    global screen

    # QUITTER LE JEU
    if event.type == QUIT:
        play = False

    # REDIMENSIONNER LA FENÊTRE
    elif event.type == VIDEORESIZE:
        if not fullscreen :
            screen = pygame.display.set_mode((event.w, event.h),RESIZABLE)
            autoscale(classic_pong,taille1[0],taille1[1],pos1[0],pos1[1])
            autoscale(fun         ,taille1[0],taille1[1],pos2[0],pos2[1])
            autoscale(invisiball  ,taille1[0],taille1[1],pos1[0],pos1[1])
            autoscale(ia          ,taille1[0],taille1[1],pos2[0],pos2[1])
            autoscale(cursed_ball ,taille1[0],taille1[1],pos3[0],pos3[1])
            autoscale(bill_ball   ,taille1[0],taille1[1],pos4[0],pos4[1])
            autoscale(settings    ,taille1[0],taille1[1],pos3[0],pos3[1])
            autoscale(skins       ,taille1[0],taille1[1],pos1[0],pos1[1])
            autoscale(volume      ,taille2[0],taille2[1],pos6[0],pos6[1])
            autoscale(plus        ,taille2[0],taille2[1],pos7[0],pos7[1],"reverse")   # le reverse sert à changer le signe dans le calcul de la fonction
            autoscale(minus       ,taille2[0],taille2[1],pos8[0],pos8[1])
            autoscale(quitter     ,taille1[0],taille1[1],pos5[0],pos5[1])

    # CUSTOM KEYBINDS
    elif event.type == KEYDOWN:
    # REVENIR AU MENU AVEC LA TOUCHE ECHAP
        if event.key == K_ESCAPE :
            pygame.display.set_caption('MENU')
    # QUITTER LE JEU AVEC LA TOUCHE F12
        elif event.key == K_F12 :
            play = False
    # CHANGER LE MODE DE L'ECRAN AVEC F11
        elif event.key == K_F11:
            fullscreen = not fullscreen
            if fullscreen :
                screen = pygame.display.set_mode((info.current_w,info.current_h), FULLSCREEN)
                pygame.mouse.set_visible(False)
            else :
                screen = pygame.display.set_mode((info.current_w,info.current_h), RESIZABLE)
                pygame.mouse.set_visible(True)
#######################################


#------------------------------------------------- MAIN -----------------------------------------------------------
fullscreen = True
play = True
while play:

    clock.tick(60)

    bg_taille   = screen.get_size()
    mouse_coord = pygame.mouse.get_pos()
    coins       = c.get_coins()
    if audio_device and not pygame.mixer.music.get_busy() : pygame.mixer.music.play()

    # LOADING-----------------------------------------------------------------------------------------------------
    if pygame.display.get_caption()[0] == 'LOADING...':
        fade()

    # MENU--------------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'MENU':
        pygame.mouse.set_visible(True)
        sec = 0     #initialisation des secondes (timer)

        # RESET DE LA PARTIE
        score.reset_score()
        ball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,450))
        barreg.set_pos((30,300))
        barred.set_pos((screen.get_size()[0]-60,300))

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BOUTONS CLIQUÉS
            if pygame.mouse.get_pressed()[0]:

                if classic_pong.get_clicked(mouse_coord) :
                    pygame.display.set_caption('PONG')
                    if fullscreen : pygame.mouse.set_visible(False)
                elif fun.get_clicked(mouse_coord) :
                    pygame.display.set_caption('FUN')
                elif settings.get_clicked(mouse_coord):
                    pygame.display.set_caption('SETTINGS')
                elif quitter.get_clicked(mouse_coord) :
                    play = False

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_title()
        draw_coins(coins)
        draw_buttons()
        pygame.display.flip()

    # JEU PONG----------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'PONG' :

        # BALL MOVEMENTS
        ball.avancer('NORMAL')
        ball.collision(barreg.get_pos(),barreg.get_orientation(),1,'NORMAL')
        ball.collision(barred.get_pos(),barred.get_orientation(),2,'NORMAL')
        if ball.get_coord()[0] < 0 :
            ball.reset(screen.get_size()[0],screen.get_size()[1], randint(270,450))
            score.add_pts(2)
        elif ball.get_coord()[0] > screen.get_size()[0]+1:
            ball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,270))
            score.add_pts(1)

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BARRES MOVEMENTS
            if pygame.key.get_pressed()[pygame.K_w]:
                barreg.move('haut')
                barreg.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_s]:
                barreg.move('bas')
                barreg.set_orientation('bas')

            if pygame.key.get_pressed()[pygame.K_UP]:
                barred.move('haut')
                barred.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                barred.move('bas')
                barred.set_orientation('bas')

        if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN] :
            barred.set_orientation('neutre')
        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] :
            barreg.set_orientation('neutre')

        # SCREEN UPTADE
        screen.fill((0,0,0))

        #draw_background()
        draw_ball(ball.get_coord())
        put_skins()
        draw_barres(barreg.get_pos(),barred.get_pos())
        draw_score()
        pygame.display.flip()

    # SETTINGS------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'SETTINGS':
        pygame.mouse.set_visible(True)
        sec += 1

        for event in pygame.event.get():
            # PARAMETRES DE BASE
            global_settings()
            if sec >= 5:             # PERMET DE CRÉER UN LÉGER DÉLAI POUR NE PAS CLIQUER SUR PLUSIEURS BOUTONS EN MÊME TEMPS
            # BOUTONS CLIQUÉS
                if pygame.mouse.get_pressed()[0]:
                    if skins.get_clicked(mouse_coord) :
                        sec = 0       # RESET DU TIMER
                        pygame.display.set_caption('SKINS')
                        affichage = False
                    # GESTION DU VOLUME DU SON
                    elif plus.get_clicked(mouse_coord):
                        if audio_device:
                            if volume_int < 100 :
                                pygame.mixer.music.set_volume((volume_int/100)+0.1)
                                volume_int += 10
                    elif minus.get_clicked(mouse_coord):
                        if audio_device :
                            if volume_int > 0 :
                                pygame.mixer.music.set_volume((volume_int/100)-0.1)
                                volume_int -= 10

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_title()
        draw_coins(coins)
        draw_buttons()
        draw_volume()
        pygame.display.flip()

    # SKINS---------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'SKINS':
        pygame.mouse.set_visible(True)
        sec += 1

        for event in pygame.event.get():
            # PARAMETRES DE BASE
            global_settings()
            if sec >= 5:             # PERMET DE CRÉER UN LÉGER DÉLAI POUR NE PAS CLIQUER SUR PLUSIEURS BOUTONS EN MÊME TEMPS
            # SKINS CLIQUÉS
                if pygame.mouse.get_pressed()[0]:
                    if none.select(mouse_coord):
                        if shop.select(int(coins),none.get_price(),none.get_idskin()) == True :
                            c.add_coins(-none.get_price())
                    elif notch.select(mouse_coord):
                        if shop.select(int(coins),notch.get_price(),notch.get_idskin()) == True :
                            c.add_coins(-notch.get_price())
                        elif shop.select(int(coins),notch.get_price(),notch.get_idskin()) == "No coins":
                            missing_coins = notch.get_price()
                            alpha = 255
                    elif lgbt.select(mouse_coord):
                        if shop.select(int(coins),lgbt.get_price(),lgbt.get_idskin()) == True:
                            c.add_coins(-lgbt.get_price())
                        elif shop.select(int(coins),lgbt.get_price(),lgbt.get_idskin()) == "No coins" :
                            missing_coins = lgbt.get_price()
                            alpha = 255
                    elif ukraine.select(mouse_coord):
                        if shop.select(int(coins),ukraine.get_price(),ukraine.get_idskin()) == True:
                            c.add_coins(-ukraine.get_price())
                        elif shop.select(int(coins),ukraine.get_price(),ukraine.get_idskin()) == "No coins":
                            missing_coins = ukraine.get_price()
                            alpha = 255
                    elif spman.select(mouse_coord):
                        if shop.select(int(coins),spman.get_price(),spman.get_idskin()) == True:
                            c.add_coins(-spman.get_price())
                        elif shop.select(int(coins),spman.get_price(),spman.get_idskin()) == "No coins":
                            missing_coins = spman.get_price()
                            alpha = 255

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_title()
        draw_coins(coins)
        if alpha > 4 :
            alpha -= 4
            draw_no_coins(missing_coins,coins,alpha)
        draw_selection()
        draw_demo(notch.get_taille(),notch.get_coord(),none.get_coord(),lgbt.get_coord(),ukraine.get_coord(),spman.get_coord())
        pygame.display.flip()

    # FUN-----------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'FUN':
        pygame.mouse.set_visible(True)
        sec += 1

        for event in pygame.event.get():
            # PARAMETRES DE BASE
            global_settings()
            if sec >= 10:             # PERMET DE CRÉER UN LÉGER DÉLAI POUR NE PAS CLIQUER SUR PLUSIEURS BOUTONS EN MÊME TEMPS
            # BOUTONS CLIQUÉS
                if pygame.mouse.get_pressed()[0]:
                    if invisiball.get_clicked(mouse_coord) :
                        sec = 0       # RESET DU TIMER
                        pygame.display.set_caption('INVISIBALL')
                        if fullscreen : pygame.mouse.set_visible(False)
                        su.fill((255,255,255))
                    elif ia.get_clicked(mouse_coord) :
                        pygame.display.set_caption('IA')
                        if fullscreen : pygame.mouse.set_visible(False)
                    elif cursed_ball.get_clicked(mouse_coord) :
                        sec = 0       # RESET DU TIMER
                        pygame.display.set_caption('CURSED BALL')
                        if fullscreen : pygame.mouse.set_visible(False)
                    elif bill_ball.get_clicked(mouse_coord) :
                        pygame.display.set_caption('BILL BALL')
                        if fullscreen : pygame.mouse.set_visible(False)

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_title()
        draw_buttons()
        pygame.display.flip()

    # INVISIBALL----------------------------------------------------------------------------------------------
    if pygame.display.get_caption()[0] == 'INVISIBALL':

        # BALL MOVEMENTS
        ball.avancer('INVISIBALL')
        ball.collision(barreg.get_pos(),barreg.get_orientation(),1,'INVISIBALL')
        ball.collision(barred.get_pos(),barred.get_orientation(),2,'INVISIBALL')
        if ball.get_coord()[0] < 0 :
            ball.reset(screen.get_size()[0],screen.get_size()[1], randint(270,450))
            score.add_pts(2)
            show()
        elif ball.get_coord()[0] > screen.get_size()[0]+1:
            ball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,270))
            score.add_pts(1)
            show()
        sec += 1
        if sec == 60 :
            hide()
            sec = 0

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BARRES MOVEMENTS
            if pygame.key.get_pressed()[pygame.K_w]:
                barreg.move('haut')
                barreg.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_s]:
                barreg.move('bas')
                barreg.set_orientation('bas')

            if pygame.key.get_pressed()[pygame.K_UP]:
                barred.move('haut')
                barred.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                barred.move('bas')
                barred.set_orientation('bas')

        if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN] :
            barred.set_orientation('neutre')
        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] :
            barreg.set_orientation('neutre')

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_ball(ball.get_coord())
        draw_barres(barreg.get_pos(),barred.get_pos())
        draw_score()
        pygame.display.flip()

    # IA----------------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'IA' :

        # BALL MOVEMENTS
        ball.avancer('NORMAL')
        ball.collision(barreg.get_pos(),barreg.get_orientation(),1,'NORMAL')
        ball.collision(barreIA.get_pos(),barreIA.get_orientation(),2,'NORMAL')
        if ball.get_coord()[0] < 0 or ball.get_coord()[0] > screen.get_size()[0]+1:
            if ball.get_coord()[0] > screen.get_size()[0]+1 : c.add_coins(10)
            ball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,270))

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BARRE MOVEMENTS
            if pygame.key.get_pressed()[pygame.K_w]:
                barreg.move('haut')
                barreg.set_orientation('haut')
            elif pygame.key.get_pressed()[pygame.K_s]:
                barreg.move('bas')
                barreg.set_orientation('bas')

        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] :
            barreg.set_orientation('neutre')

        # BARRE IA
        barreIA.move(ball.get_coord()[1])

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_coins(coins)
        draw_ball(ball.get_coord())
        put_skins()
        draw_barres_IA(barreg.get_pos(),barreIA.get_pos())
        pygame.display.flip()

    # CURSED BALL--------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'CURSED BALL' :

        sec += 1
        # BALL MOVEMENTS
        ball.avancer('NORMAL')
        ball.collision(barreg.get_pos(),barreg.get_orientation(),1,'NORMAL')
        ball.collision(barred.get_pos(),barred.get_orientation(),2,'NORMAL')
        if ball.get_coord()[0] < 0 :
            ball.reset(screen.get_size()[0],screen.get_size()[1], randint(270,450))
            score.add_pts(2)
        elif ball.get_coord()[0] > screen.get_size()[0]+1:
            ball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,270))
            score.add_pts(1)
        # BALL RANDOM MOVEMENTS
        if sec >= randint(180,300):
                ball.set_angle(ball.get_angle() - randint(90,270))
                ball.set_speed(ball.get_speed() + randint(1,3))
                sec = 0

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BARRES MOVEMENTS
            if pygame.key.get_pressed()[pygame.K_w]:
                barreg.move('haut')
                barreg.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_s]:
                barreg.move('bas')
                barreg.set_orientation('bas')

            if pygame.key.get_pressed()[pygame.K_UP]:
                barred.move('haut')
                barred.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                barred.move('bas')
                barred.set_orientation('bas')

        if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN] :
            barred.set_orientation('neutre')
        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] :
            barreg.set_orientation('neutre')

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_ball(ball.get_coord())
        put_skins()
        draw_barres(barreg.get_pos(),barred.get_pos())
        draw_score()
        pygame.display.flip()

    # BILL BALL---------------------------------------------------------------------------------------------------
    elif pygame.display.get_caption()[0] == 'BILL BALL' :

        # BILL BALL MOVEMENTS
        bball.avancer('NORMAL')
        bball.collision(barreg.get_pos(),barreg.get_orientation(),1,'NORMAL')
        bball.collision(barred.get_pos(),barred.get_orientation(),2,'NORMAL')
        if bball.get_coord()[0] < 0 :
            bball.reset(screen.get_size()[0],screen.get_size()[1], randint(270,450))
            score.add_pts(2)
        elif bball.get_coord()[0] > screen.get_size()[0]+1:
            bball.reset(screen.get_size()[0],screen.get_size()[1],randint(90,270))
            score.add_pts(1)

        for event in pygame.event.get():
        # PARAMETRES DE BASE
            global_settings()
        # BARRES MOVEMENTS
            if pygame.key.get_pressed()[pygame.K_w]:
                barreg.move('haut')
                barreg.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_s]:
                barreg.move('bas')
                barreg.set_orientation('bas')

            if pygame.key.get_pressed()[pygame.K_UP]:
                barred.move('haut')
                barred.set_orientation('haut')
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                barred.move('bas')
                barred.set_orientation('bas')

        if not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN] :
            barred.set_orientation('neutre')
        if not pygame.key.get_pressed()[pygame.K_w] and not pygame.key.get_pressed()[pygame.K_s] :
            barreg.set_orientation('neutre')

        # SCREEN UPTADE
        screen.fill((0,0,0))

        draw_bball(bball.get_coord())
        put_skins()
        draw_barres(barreg.get_pos(),barred.get_pos())
        draw_score()
        pygame.display.flip()

# END THE GAME
pygame.quit()
###################################################################################################################