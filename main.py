from art import logo
import functions

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

wanna_play = True

while wanna_play:
    player_cards = []
    player_score = 0

    computer_cards = []
    computer_score = 0

    if input("Do you want to play Blackjack? Type 'y' or 'n': ") == 'n':
        wanna_play = False
    else:

        print(logo)
        wanna_get_card = True

        for n in range(0, 2):
            player_score = functions.generate_card(cards, player_cards, player_score)
            computer_score = functions.generate_card(cards, computer_cards, computer_score)

        while wanna_get_card:
            functions.final_hands(computer_cards, player_cards, player_score)

            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                player_score = functions.generate_card(cards, player_cards, player_score)
                if player_score > 21:
                    wanna_get_card = False
                    functions.final_hands(computer_cards, player_cards, player_score)
                    print(f"\n   Your final hand: {player_cards}, final score: {player_score}")
                    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You went over. You lost.\n")
            else:
                while computer_score < player_score:
                    computer_score = functions.generate_card(cards, computer_cards, computer_score)
                if computer_score < 22:
                    print(f"\n   Your final hand: {player_cards}, final score: {player_score}")
                    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You lose.\n")
                else:
                    print(f"\n   Your final hand: {player_cards}, final score: {player_score}")
                    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You won.\n")
                wanna_get_card = False



