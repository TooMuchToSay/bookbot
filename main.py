from stats import get_num_words
def main():
    total_words = 0
    with open("/home/toomuchtosay/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents, total_words)
        total_words += word_count
    print(f"Found {total_words} total words")
#def get_word_count(file):
 #   #counted = len(file.split(' '))
  
#stuff = len(file.split())
    #sentence = file.split(' ')

 #   return stuff

main()
