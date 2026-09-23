from utils import generate_secret_number, check_user_guess
from score import lose_points, get_rating

secret_number = generate_secret_number()
score = 100

while True:
    correct = check_user_guess(secret_number)

    if correct:
        break
    else:
        score = lose_points(score)
        print("Score: ", score)

rating = get_rating(score)

print("Final score: ", score)
print("Rating: ", rating)