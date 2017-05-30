import paramiko

host = input('host\n')
user = input('user\n')
secret = input('pass\n')
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)

# Выполнение команды
stdin, stdout, stderr = client.exec_command('uptime')

# Читаем результат
data = stdout.read() + stderr.read()
client.close()


print(data)