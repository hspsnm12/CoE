def feedback(ratings):
    if not ratings:
        return "No ratings available"
    positive_ratings = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_ratings / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.1f}%"

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(feedback(ratings))
