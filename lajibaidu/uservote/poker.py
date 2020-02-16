

class poker:

    pokerlist={
        1:'w',
        2:'2',
        3:'1',
        4:'k',
        5:'q',
        6:'j',
        7:'a',
        8:'9',
        9:'8',
        10:'7',
        11:'6',
        12:'5',
        13:'4',
        14:'3',
    }
    userme={}
    usera={}
    userb={}
    userc={}

    surplusNums={
        "unknown":0,
        "me":0,
        "a":0,
        "b":0,
        "c":0,
    }

    unknowpokers={}
    allpokers={}
    perUserNum=27
    perPokerNum = 8

    def pokerinit(self):

        self.surplusNums["unknown"] = self.perUserNum * 4 
        self.surplusNums["a"] = self.perUserNum
        self.surplusNums["b"] = self.perUserNum
        self.surplusNums["c"] = self.perUserNum
        self.surplusNums["me"] = self.perUserNum

        self.allpokers.clear()
        self.unknowpokers.clear
        for p in self.pokerlist:
            self.allpokers[self.pokerlist[p]]= self.perPokerNum
            self.unknowpokers[self.pokerlist[p]]=self.perPokerNum

    def test(self):

        self.UpdateUnknownpoker()
        print("===%d==[%d]===[%d]===[%d]" 
            %(self.surplusNums["unknown"],
            self.surplusNums["a"],
            self.surplusNums["b"],
            self.surplusNums["c"]))

        for i in self.unknowpokers:

            a = i
            if i in self.unknowpokers:
                a="%s   %d" %(a,self.unknowpokers[i])
            else:
                a="%s     out" %(a)

            if i in self.usera:
                a="%s A[%d] " %(a,self.usera[i])
            else:
                a="%s A[ ] " %(a) 

            if i in self.userb:
                a="%s B[%d] " %(a,self.userb[i])
            else:
                a="%s B[ ] " %(a) 

            if i in self.userc:
                a="%s C[%d] " %(a,self.userc[i])
            else:
                a="%s C[ ] " %(a) 
            
            print(a)
    

    def calcupokerbyuser(self,userx):
        for u in userx:
            if userx[u] > 0:
                self.unknowpokers[u] = self.unknowpokers[u] - userx[u]
                
    def UpdateUnknownpoker(self):
        self.calcupokerbyuser(self.userme)
        self.calcupokerbyuser(self.usera)
        self.calcupokerbyuser(self.userb)
        self.calcupokerbyuser(self.userc)
        
    def addoutpoker(self,inputstr,userx,x):
        for i in inputstr:
            if i in userx:
                userx[i] = userx[i] + 1
            else:
                userx[i] = 1
            self.surplusNums[x] = self.surplusNums[x] - 1
            self.surplusNums["unknown"] = self.surplusNums[x] - 1
        
        return userx

    def addpoker_me(self,inputstr):
        self.addoutpoker(inputstr,self.userme,'me')

    def addpoker_usera(self,inputstr):
        self.addoutpoker(inputstr,self.usera,'a')

    def addpoker_userb(self,inputstr):
        self.addoutpoker(inputstr,self.userb,'b')

    def addpoker_userc(self,inputstr):
        self.addoutpoker(inputstr,self.userc,'c')


if __name__ == '__main__':
    a = poker()
    a.pokerinit()

    a.addpoker_me("w222111kqqjjaa9888777654433")
    a.addpoker_usera("33345")
    a.addpoker_usera("jjj45")
    a.addpoker_userc("22233")

    a.test()


