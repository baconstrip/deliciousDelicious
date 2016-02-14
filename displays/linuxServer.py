import paramiko
from Display import Display
from layout.Container import Container
from layout.Label import Label
from layout.PercentBar import PercentBar
from layout.Value import Value

class LinuxServer(Display):

    def __init__(self,name, data):
        Display.__init__(self,name, data)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        filename=open("./Login.txt")
        user=filename.read().split()

        reachable=ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1], timeout=1000)

        # Check if we reached the server
        if reachable:
            self.addElement(Label("Label0", 4, "Able to connect successfully!", "green"))
            stdin1, stdout1, stderr1 = ssh.exec_command("top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\"")
            print(stdout1.read())
            stdoutData1 = stdout1.read()
            stdin2, stdout2, stderr2 = ssh.exec_command("grep MemTotal /proc/meminfo | awk '{print $2}")
            stdoutData2 = stdout2.read()

            self.addElement(Container("Container", 0))
            self.addElement(Label("Label1", 1, "CPU Usage"))
            self.addElement(PercentBar("PercentageBar", 2, stdoutData1))
            self.addElement(Label("Label2", 3, stdoutData2))

        else:
            self.addElement(Label("Label2", 4, "Not able to connect to the server!", "red"))
        
