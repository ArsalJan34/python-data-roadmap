import string

lexicon = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5
}

def censor_review_with_stars(text):
    words = text.split()
    new_words = []

    for word in words:

        clean_word = word.strip(string.punctuation).lower()

        if clean_word in lexicon:

            star_rep = '*' * lexicon[clean_word]
            new_words.append(star_rep)
        else:

            new_words.append(word)


    return " ".join(new_words)


user_name = input("Enter Your name: ")
review = input("Enter The Review: ")


censored_review = censor_review_with_stars(review)


print(f"\n{user_name} Review:\n{censored_review}")
