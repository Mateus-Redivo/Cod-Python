import random
import os
import time
from collections import defaultdict


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11  # Ace value is handled in Hand class
        else:
            return int(self.rank)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.original_count = len(self.cards)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def cards_remaining(self):
        return len(self.cards)

    def get_remaining_card_counts(self):
        """Returns count of each card value remaining in deck"""
        counts = defaultdict(int)
        for card in self.cards:
            if card.rank in ["J", "Q", "K"]:
                counts[10] += 1
            elif card.rank == "A":
                counts[11] += 1
            else:
                counts[int(card.rank)] += 1
        return counts


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.rank == "A":
                aces += 1
                value += 11
            else:
                value += card.value

        # Convert aces from 11 to 1 as needed
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.games_played = 0
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0

    def reset(self):
        if self.deck.cards_remaining() < 15:  # Reshuffle if running low on cards
            self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def initial_deal(self):
        # Deal two cards to player and dealer
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def calculate_bust_probability(self):
        """Calculate probability of busting if hitting"""
        current_value = self.player_hand.get_value()
        bust_threshold = 21 - current_value + 1

        # Count cards that would cause a bust
        card_counts = self.deck.get_remaining_card_counts()
        bust_cards = sum(
            count for value, count in card_counts.items() if value >= bust_threshold)

        if self.deck.cards_remaining() == 0:
            return 0

        bust_probability = bust_cards / self.deck.cards_remaining()
        return bust_probability * 100  # Return percentage

    def play(self):
        self.reset()
        self.initial_deal()

        # Game loop
        self.display_game_state(hide_dealer=True)

        # Check for natural blackjack
        if self.player_hand.get_value() == 21:
            if self.dealer_hand.get_value() == 21:
                self.display_game_state(hide_dealer=False)
                print("Both have Blackjack! It's a tie!")
                self.ties += 1
            else:
                self.display_game_state(hide_dealer=False)
                print("Blackjack! You win!")
                self.player_wins += 1
            self.games_played += 1
            return

        # Player's turn
        while True:
            bust_probability = self.calculate_bust_probability()
            print(
                f"\nProbability of busting if you hit: {bust_probability:.1f}%")

            choice = input("Do you want to (H)it or (S)tand? ").strip().lower()

            if choice == 'h':
                self.player_hand.add_card(self.deck.deal())
                self.display_game_state(hide_dealer=True)

                if self.player_hand.get_value() > 21:
                    print("Bust! You lose.")
                    self.dealer_wins += 1
                    self.games_played += 1
                    return
            elif choice == 's':
                break

        # Dealer's turn
        self.display_game_state(hide_dealer=False)

        while self.dealer_hand.get_value() < 17:
            time.sleep(1)  # Pause for effect
            print("Dealer hits...")
            self.dealer_hand.add_card(self.deck.deal())
            time.sleep(0.5)
            print(f"Dealer drew: {self.dealer_hand.cards[-1]}")
            print(f"Dealer's hand: {self.dealer_hand}")
            print(f"Dealer's total: {self.dealer_hand.get_value()}")

        dealer_value = self.dealer_hand.get_value()
        player_value = self.player_hand.get_value()

        # Determine outcome
        if dealer_value > 21:
            print("Dealer busts! You win!")
            self.player_wins += 1
        elif dealer_value > player_value:
            print(
                f"Dealer wins with {dealer_value} against your {player_value}.")
            self.dealer_wins += 1
        elif player_value > dealer_value:
            print(
                f"You win with {player_value} against dealer's {dealer_value}!")
            self.player_wins += 1
        else:
            print(f"It's a tie at {player_value}!")
            self.ties += 1

        self.games_played += 1

    def display_game_state(self, hide_dealer=False):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("=== BLACKJACK ===")
        print(
            f"Games played: {self.games_played} | Player wins: {self.player_wins} | Dealer wins: {self.dealer_wins} | Ties: {self.ties}")
        print("\nDealer's hand:")
        if hide_dealer:
            print(f"{self.dealer_hand.cards[0]} and [Hidden]")
            print(f"Dealer's visible total: {self.dealer_hand.cards[0].value}")
        else:
            print(self.dealer_hand)
            print(f"Dealer's total: {self.dealer_hand.get_value()}")

        print("\nYour hand:")
        print(self.player_hand)
        print(f"Your total: {self.player_hand.get_value()}")

        # Display deck information
        print(
            f"\nCards remaining in deck: {self.deck.cards_remaining()}/{self.deck.original_count}")


def display_probability_lesson():
    print("\n=== BLACKJACK PROBABILITY CONCEPTS ===")
    print("1. Bust Probability: The chance of drawing a card that puts you over 21")
    print("2. Card Counting: The composition of the remaining deck affects probabilities")
    print("3. Basic Strategy: Mathematical optimal play based on your hand vs dealer's up card")
    print("4. Expected Value: Making decisions that are profitable in the long run")
    print("\nThis game shows real-time bust probability to help you make informed decisions.")


def main():
    print("Welcome to Blackjack - A game of probability!")
    display_probability_lesson()
    input("\nPress Enter to continue...")

    game = BlackjackGame()

    while True:
        game.play()
        if input("\nPlay again? (y/n): ").strip().lower() != 'y':
            break

    print("\n=== FINAL STATISTICS ===")
    print(f"Games played: {game.games_played}")
    print(
        f"Player wins: {game.player_wins} ({game.player_wins/game.games_played*100:.1f}%)")
    print(
        f"Dealer wins: {game.dealer_wins} ({game.dealer_wins/game.games_played*100:.1f}%)")
    print(f"Ties: {game.ties} ({game.ties/game.games_played*100:.1f}%)")
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
