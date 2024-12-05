alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_to_index = {
  c: i+1 for i,c in enumerate(alphabet)
}

triangle_numbers = {n*(n+1)/2 for n in range(1,1000)}

def word_score(word: str):
  return sum([alphabet_to_index[c] for c in word.lower()])

def word_is_triangle(word: str):
  return word_score(word) in triangle_numbers;

import csv

f = open('problem42.txt','r')
reader = csv.reader(f, delimiter=',')
count = 0
for row in reader:
  for word in row:
    if word_is_triangle(word):
      count += 1
print(count)