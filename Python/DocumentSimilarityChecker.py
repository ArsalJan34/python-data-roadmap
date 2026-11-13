import string

def getcleanwords(text):
  trans_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
  return set(text.translate(trans_table).lower().split())
def calculate_similarity(text1,text2):
  set1 = getcleanwords(text1)
  set2= getcleanwords(text2)

  intersection = set1.intersection(set2)
  union = set1.union(set2)

  if not union:
    return 0.0
  return len(intersection)/ len(union)
def print_same(text1,text2):
  set1 = getcleanwords(text1)
  set2 = getcleanwords(text2)
  intersection = set1.intersection(set2)
  print(intersection)

t1 = "Python programming is fun and powerful until you go deep"
t2 = "Python helped me get blowjob from girl because she told me to teach her and she told me you should fuck me too deep very deeply"
score = calculate_similarity(t1,t2)
same_words= print_same(t1,t2)

print(f"Similarity score: {score:.2f} ({score * 100:.1f}%)")
