def lose_points(current_score):
    new_score = current_score - 10

    if new_score < 0:
        new_score = 0

    return new_score

def get_rating(final_score):
    if final_score >= 80:
        return "Excellent"
    elif final_score >= 50:
        return "Good"
    else:
        return "Bad"

if __name__ == '__main__':
    score = 100

    score = lose_points(score)
    print("Score: ", score)

    rating = get_rating(score)
    print("Rating: ", rating)

