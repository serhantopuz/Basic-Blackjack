import random
import os


def generate_card(cards, current_player, current_score):
    random_number = random.randint(0, 12)
    current_player.append(cards[random_number])
    current_score += cards[random_number]

    return current_score


def final_hands(computer_cards, player_cards, player_score):
    print(f"\n   Your cards: {player_cards}, current score: {player_score}")
    print(f"   Computer's first card: {computer_cards[0]}\n")


def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

