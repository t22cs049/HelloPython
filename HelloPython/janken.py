import random

#入力可能タイプ
"""class RockPaperScissors:
    def __init__(self):
        self.choices = ["グー", "チョキ", "パー"]

    def get_computer_choice(self):
        return random.randint(0, 2)

    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "引き分け"
        elif (player_choice == 0 and computer_choice == 1) or \
             (player_choice == 1 and computer_choice == 2) or \
             (player_choice == 2 and computer_choice == 0):
            return "プレイヤーの勝ち"
        else:
            return "コンピュータの勝ち"

    def play(self, player_choice):
        computer_choice = self.get_computer_choice()
        result = self.get_result(player_choice, computer_choice)
        return {
            "player_choice": self.choices[player_choice],
            "computer_choice": self.choices[computer_choice],
            "result": result
        }
# 使用例
if __name__ == "__main__":
    game = RockPaperScissors()
    
    print("0: グー, 1: チョキ, 2: パー")
    player_input = int(input("あなたの選択は？ (0-2): "))
    
    if player_input not in [0, 1, 2]:
        print("無効な入力です。0, 1, 2 のいずれかを入力してください。")
    else:
        result = game.play(player_input)
        print(f"あなたの選択: {result['player_choice']}")
        print(f"コンピュータの選択: {result['computer_choice']}")
        print(f"結果: {result['result']}")"""

#自動で先に３回勝った方の勝利
"""class RockPaperScissors:
    def __init__(self):
        self.moves = {0: "グー", 1: "チョキ", 2: "パー"}
        self.player1_score = 0
        self.player2_score = 0

    def get_move(self):
        return random.randint(0, 2)

    def judge_round(self, move1, move2):
        if move1 == move2:
            return "引き分け"
        elif (move1 - move2) % 3 == 1:
            return "プレイヤー2の勝ち"
        else:
            return "プレイヤー1の勝ち"

    def play_game(self):
        while self.player1_score < 3 and self.player2_score < 3:
            move1 = self.get_move()
            move2 = self.get_move()
            
            print(f"プレイヤー1: {self.moves[move1]}, プレイヤー2: {self.moves[move2]}")
            
            result = self.judge_round(move1, move2)
            print(result)
            
            if result == "プレイヤー1の勝ち":
                self.player1_score += 1
            elif result == "プレイヤー2の勝ち":
                self.player2_score += 1
            
            print(f"スコア - プレイヤー1: {self.player1_score}, プレイヤー2: {self.player2_score}\n")

        if self.player1_score > self.player2_score:
            print("プレイヤー1の勝利！")
        else:
            print("プレイヤー2の勝利！")

# ゲームを実行
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()"""
    
#自動で３回勝負
"""def play_game():
    # 手の定義
    hands = {0: "グー", 1: "チョキ", 2: "パー"}
    
    # 勝敗カウント
    player1_wins = 0
    player2_wins = 0
    
    for round in range(1, 4):  # 3回のゲーム
        print(f"\nラウンド {round}:")
        
        # プレイヤーの手を決定
        player1 = random.randint(0, 2)
        player2 = random.randint(0, 2)
        
        print(f"プレイヤー1: {hands[player1]}")
        print(f"プレイヤー2: {hands[player2]}")
        
        # 勝敗判定
        if player1 == player2:
            print("引き分け")
        elif (player1 - player2) % 3 == 1:
            print("プレイヤー2の勝ち")
            player2_wins += 1
        else:
            print("プレイヤー1の勝ち")
            player1_wins += 1
        
        print(f"現在の勝利数 - プレイヤー1: {player1_wins}, プレイヤー2: {player2_wins}")
        
        # 2勝した場合、ゲーム終了
        if player1_wins == 2 or player2_wins == 2:
            break
    
    # 最終結果
    print("\n最終結果:")
    if player1_wins == player2_wins:
        print("引き分け")
    elif player1_wins > player2_wins:
        print("プレイヤー1の勝利!")
    else:
        print("プレイヤー2の勝利!")

# ゲームの実行
if __name__ == "__main__":
    play_game()"""
    
import random

def play_janken(num_players):
    choices = ["グー", "チョキ", "パー"]
    scores = [0] * num_players
    
    def determine_winner(player_choices):
        if len(set(player_choices)) == 1:  # 全員同じ手
            return None
        if len(set(player_choices)) == 3:  # 3種類全ての手が出た
            return None
        winning_choice = max(set(player_choices))
        winners = [i for i, choice in enumerate(player_choices) if choice == winning_choice]
        return winners

    while max(scores) < 2:
        player_choices = [random.randint(0, 2) for _ in range(num_players)]
        
        print("\n今回の手:")
        for i, choice in enumerate(player_choices):
            print(f"プレイヤー{i+1}: {choices[choice]}")
        
        winners = determine_winner(player_choices)
        
        if winners is None:
            print("引き分け")
        else:
            for winner in winners:
                scores[winner] += 1
                print(f"プレイヤー{winner+1}の勝ち")
        
        print("\n現在のスコア:")
        for i, score in enumerate(scores):
            print(f"プレイヤー{i+1}: {score}")

    winners = [i for i, score in enumerate(scores) if score == 2]
    for winner in winners:
        print(f"\nプレイヤー{winner+1}の勝利!")

if __name__ == "__main__":
    num_players = int(input("プレイヤーの数を入力してください: "))
    play_janken(num_players)