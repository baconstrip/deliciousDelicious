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

        ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1], timeout=1000)

        # Check if we reached the server

        stdin1, stdout1, stderr1 = ssh.exec_command("grep Active /proc/meminfo | awk \'{print $2}\'")
        stdoutData1 = stdout1.readline()
        stdin2, stdout2, stderr2 = ssh.exec_command("grep MemTotal /proc/meminfo | awk \'{print $2}\'")
        stdoutData2 = stdout2.readline()

        stdin3, stdout3, stderr3 = ssh.exec_command("top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\" | awk \'{print 100 - $1\"%\"}'")
        stdoutData3 = stdout3.readline()


        self.addElement(Container("Container", 0))
        self.addElement(Label("Label1", 1, "Memory Used:"))
        self.addElement(Label("Label2", 2, stdoutData1))
        self.addElement(Label("Label3", 3, "Maximum Mememory:"))
        self.addElement(Label("Label4", 4, stdoutData2))

        self.addElement(Label("Label5", 5, "CPU Usage:"))
        self.addElement(Label("Label6", 6, stdoutData3))

