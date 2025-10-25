import random as rand
from WordState import WordState
import pandas as pd
from collections import defaultdict
    
# Some sentences to test your code on...
test_sentences = ["hello there friend",
                  "hello there good friend",
                  "hello there my good friend",
                  "hello my friend",
                  "hello my good friend",
                  "good day friend",
                  "good morning friend",
                  "good morning to you my friend",
                  "good morning to you my good friend"]
    
# A simple "pre-trained model"/graph derived from above sentences with words and corresponding frequencies.
states = {"#": {"hello": 5, "good": 4},
        "hello": {"there": 3, "my": 2},
        "good": {"friend": 4, "day": 1, "morning": 3},
        "there": {"friend": 1, "good": 1, "my": 1},
        "my": {"good": 2, "friend": 2},
        "friend": {},
        "day": {"friend": 1},
        "morning": {"friend": 1, "to": 2},
        "to": {"you": 2},
        "you": {"my": 1}}
 
#Train Markov chain from csv file
def markov_chain_from_csv(filepath):
      data = pd.read_csv(filepath, usecols=[0], names=["Title"], header=None) #read csv
   
      chain = defaultdict(WordState) #dict to store words and frequencies
      
      #create Markov chain
      for sentence in data["Title"]: 
        words = sentence.strip().split()        #list of words
        words = ["#"] + words           #add "#" as first word
        for i in range(len(words) - 1):         #iterate over data
                current, nxt = words[i], words[i+1]
                chain[current].add_next_word(nxt)

      return chain

#Generate new love song
def generate_new_sentence(chain):
     word = "#" #start of chain
     output = ""
     max_length = 10

     for _ in range(max_length):
        if word not in chain or not chain[word].has_next():
               break
        next_word = chain[word].get_next()
        output += next_word + " "
        word = next_word
     
     return output

def main():
        path = "love_song_data.csv"
        chain = markov_chain_from_csv(path)
        love_song = generate_new_sentence(chain)
        print(love_song)

if __name__ == "__main__":
     main()