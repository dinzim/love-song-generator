import random as rand
from WordState import WordState
import pandas as pd
from collections import defaultdict
 
#Train Markov chain from csv file
def markov_chain_from_csv(filepath):
      data = pd.read_csv(filepath, usecols=[0], names=["Title"], header=None) #read csv

      #clean data
      data['Title'] = data['Title'].str.strip() #remove spaces in beginning or end
      data = data[data['Title'].str.contains(' ')]  #removes one-word titles, by keeping with at least one space

      chain = defaultdict(WordState) #dict to store words and frequencies
      
      #create Markov chain
      for sentence in data["Title"]: 
        words = sentence.split() #list of words
        words = ["#"] + words  #add "#" as first word
        for i in range(len(words) - 1):    #iterate over data
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
        print("--- Love Song Title Generator ---")

        path = "love_song_data.csv"
        chain = markov_chain_from_csv(path)
        num_titles = 1
        store_songs = []

        print(f"Press Enter to generate {num_titles} love song title(s)")
        print("Type 's' for settings")
        print("Type 'q' to quit")
        print("Type 'f' so save love song titles to a file")

        while True:
                cmd = input(":")
                
                if cmd == "q":
                        print("Goodbye!")
                        break
                elif cmd == "s":
                        print("---Settings---")
                        print("1 | Training data path:", path)
                        print("2 | Number of sentences:", num_titles)
                        choice = input("Enter setting number to change: ")

                        if choice == "1":
                            path = str(input("Enter new path: "))
                            chain = markov_chain_from_csv(path)
                            print("Setting saved!")

                        if choice == "2":
                            num_titles = int(input("Enter number of sentences: "))
                            print("Setting saved!")
                elif cmd == "f":
                        with open("generated_titles.txt", "w", encoding="utf-8") as f:
                              for title in store_songs:
                                    f.write(title + "\n")
                        print("Titles successfully stored in file 'generated_titles.txt'")
                else:
                        for _ in range(num_titles):
                            love_song = generate_new_sentence(chain)
                            store_songs.append(love_song)
                            print(love_song)

if __name__ == "__main__":
     main()