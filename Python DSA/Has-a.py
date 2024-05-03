class player:
    def __init__(self,name):
        self.name = name
    def getplayer(self):
        return self.name
class team:
    def __init__(self):
        self.players= []
    def addplayer(self,player):
        self.players.append(player)
p1=player("sachin")
p2=player("kapil")
p3=player("virat")
t=team()
t.addplayer(p1)
t.addplayer(p2)
t.addplayer(p3)
print(t.players[0].getplayer())
print(t.players[1].getplayer())
print(t.players[2].name)
del t
print(p1.getplayer())
print(p2.name)