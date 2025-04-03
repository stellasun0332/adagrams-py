# import random
from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

# create a dictionary include key as letter and number as value
# use for to loop through the dictianry to get a list of full letters
# use ranint to get random index
# get the randome letter
# append to hand list
# remove from letter_list
# loop 10 times


def draw_letters():
    letter_list = []
    for letter in LETTER_POOL:
        count_num = LETTER_POOL[letter]
        i = 1
        while i <= count_num:
            letter_list.append(letter)
            i += 1

    hand_list = []
    for i in range(10):
        max_index = len(letter_list) - 1
        ran_index = randint(0, max_index)
        ran_letter = letter_list[ran_index]
        hand_list.append(ran_letter)
        letter_list.pop(ran_index)
    return hand_list


def uses_available_letters(word, letter_bank):
    letter_bank_copy = [letter.lower() for letter in letter_bank]
    word = word.lower()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    points = {
            "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1,
            "R": 1, "S": 1, "T": 1, "D": 2, "G": 2, "B": 3, "C": 3,
            "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
            "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10
            }
    word = word.upper()
    if len(word) > 6:
        total_points = 8
    else:
        total_points = 0

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
        get_word_score[word] = word_score

    for key, value in get_word_score.items():
        if value > max_score:
            max_score = value
            max_key = key
        elif value == max_score:
            if len(max_key) == 10:
                return (max_key, max_score)
            elif len(key) == 10 or len(key) < len(max_key):
                max_score = value
                max_key = key
    return (max_key, max_score)


