from protocol.piranhamessage import PiranhaMessage
from protocol.messages.Home.LoginOK import LoginOK
from protocol.messages.Home.OwnHomeDMessage import OwnHomeDMessage

class Login(PiranhaMessage):
    def __init__(self):
        super().__init__()
        self.id = 20100
    
    def decode(self):
        self.HighID = self.stream.readInt()
        self.LowID = self.stream.readInt()

    def process(self):
        con.messaging.send_message(LoginOK())
        con.messaging.send_message(OwnHomeDMessage())