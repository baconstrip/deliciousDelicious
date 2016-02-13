import paramiko

class cpuUsage(Display):

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(
	paramiko.AutoAddPolicy())

	filename = open("./Login.txt")
	user=filename.read().split()

	ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1])

	stdin, stdout, stderr = ssh.exec_command("top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'")
	stdoutData = stdout.read()

	container1 = Container("container1", 0)
	layout.append(container1)

	label1 = Label("label1", 1)
	label1.text="CPU Usage:"
	container1.addElement(label1)

	value1 = Label("value1", 2)
	value1.value=stdoutData
	container1.addElement(value1)

