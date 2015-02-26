class EasyScorer:
    def __call__(self, p):
        self.p = p
        return self.calc_score(p)

    def calc_score(self, p):
        white_pieces = p.get_white_pieces()
        black_pieces = p.get_black_pieces()

        white = self.get_score_one_sided(white_pieces, black_pieces)
        black = self.get_score_one_sided(black_pieces, white_pieces)

        return white - black

    def get_score_one_sided(self, pieces, enemy_pieces):
        score = 0
        Rooks=[]
        Bishops=[]
        points=[]
        Que=0
        for p,i,j in pieces:
            points.append((i,j))
            if p[0]=='K' or p[0]=='k':
                King=(p,i,j)
            if p[0]=='Q' or p[0]=='q':
                Que=(p,i,j)          
            if p[0]=='B' or p[0]=='b':
                Bishops.append((p,i,j))
            if p[0]=='R' or p[0]=='r':
                Rooks.append((p,i,j))
            if p[0]=='P' or p[0]=='p':
                score+=i/10 
        for p,i,j in enemy_pieces:
            points.append((i,j))    
        for p,i,j in pieces:
            if p=='P' or p=='p' and (i-King[1])**2 + (j-King[2])**2 < 3:
                score+=1
        for r in Rooks:
            x=r[1]
            k=0
            for i in range(0,8):
                if (i,x) not in points:
                    k+=0.1
            if k>5:
                score+=0.2
        if len(Bishops)==2:
            score+=0.33
        bitQ=0
        free=True
        if Que!=0:
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]+t,Que[2]) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]-t,Que[2]) not in points:
                    free=False        
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1],Que[2]-t) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1],Que[2]+t) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]+t,Que[2]+t) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]-t,Que[2]-t) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]-t,Que[2]+t) not in points:
                    free=False   
            free=True
            for t in range(1,8):
                if free:
                    bitQ+=1
                if (Que[1]+t,Que[2]-t) not in points:
                    free=False 
        score+=bitQ/33
        
        for b in Bishops:
            free=True
            bitB=0
            for t in range(1,8):
                if free:
                    bitB+=1
                if (b[1]-t,b[2]+t) not in points:
                    free=False   
            free=True
            for t in range(1,8):
                if free:
                    bitB+=1
                if (b[1]+t,b[2]-t) not in points:
                    free=False
            free=True
            for t in range(1,8):
                if free:
                    bitB+=1
                if (b[1]+t,b[2]+t) not in points:
                    free=False 
            free=True
            for t in range(1,8):
                if free:
                    bitB+=1
                if (b[1]-t,b[2]-t) not in points:
                    free=False 
            score+=bitB/100
        if Que!=0:
            score-=( (King[1]-Que[1])**2+(King[2]-Que[2])**2 )/70
        functions = {
            'p': self.get_pawn_score,
            'n': self.get_knight_score,
            'b': self.get_bishop_score,
            'r': self.get_rook_score,
            'q': self.get_queen_score,
            'k': self.get_king_score,
        }

        for p, i, j in pieces:
            if p == p.lower():
                i = 7 - i
            score += functions[p.lower()](i, j)
        return score

    def get_pawn_score(self, i, j):
        return 1

    def get_knight_score(self, i, j):
        return 3 +  1*bool(2<i<5 and 2<j<5)

    def get_bishop_score(self, i, j):
        return 3

    def get_rook_score(self, i, j):
        return 5+2/((5-i)**2+1)

    def get_queen_score(self, i, j):
        return 9

    def get_king_score(self, i, j):
        return -i

