import socket
host = ''
port = 12800
main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connexion.bind((host, port))
main_connexion.listen(5)
client_connexion, connexion_info = main_connexion.accept()
client_connexion.close()
main_connexion.close()
print("lol")
