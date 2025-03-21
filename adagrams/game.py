import random
from random import randint

def draw_letters():
    letter = []
    pool = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    pool_dic= {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, 
    "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, 
    "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}

    while len(letter) < 10:
        index = randint(0,len(pool)-1)
        pick_letter = pool[index]
        if pool_dic[pick_letter]>0: 
            letter.append(pick_letter)
            pool_dic[pick_letter] -= 1
        else: 
            print("Please pick again.")
    return letter


def uses_available_letters(word, letter_bank):
    letter_bank_copy =[letter.lower() for letter in letter_bank]
    word = word.lower()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    points =  {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10}
    word = word.upper()
    if len(word)in (7,8,9,10):
        total_points = 8
    else: total_points = 0
    
    for letter in word:
        point = points[letter]
        total_points += point

    return total_points


def get_highest_word_score(word_list):
    get_word_score = {}
    max_score = 0
    max_key = None
    for word in word_list:
        word_score = score_word(word)
        get_word_score[word]= word_score
    
    for key,value in get_word_score.items():
        if value > max_score:
            max_score = value
            max_key = key
        elif value == max_score:
            if len(max_key) == 10:
                return (max_key, max_score)
                break
            elif len(key) == 10 or len(key) < len(max_key):
                max_score = value
                max_key = key
    return(max_key,max_score)    


    