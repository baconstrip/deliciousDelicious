import paramiko
from Display import Display
from layout.Container import Container
from layout.Label import Label
from layout.PercentBar import PercentBar
from layout.Value import Value

class LinuxServer(Display):

    def __init__(self,name, data):

        # Get ready for the next program file.
        Display.__init__(self,name, data)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        filename=open("./Login.txt")
        user=filename.read().split()
        
        # Connect to the wopr server on campus. Any server can be accessed this way as long as login information is available and an SSH link can be established.
        self.ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1], timeout=1000)

        # Check if we reached the server
        self.addElement(Label("Label0", 4, "Able to connect successfully!", "green"))
        stdin1, stdout1, stderr1 = self.ssh.exec_command("top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\"")
        print(stdout1.read())
        stdoutData1 = stdout1.read()
        stdin2, stdout2, stderr2 = self.ssh.exec_command("grep MemTotal /proc/meminfo | awk '{print $2}")
        stdoutData2 = stdout2.read()

        stdin3, stdout3, stderr3 = self.ssh.exec_command("df | awk \'{print $1}\'")
        stdoutData3 = stdout3.readlines()

        stdin4, stdout4, stderr4 = self.ssh.exec_command("df | awk \'{print $5}\' | sed 's/%//'")
        stdoutData4 = stdout4.readlines()

        stdin5, stdout5, stderr5 = self.ssh.exec_command("grep Active /proc/meminfo | awk '{print $2}")
        stdoutData5 = stdout5.readline()
        
        # Create all of the elements.
        self.addElement(Container("Container", 0))
        self.addElement(Label("Label1", 1, "CPU Usage (%)"))
        self.addElement(PercentBar("PercentageBar", 2, stdoutData1))
        self.addElement(Label("Label2", 2, "Free Memory (%)"))
        self.addElement(PercentBar("PercentageBar2", 4, stdoutData2.decode("UTF-8")))
        self.addElement(Label("Label3", 3, "Maximum Memory (kB)"))
        self.addElement(Label("Label4", 4, stdoutData2.decode("UTF-8")))
        self.addElement(Label("Label5", 5, "Storage (kB):"))
        count=0
        for line in stdoutData3:
                labelName = "Label" + str(count+6)
                self.addElement(Label(labelName, 4, line))
                labelName = "PercentageBar" + str(count)
                self.addElement(PercentBar(labelName, 5, stdoutData4[int(count)]))
                count = count + 1

    def update(self, delta):
        # Get the current memory usage on the computer
        stdin1, stdout1, stderr1 = self.ssh.exec_command("grep Active /proc/meminfo | awk \'{print $2}\'")
        stdoutData1 = stdout1.readline()

        # Get the amount of memory for the computer
        stdin2, stdout2, stderr2 = self.ssh.exec_command("grep MemTotal /proc/meminfo | awk \'{print $2}\'")
        stdoutData2 = stdout2.readline()
        
        # Get the CPU usage of the computer
        stdin3, stdout3, stderr3 = self.ssh.exec_command("top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\" | awk \'{print 100 - $1\"%\"}'")
        stdoutData3 = stdout3.readline()

        stdin3, stdout3, stderr3 = self.ssh.exec_command("df | awk \'{print $1}\'")
        stdoutData3 = stdout3.readlines()

        stdin4, stdout4, stderr4 = self.ssh.exec_command("df | awk \'{print $5}\' | sed 's/%//'")
        stdoutData4 = stdout4.readlines()

        self.updateLayout("Label1",  "CPU Usage (%):")
        self.updateLayout("PercentageBar",  stdoutData1)
        self.updateLayout("Label2",  "Free Memory (%):")
        self.updateLayout("PercentageBar2",  stdoutData1)
        self.updateLayout("Label3",  "Maximum Memory (kB):")
        self.updateLayout("Label4",  stdoutData2)
        self.updateLayout("Label5",  "Storage (kB):")
        
        count=0
        for line in stdoutData3:
                labelName = "Label" + str(count+6)
                self.updateLayout(labelName, line)
                labelName = "PercentageBar" + str(count)
                self.updateLayout(labelName, stdoutData4[int(count)])
                count = count + 1
