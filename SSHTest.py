import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

filename = open("./Login.txt")
user=filename.read().split()

ssh.connect('wopr.csl.mtu.edu',username=user[0],password=user[1])

stdin, stdout, stderr = ssh.exec_command("lsblk")

for line in stdout.readlines():
	print(line)


