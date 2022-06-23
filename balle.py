from random import randint
from math import cos,sin, pi, radians

class Ball :

    def __init__ (self,speed,x,y,surface,res,angle = randint(0,359)) :

        self.__speed = speed
        self.__angle = angle
        self.surface = surface
        self.__coord = (x,y)
        self.res = res
        self.in_border = False

        self.rgb = False

    def set_coord (self,x,y) :
        self.__coord = (x,y)

    def get_coord (self) :
        return self.__coord

    def set_angle (self, a) :
        self.__angle = a

    def get_angle (self) :
        return self.__angle

    def caper_angle (self) :
        angle = self.get_angle()
        if angle >= 360 :
            self.set_angle(angle - 360)
        elif angle < 0 :
            self.set_angle(angle + 360)
        if cos(radians(self.get_angle())) >= 0 :
            if sin(radians(self.get_angle())) >= 0.9 : self.set_angle(self.get_angle()-0.2)
            elif sin(radians(self.get_angle())) <= -0.9: self.set_angle(self.get_angle()+0.2)
        else :
            if sin(radians(self.get_angle())) >= 0.9 : self.set_angle(self.get_angle()+0.2)
            elif sin(radians(self.get_angle())) <= -0.9 : self.set_angle(self.get_angle()-0.2)



    def get_speed (self) :
        return self.__speed

    def set_speed (self,s) :
        self.__speed = s

    def rebond (self,param) :
        self.caper_angle()
        angle = self.get_angle()
        cord = self.get_coord()

        if cord[1] <= 0 or cord[1] >= self.res[1] - 30:
            if not self.in_border :
                self.set_angle(360 - angle)
                if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))
            self.in_border = True

        else : self.in_border = False


    def avancer (self,param) :
        self.caper_angle()
        angle = self.get_angle()

        x = self.get_coord()[0]
        y = self.get_coord()[1]
        s = self.get_speed()

        self.set_coord(x+cos(radians(angle)) * s, y - sin(radians(angle)) * s)
        self.rebond(param)

        if self.rgb :
            self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))


    def collision (self, cord_barre, orientation, j,param) :
        self.caper_angle()
        angle = self.get_angle()
        cord = self.get_coord()

        if j == 1 :
            if cord_barre[0] >= cord[0]-30 and cord_barre[0] <= cord[0] and cord[1] >= cord_barre[1] and cord[1] <= cord_barre[1]+200:
                if orientation == 'haut' :
                    self.set_angle(200 - angle)
                    self.set_coord(cord[0]+8,cord[1])
                elif orientation == 'bas' :
                    self.set_angle(160 - angle)
                    self.set_coord(cord[0]+8,cord[1])
                else :
                    self.set_angle(180 - angle)

                    self.add_speed()
                    if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                    #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))

        if j == 2 :
            if cord_barre[0] >= cord[0] and cord_barre[0] <= cord[0]+30 and cord[1] >= cord_barre[1] and cord[1] <= cord_barre[1]+200:
                if orientation == 'haut' :
                    self.set_angle(160 - angle)
                    self.set_coord(cord[0]-8,cord[1])
                elif orientation == 'bas' :
                    self.set_angle(200 - angle)
                    self.set_coord(cord[0]-8,cord[1])
                else :
                    self.set_angle(180 - angle)

                self.add_speed()
                if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))

    def add_speed(self) :
        if self.get_speed() < 25 :
            self.set_speed(self.get_speed() + 0.5)
        #else :
            #self.rgb = True


    def reset(self,x,y,angle):
        self.caper_angle()
        self.set_angle(angle)
        self.set_speed(12)
        self.set_coord(x//2,y//2)
        self.rgb = False


##################################################################################################



class Bill_Ball :

    def __init__ (self,speed,x,y,surface,res,angle = randint(0,359)) :

        self.__speed = speed
        self.__angle = angle
        self.surface = surface
        self.__coord = (x,y)
        self.res = res
        self.in_border = False
        self.fast = False

        self.rgb = False

    def set_coord (self,x,y) :
        self.__coord = (x,y)

    def get_coord (self) :
        return self.__coord

    def set_angle (self, a) :
        self.__angle = a

    def get_angle (self) :
        return self.__angle

    def caper_angle (self) :
        angle = self.get_angle()
        if angle >= 360 :
            self.set_angle(angle - 360)
        elif angle < 0 :
            self.set_angle(angle + 360)
        if cos(radians(self.get_angle())) >= 0 :
            if sin(radians(self.get_angle())) >= 0.9 : self.set_angle(self.get_angle()-0.2)
            elif sin(radians(self.get_angle())) <= -0.9: self.set_angle(self.get_angle()+0.2)
        else :
            if sin(radians(self.get_angle())) >= 0.9 : self.set_angle(self.get_angle()+0.2)
            elif sin(radians(self.get_angle())) <= -0.9 : self.set_angle(self.get_angle()-0.2)



    def get_speed (self) :
        return self.__speed

    def set_speed (self,s) :
        self.__speed = s

    def rebond (self,param) :
        self.caper_angle()
        angle = self.get_angle()
        cord = self.get_coord()

        if cord[1] <= 0 or cord[1] >= self.res[1] - 30:
            if not self.in_border :
                self.set_angle(360 - angle)
                if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))
            self.in_border = True

        else : self.in_border = False


    def avancer (self,param) :
        self.caper_angle()
        angle = self.get_angle()

        x = self.get_coord()[0]
        y = self.get_coord()[1]
        s = self.get_speed()

        self.set_coord(x+cos(radians(angle)) * s, y - sin(radians(angle)) * s)
        self.rebond(param)

        if self.rgb :
            self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))


    def collision (self, cord_barre, orientation, j,param) :
        self.caper_angle()
        angle = self.get_angle()
        cord = self.get_coord()

        if j == 1 :
            if cord_barre[0] >= cord[0]-30 and cord_barre[0] <= cord[0] and cord[1] >= cord_barre[1] and cord[1] <= cord_barre[1]+200:
                if orientation == 'haut' :
                    self.set_angle(200 - angle)
                    self.set_coord(cord[0]+8,cord[1])
                elif orientation == 'bas' :
                    self.set_angle(160 - angle)
                    self.set_coord(cord[0]+8,cord[1])
                else :
                    self.set_angle(180 - angle)

                self.add_speed()
                if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))

        if j == 2 :
            if cord_barre[0] >= cord[0] and cord_barre[0] <= cord[0]+30 and cord[1] >= cord_barre[1] and cord[1] <= cord_barre[1]+200:
                if orientation == 'haut' :
                    self.set_angle(160 - angle)
                    self.set_coord(cord[0]-8,cord[1])
                elif orientation == 'bas' :
                    self.set_angle(200 - angle)
                    self.set_coord(cord[0]-8,cord[1])
                else :
                    self.set_angle(180 - angle)

                self.add_speed()
                if param == 'INVISIBALL' : self.surface.fill((255,255,255))
                #else : self.surface.fill((randint(0,255),randint(0,255),randint(0,255)))

    def add_speed(self) :
        angle = self.get_angle()

        if sin(radians(angle)) > -0.3 and sin(radians(angle)) < 0.3 :
            self.set_speed(100)
            fast = True
        elif self.fast : self.set_speed(12)

        if self.get_speed() < 25 :
            self.set_speed(self.get_speed() + 0.5)
        else :
            self.rgb = True


    def reset(self,x,y,angle):
        self.caper_angle()
        self.set_angle(angle)
        self.set_speed(12)
        self.set_coord(x//2,y//2)
        self.rgb = False