
class Barre():

    def __init__(self,taille,x,y,height):
        self.__taille = taille
        self.__orientation = 'neutre'
        self.__x = x
        self.__y = y
        self.__height = height


    def get_pos(self):
        return (self.__x,self.__y)

    def set_pos(self,coord):
        self.__x = coord[0]
        self.__y = coord[1]

    def get_taille(self):
        return self.__taille

    def get_orientation (self) :
        return self.__orientation

    def set_orientation (self, o) :
        self.__orientation = o

    def move(self,orientation):
        if orientation == "haut" and self.get_pos()[1] >= 0:
            self.__y -= 10
        elif orientation == "bas" and self.get_pos()[1] <= self.__height :
            self.__y += 10





class Barre_IA():

    def __init__(self,taille,x,y,height):
        self.__taille = taille
        self.__orientation = 'neutre'
        self.__x = x
        self.__y = y
        self.__height = height


    def get_pos(self):
        return (self.__x,self.__y)

    def set_pos(self,coord):
        self.__x = coord[0]
        self.__y = coord[1]

    def get_taille(self):
        return self.__taille

    def get_orientation (self) :
        return self.__orientation

    def set_orientation (self, o) :
        self.__orientation = o

    def move(self,coord_ball):
        if self.get_pos()[1] > coord_ball - 75 and self.get_pos()[1] >= 0:
            self.__y -= 8
        elif self.get_pos()[1] < coord_ball - 125 and self.get_pos()[1] <= self.__height :
            self.__y += 8