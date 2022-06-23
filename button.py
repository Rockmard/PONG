class Button :

    def __init__(self,t,c,img):
        self.__taille = t
        self.__coord = c
        self.__image = img

    def get_coord(self):
        return self.__coord

    def set_coord(self,nouv_coord):
        self.__coord = nouv_coord

    def get_taille(self):
        return self.__taille

    def set_taille(self,nouv_taille):
        self.__taille = nouv_taille

    def get_image(self):
        return self.__image

    def set_image(self,nouv_image):
        self.__image = nouv_image

    def get_clicked(self,mouse):
        if self.get_coord()[0] <= mouse[0] <= self.get_coord()[0]+self.get_taille()[0] and self.get_coord()[1] <= mouse[1] <= self.get_coord()[1]+self.get_taille()[1]:
            return True


















