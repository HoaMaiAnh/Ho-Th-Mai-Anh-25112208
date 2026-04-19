import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit   # Chất (Cơ, Rô, Chuồn, Bích)
        self.rank = rank   # Giá trị (2->10, J, Q, K, A)

    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = []
        for _ in range(num_cards):
            if self.cards:
                dealt_cards.append(self.cards.pop())
        return dealt_cards

class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        self.cards.extend(cards)

    def show_hand(self):
        return ", ".join(str(card) for card in self.cards)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

class PokerGame:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def start_game(self):
        print("\n--- BẮT ĐẦU POKER GAME ---")
        self.deck.shuffle()
        print("Đã trộn bài xong.")
        
        # Mỗi người được chia 2 lá (Texas Hold'em cơ bản)
        for player in self.players:
            player.hand.add_cards(self.deck.deal(2))
            print(f"Người chơi {player.name} nhận bài: {player.hand.show_hand()}")

# TEST BT NC
game = PokerGame(["Alice", "Bob", "Charlie"])
game.start_game()