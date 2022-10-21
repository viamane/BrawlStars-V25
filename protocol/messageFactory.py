from protocol.messages.Auth.Login import Login
from protocol.messages.Auth.clientHello import ClientHelloMessage
from protocol.messages.Auth.Login import Login

packets = {
    10100: ClientHelloMessage,
    10101: Login,
}

class MessageFactory:
    def create_message_by_type(m_type):
        if m_type in packets:
            return packets[m_type]()
        return None