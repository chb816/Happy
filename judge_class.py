class Annie :
    def __init__(self, health, mana, ap):
        self.health = health
        self.mana = mana
        self.ap = ap
    
    def deal(self) :
        deal = self.ap * 0.65 + 400
        print("티버 : 피해량 ", deal)

health, mana, ap = map(float, input().split())

x= Annie(health=health, mana=mana, ap=ap)
x.deal()

