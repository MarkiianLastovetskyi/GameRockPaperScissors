import socket
import xml.etree.ElementTree as ET
import random

# Список можливих ходів гри
MOVES = ['rock', 'paper', 'scissors']

def determine_winner(player_move, server_move):
    """
    Визначає переможця гри на основі ходів гравця та сервера.

    :param player_move: Хід гравця (рядок, який може бути 'rock', 'paper' або 'scissors').
    :param server_move: Хід сервера (рядок, який може бути 'rock', 'paper' або 'scissors').
    :return: Результат гри (рядок), який може бути 'It's a tie!', 'You win!' або 'You lose!'.
    """
    if player_move == server_move:
        return "It's a tie!"
    elif (player_move == 'rock' and server_move == 'scissors') or \
         (player_move == 'scissors' and server_move == 'paper') or \
         (player_move == 'paper' and server_move == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def start_server():
    """Запускає сервер для обробки з'єднань."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")

        data = conn.recv(1024).decode()
        print(f"Received from client: {data}")
        player_move = data.strip().lower()
        server_move = random.choice(MOVES)
        print(f"Server move: {server_move}")
        result = determine_winner(player_move, server_move)

        response = ET.Element('response')
        ET.SubElement(response, 'player_move').text = player_move
        ET.SubElement(response, 'server_move').text = server_move
        ET.SubElement(response, 'result').text = result
        conn.send(ET.tostring(response))
        conn.close()

if __name__ == "__main__":
    start_server()
