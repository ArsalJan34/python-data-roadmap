import string
lexicon = {
  "great": 2, "awesome": 3, "love": 2, "good": 1, "amazing": 3,
  "terrible": -2, "awful": -3, "hate": -2, "bad": -1, "worst": -3
}
def analyze_sentiment(text):
  trans_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
  words = text.translate(trans_table).lower().split()
  score = sum(lexicon.get(word,0) for word in words)
  if score > 0:
    return f"Positive (Score:{score})"
  elif score < 0:
    return f"Negatvie( Score:{score})"
  return f"Neutral (Score:{score})"

review = "The servie was absolutely awful and bad food was worst and terrible behavior of owner ngl i hate this restuarant"
print(analyze_sentiment(review))
