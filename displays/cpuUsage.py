import paramiko
from Display import Display
from layout.Container import Container
from layout.Label import Label
from layout.PercentBar import PercentBar
from layout.Value import Value

class cpuUsage(Display):
    name = "cpuUsage"

    def __init__(self):
        Display.__init__(self)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        filename=open("./Login.txt")
        user=filename.read().split()

        ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1])

        stdin, stdout, stderr = ssh.exec_command("top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\" | awk '{print 100 - $1\"%\"}'")
        stdoutData = stdout.read()
        self.addElement(Container("Container", 0))
        self.addElement(Label("Label", 1, "CPU Usage"))
        self.addElement(PercentBar("PercentageBar", 2, 10))
        self.addElement(Value("Value", 3, stdoutData))
        
