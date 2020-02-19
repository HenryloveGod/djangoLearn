

class pokerlog:

    id=1,
    user=None,
    log=None


class poker:

    pokerlist={
        1:'w',
        2:'2',
        3:'1',
        4:'k',
        5:'q',
        6:'j',
        7:'0',
        8:'9',
        9:'8',
        10:'7',
        11:'6',
        12:'5',
        13:'4',
        14:'3',
    }

    userlog=[]
    lognum = 0

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

    friend=""

    def pokerinit(self):
        self.userlog.clear()
  
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
        print('朋友是：%s' % self.friend)
        print("共剩余牌数：[%d]，用户A剩余牌数：[%d]，用户B剩余牌数：[%d]，用户C剩余牌数：[%d]" 
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
                a="%s                   A[%d] " %(a,self.usera[i])
            else:
                a="%s                   A[ ] " %(a) 

            if i in self.userb:
                a="%s                   B[%d] " %(a,self.userb[i])
            else:
                a="%s                   B[ ] " %(a) 

            if i in self.userc:
                a="%s                   C[%d] " %(a,self.userc[i])
            else:
                a="%s                   C[ ] " %(a) 
            
            print(a)

        for l in self.userlog:
            print("%d %s %s " %(l.id,l.user,l.log))


    def calcupokerbyuser(self,userx):
        for u in userx:
            isFound=False
            for k in self.pokerlist:
                if u in self.pokerlist[k]:
                    isFound=True
                    break
            if isFound is False:
                print('input %s error,continue' % u) 
                continue
            else:
                if userx[u] > 0:
                    self.unknowpokers[u] = self.unknowpokers[u] - userx[u]
    
    #更新位置牌
    def UpdateUnknownpoker(self):
        self.calcupokerbyuser(self.userme)
        self.calcupokerbyuser(self.usera)
        self.calcupokerbyuser(self.userb)
        self.calcupokerbyuser(self.userc)
        
    def GetPokerStringNum(self,inputstr):
        num = 0
        for u in inputstr:
            for k in self.pokerlist:
                if u in self.pokerlist[k]:
                    num = num+1

        return num

    def addoutpoker(self,inputstr,userx,x):
        self.lognum = self.lognum + 1
        tmplog = pokerlog() 
        tmplog.id = self.lognum
        tmplog.user = x
        tmplog.log = inputstr

        self.userlog.append(tmplog)

        print('您已输入有效字符数：%d' % self.GetPokerStringNum(inputstr))
        for i in inputstr:
            if i in userx:
                userx[i] = userx[i] + 1
            else:
                userx[i] = 1
            self.surplusNums[x] = self.surplusNums[x] - 1
            self.surplusNums["unknown"] = self.surplusNums["unknown"] - 1
        

        return userx

    def addpoker_me(self,inputstr):
        self.addoutpoker(inputstr,self.userme,'me')

    def addpoker_usera(self,inputstr):
        self.addoutpoker(inputstr,self.usera,'a')

    def addpoker_userb(self,inputstr):
        self.addoutpoker(inputstr,self.userb,'b')

    def addpoker_userc(self,inputstr):
        self.addoutpoker(inputstr,self.userc,'c')


    def APIaddpoker(self,inputstr,userstr):

        if 'm' in userstr:
            a.addpoker_me(inputstr)
        elif 'a' in userstr:
            a.addpoker_usera(inputstr)
        elif 'b' in userstr:
            a.addpoker_usera(inputstr)
        elif 'c' in userstr:
            a.addpoker_usera(inputstr)
        else:
            return False
        
        return True


if __name__ == '__main__':
    a = poker()
    a.pokerinit()

    while True:
        ps = input("输入已知的牌(m:a:b:c)")
        if 'm+' in ps[0:2]:
            a.addpoker_me(ps[2:])
        elif 'a+' in ps[0:2]:
            a.addpoker_usera(ps[2:])
        elif 'b+' in ps[0:2]:
            a.addpoker_userb(ps[2:])
        elif 'c+' in ps[0:2]:
            a.addpoker_userc(ps[2:])
        elif 'p+' in ps[0:2]:
            a.friend = ps[2:]
        else:
            print("input error,please input again with 'm:' or 'a:' or 'b:' or 'c:' ")

        a.test()




