def get_num_words(file, total):
    count = len(file.split())
    total += count
    return total
def total_characters(file):
    dictionary = {}
    for i in file.lower():
        #if i not in dictionary.keys():
         #   num = file.count(i.lower())
           # dictionary[i] = num
        #elif i in dictionary.keys():
         #   pass
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i]+ 1
    return dictionary
