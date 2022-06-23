class Score :

    def __init__(self):
        self.__score_solo   = 0
        self.__score_gauche = 0
        self.__score_droite = 0

    def get_score(self,j):
        assert 0 <= j <= 2; "le joueur visé n'existe pas → joueurs valides : 0 (solo) 1 (gauche) 2 (droite)"

        if j == 1   : return self.__score_gauche
        elif j == 2 : return self.__score_droite
        elif j == 0 : return self.__score_solo

    def add_pts(self,j):
        assert 0 <= j <= 2; "le joueur visé n'existe pas → joueurs valides : 0 (solo) 1 (gauche) 2 (droite)"

        if j == 1   : self.__score_gauche += 1
        elif j == 2 : self.__score_droite += 1
        elif j == 0 : self.__score_solo += 1

    def reset_score(self):
        self.__score_gauche = 0
        self.__score_droite = 0
        self.__score_solo   = 0




