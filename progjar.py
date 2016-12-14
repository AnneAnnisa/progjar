import socket

BUFF = 1024
mail_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mail_socket.connect(('mail.its-sby.edu', 25))
print 'S:', mail_socket.recv(BUFF).strip()

# TEST HEHEHE

commands = ['HELO mail.its-sby.edu\r\n', 'AUTH LOGIN\r\n', 'dGVzQGl0cy1zYnkuZWR1\r\n', 'dGVzcHJvZ2phcg==\r\n', 'MAIL FROM:<tes@its-sby.edu>\r\n', 'RCPT TO:<kuliah.progjar@gmail.com>\r\n', 'DATA\r\n', 'hehe\r\n.\r\n', 'QUIT\r\n']
for command in commands:
	mail_socket.send(command)
	print 'S:', mail_socket.recv(BUFF).strip()
mail_socket.close()	