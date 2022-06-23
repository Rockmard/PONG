import csv

class Skins :

    def __init__(self,t,c,idskin,p,text):
        self.__taille = t
        self.__coord = c
        self.__idskin = idskin
        self.__price = p
        self.__texture = text

    def get_coord(self):
        return self.__coord

    def set_coord(self,nouv_coord):
        self.__coord = nouv_coord

    def get_taille(self):
        return self.__taille

    def set_taille(self,nouv_taille):
        self.__taille = nouv_taille

    def get_idskin(self):
        return self.__idskin

    def set_idskin(self,nouv_idskin):
        self._idskin = nouv_idskin

    def get_price(self):
        return self.__price

    def set_price(self,nouv_price):
        self.__price = nouv_price

    def get_texture(self):
        return self.__texture

    def set_texture(self,nouv_texture):
        self.__texture = nouv_texture

    def select(self,mouse):
        if self.get_coord()[0] <= mouse[0] <= self.get_coord()[0]+self.get_taille()[0] and self.get_coord()[1] <= mouse[1] <= self.get_coord()[1]+self.get_taille()[1]:
            return True

class Coins():

    def __init__(self,n):
        '''
        n → nom du fichier AVEC son extension
        exemple → 'coins.txt'
        '''
        self.__name = n

    def __file_exist(self):
        try :
            with open(self.__name) :
                return True
        except IOError :
            return False

    def create(self):
        if not self.__file_exist():
            with open(self.__name,'w') as f:
                f.write("0")

    def get_coins(self):
        if self.__file_exist() :
            with open(self.__name,'r') as f:
                return f.read()
        else :
            self.create()

    def add_coins(self,add):
        if self.__file_exist():
            coins = self.get_coins()
            coins = int(coins) + add
            with open(self.__name,'w') as f:
                f.write(str(coins))
        else :
            self.create()

class Shop():

    def __init__(self,n):
        '''
        n → nom du fichier AVEC son extension
        exemple → 'saves.csv'
        '''
        self.__name = n

    def __file_exist(self):
        try :
            with open(self.__name) :
                return True
        except IOError :
            return False

    def create(self):
        if not self.__file_exist():
            with open(self.__name,'w',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id_skin','is_owned','is_selected'])
                writer.writerow(['0','True','True'])
                for i in range(1,50):
                    writer.writerow([str(i),'False','False'])

    def is_owned(self,idskin):
        if self.__file_exist() :
            with open(self.__name,'r') as f:
                reader = csv.DictReader(f)
                line_tab = [dict(line) for line in reader]
                if line_tab[idskin]['is_owned'] == 'True': return True
                else : return False
        else :
            self.create()

    def is_selected(self,idskin):
        if self.__file_exist() :
            with open(self.__name,'r') as f:
                reader = csv.DictReader(f)
                line_tab = [dict(line) for line in reader]
                if line_tab[idskin]['is_selected'] == 'True': return True
                else : return False
        else :
            self.create()

    def select(self,coins,price,idskin):
        # SELECTIONNER LE SKIN SI ON LE POSSEDE DEJA
        if self.is_owned(idskin) :
            if not self.is_selected(idskin):
                with open(self.__name,'r') as f:
                        reader = csv.DictReader(f)
                        line_tab = [dict(line) for line in reader]
                for i in range(len(line_tab)):
                    line_tab[i]['is_selected'] = 'False'
                line_tab[idskin]['is_selected'] = 'True'
                with open(self.__name,'w') as f:
                    writer = csv.DictWriter(f,['id_skin','is_owned','is_selected'])
                    writer.writeheader()
                    for skin_settings in line_tab :
                        writer.writerow(skin_settings)
        # ACHETER LE SKIN LORSQU'ON NE LE POSSEDE PAS
        else :
            if coins >= price :
                with open(self.__name,'r') as f:
                    reader = csv.DictReader(f)
                    line_tab = [dict(line) for line in reader]
                line_tab[idskin]['is_owned'] = 'True'
                with open(self.__name,'w') as f:
                    writer = csv.DictWriter(f,['id_skin','is_owned','is_selected'])
                    writer.writeheader()
                    for skin_settings in line_tab :
                        writer.writerow(skin_settings)
                return True
            elif coins < price :
                return "No coins"



