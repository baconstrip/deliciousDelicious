from Display import Display
import socket

class DeliciousMC(Display):

    def __init__(self, name, data):
        Display.__init__(self, name, data)
        
        values = self.grabData()

        self.addElement(Label("playerLabel", 0, "Players online: ")) 
        self.addElement(Value("players", 2, values[0] + '/' + values[1]))
        self.addElement(Label("uptimelable", 4, "Uptime: "))
        self.addElement(Value("uptime", 5, values[2]))

    def update(self, delta):
        print(delta)
        try:
            values = self.grabData()
        except ConnectionRefusedError:
            return ("Server Unreachable!", 3)
        self.updateLayout("players", values[0] + '/' + values[1])
        self.updateLayout("uptime", values[2])

    def grabData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("localhost", 24921))
        except ConnectionRefusedError as e:
            raise e
        totalsent = 0

        msg = b"DeliciousMCsupersecret\n"

        while totalsent < len(msg):
            sent = s.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

        value = s.recv(1024)
        decoded = value.decode("UTF-8")
        return decoded.split('\n');  
