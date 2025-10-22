from stats import get_num_words
from stats import total_characters
from stats import generate_report
import sys
def main():
    total_words = 0
    try:
        with open(f"{sys.argv[1]}") as f:
            file_contents = f.read()                
            dictionary = total_characters(file_contents)
            word_count = get_num_words(file_contents, total_words)
            total_words += word_count
        print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {total_words} total words\n--------- Character Count -------")
        report = generate_report(dictionary)
        for i in range(0, len(report)):
            print(f"{report[i]['char'].strip()}: {report[i]['num']}")
        print("============= END ===============")
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

                      
#def get_word_count(file):
 #   #counted = len(file.split(' '))
  
#stuff = len(file.split())
    #sentence = file.split(' ')

 #   return stuff

main()
