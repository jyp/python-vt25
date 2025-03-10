

def guess_winner(white_rating, black_rating):
    A = black_rating
    B = white_rating
    expected_score = 1 / (10**((B-A)/400) + 1)
    print(expected_score)
    if 0.45 <= expected_score <= 0.55:
        print("A draw is expected")
    elif expected_score <= 0.45:
        print("White is expected to win")
    else:
        print("Black is expected to win")

guess_winner(2000,1000)
guess_winner(1000,1200)
guess_winner(1400,1400)
