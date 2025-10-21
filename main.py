from stats import get_num_words
from stats import total_characters 
def main():
    total_words = 0
    with open("/home/toomuchtosay/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        dictionary = total_characters(file_contents)
        word_count = get_num_words(file_contents, total_words)
        total_words += word_count
    print(f"Found {total_words} total words")
    print(dictionary)
#def get_word_count(file):
 #   #counted = len(file.split(' '))
  
#stuff = len(file.split())
    #sentence = file.split(' ')

 #   return stuff

main()
