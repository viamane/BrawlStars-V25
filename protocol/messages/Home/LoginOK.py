from protocol.piranhamessage import PiranhaMessage

class LoginOK(PiranhaMessage):
    def __init__(self):
        super().__init__()
        self.id = 20100
    
    def encode(self):
        self.stream.writeLogicLong(0, 1)
        self.stream.writeLogicLong(0, 1)

        self.stream.writeString()
        self.stream.writeString()
        self.stream.writeString()

        self.stream.writeInt(25)#major
        self.stream.writeInt(1)#minor
        self.stream.writeInt(999)#build

        self.stream.writeString()

        self.stream.writeInt(0)
        self.stream.writeInt(0)
        self.stream.writeInt(0)
        
        self.stream.writeString()
        self.stream.writeString()
        self.stream.writeString()

        self.stream.writeInt(0)
        
        self.stream.writeString()
        self.stream.writeString("RU")
        self.stream.writeString()

        self.stream.writeInt(1)

        self.stream.writeString()

        self.stream.writeInt(0)
        self.stream.writeString()

        self.stream.writeInt(0)
        self.stream.writeInt(0)

        self.stream.writeString()
        self.stream.writeInt(0)

        self.stream.writeCompressedString(b'') # if not working, set self.stream.writeString()
        self.stream.writeBoolean(False)
        self.stream.writeBoolean(False)