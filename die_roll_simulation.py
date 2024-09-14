import random

def simulate_game():
    points = 0
    rolls = 0
    while points < 20:
        roll = random.randint(1, 6)
        if points + roll <= 20:
            points += roll
        rolls += 1
    return rolls

def main():
    num_games = int(input("Enter the number of games to simulate: "))

    roll_counts = [0] * 21
    more_than_20 = 0

    for _ in range(num_games):
        rolls_needed = simulate_game()
        if rolls_needed <= 20:
            roll_counts[rolls_needed] += 1
        else:
            more_than_20 += 1

    for i in range(4, 21):
        print(f"Games with exactly {i} rolls: {roll_counts[i]}")
    print(f"Games with more than 20 rolls: {more_than_20}")

if __name__ == "__main__":
    main()
