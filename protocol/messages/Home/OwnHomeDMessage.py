from protocol.piranhamessage import PiranhaMessage

class OwnHomeDMessage(PiranhaMessage):
    def __init__(self):
        super().__init__()
        self.id = 20100
    
    def encode(self):
        #ratatata
        self.stream.writeVInt(0)#timestamp
        self.stream.writeVInt(0)#timestamp
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(1)#trophy road
        self.stream.writeVInt(0)

        self.stream.writeDataReference(28, 0)
        self.stream.writeDataReference(43, 0)

        self.stream.writeVInt(0)#gamemodes array

        self.stream.writeVInt(0)#selected skins

        self.stream.writeVInt(0)#unlocked skins

        self.stream.writeVInt(0) #leaderboard tid
        self.stream.writeVInt(0) #trophyroad trophy
        self.stream.writeVInt(0) #tokens

        self.stream.writeBoolean(False)#??
        self.stream.writeVInt(1)#control jaja
        self.stream.writeBoolean(True)#hints?

        self.stream.writeVInt(0)#token doubler
        self.stream.writeVInt(0)#season end

        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        #sub_46A214 start (forced drops)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        
        self.stream.writeVInt(0)#array
        for x in range(0):
            self.stream.writeVInt(0)
        #sub_46A214 end
        self.stream.writeByte(8)#token doubler
        self.stream.writeBoolean(True)#token doubler seen state
        self.stream.writeBoolean(True)#event seen state
        self.stream.writeBoolean(True)#coin pack seen state

        self.stream.writeVInt(0)#name change price
        self.stream.writeVInt(0)#timeout for name change

        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)

        self.stream.writeVInt(0)
        #sub_1C4494 (adstatus) start
        self.stream.writeVInt(0) #count
        for x in range(0):
            self.stream.writeVInt(0)
            self.stream.writeVInt(0)
            self.stream.writeVInt(0)
        #end
        self.stream.writeVInt(200)#available tokens
        self.stream.writeVInt(0)#time till 20 tokens

        self.stream.writeVInt(0)#event tickets purchased index array

        self.stream.writeVInt(0)#tickets ammount
        self.stream.writeVInt(0)

        self.stream.writeDataReference(16, 1)#home brawler

        self.stream.writeString("RU")#region
        self.stream.writeString('via')#supported creator

        #int value entry below

        self.stream.writeVInt(6)#int value entry
        self.stream.writeLong(1, 41000012)#menu
        self.stream.writeLong(3, 0)
        self.stream.writeLong(47, 0)
        self.stream.writeLong(46, 1)
        self.stream.writeLong(61, 36270)
        self.stream.writeLong(50, 1)# Coming up quests placeholder
        #conf data now
        self.stream.writeVInt(20220827)#timestamp fdaofaofds;f;sfd;ldfs;lfadl;

        self.stream.writeVInt(10)#tokens for 1 brawl box

        self.stream.writeVInt(10)#shop brawl box cost

        self.stream.writeVInt(30)#shop big box cost
        self.stream.writeVInt(3)#shop big box multiplier
        self.stream.writeVInt(80)#shop megabox cost
        self.stream.writeVInt(10)#shop megabox multiplier
        self.stream.writeVInt(50)#shop token doubler cost
        self.stream.writeVInt(1000)#shop token doubler amount

        self.stream.writeVInt(500)#minimum brawler trophies for season reset
        self.stream.writeVInt(50)#loss percentage
        self.stream.writeVInt(999900)#token limit

        self.stream.writeArrayVInt([0,30,80,170,350,0])#boxes with guaranteed brawlers cost
        self.stream.writeVInt(0)

        self.stream.writeVInt(0)# array

        self.stream.writeVInt(0)# xyi

        self.stream.writeVInt(0)# pezzzd

        self.stream.writeArrayVInt([20,35,75,140,290,480,800,1250]) #brawler upgrade cost
        self.stream.writeArrayVInt([1,2,3,4,5,10,15,20]) #che
        self.stream.writeArrayVInt([10,30,80]) #event tickets cost
        self.stream.writeArrayVInt([6,20,60]) #event tickets amoubr
        self.stream.writeArrayVInt([20,50,140,280]) #coin packs cost
        self.stream.writeArrayVInt([150,400,1200,2600]) #coin packs amount

        self.stream.writeVInt(0)#coin packs cost
        self.stream.writeVInt(200)#max tokens
        self.stream.writeVInt(20)#new tokens

        self.stream.writeVInt(8640) #tokens refresh timer
        self.stream.writeVInt(1) #big box cost
        self.stream.writeVInt(5) #xz

        self.stream.writeByte(3)#unlocked events state

        self.stream.writeVInt(50)#??
        self.stream.writeVInt(604800)#??

        self.stream.writeBoolean(True)#shop boxes enabled

        self.stream.writeVInt(0)#release entry array

        self.stream.writeVInt(0)#array

        self.stream.writeLong(0, 1)

        self.stream.writeVInt(0)

        self.stream.writeBoolean(False)

        self.stream.writeVInt(0)
        self.stream.writeVInt(0)

        #client avatar now
        self.stream.writeLogicLong(0, 1)
        self.stream.writeLogicLong(0, 1)
        self.stream.writeLogicLong(0, 1)

        self.stream.writeString("via")#player name
        self.stream.writeVInt(1)#is name set

        self.stream.writeString()

        self.stream.writeVInt(8)#commodity

        self.stream.writeVInt(1)
        self.stream.writeDataReference(23, 0)

        self.stream.writeVInt(1)
        self.stream.writeDataReference(16, 0)

        self.stream.writeVInt(1)
        self.stream.writeDataReference(16, 0)

        self.stream.writeVInt(1)
        self.stream.writeDataReference(16, 0)

        self.stream.writeVInt(0)

        self.stream.writeVInt(1)
        self.stream.writeDataReference(16, 0)
        
        self.stream.writeVInt(1)
        self.stream.writeDataReference(16, 0)

        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)
        self.stream.writeVInt(0)

        self.stream.writeVInt(2)#tutorial 
        self.stream.writeVInt(0)