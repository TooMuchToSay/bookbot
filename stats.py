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
        if i == ' ':
            pass
        elif i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i]+ 1
        
    return dictionary

def sort_function(list):
    return list['num']

def generate_report(dictionary):
    total_dicts = {}
    all_dicts = []
    for key in dictionary:
        #print(key, dictionary[key])
        new_dict = {'char': key} | {'num': dictionary[key]}
        all_dicts.append(new_dict)
    all_dicts.sort(reverse=True, key=sort_function)
    return all_dicts
