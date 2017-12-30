from src.game import start
from src.welcome import welcome


def main():
    start_game = welcome()
    if start_game:
        start()
