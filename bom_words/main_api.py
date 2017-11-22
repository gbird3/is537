#!/usr/bin/env python3
import re
import time

from worddata import WordData
from merge_api import merge_lists
from bubblesort_api import bubble_sort
from insertionsort_api import insertion_sort

RE_LETTERS = re.compile('[^a-zA-Z]')
FILENAMES = [
    [ '1 Nephi',         '01-1 Nephi.txt' ],
    [ '2 Nephi',         '02-2 Nephi.txt' ],
    [ 'Jacob',           '03-Jacob.txt' ],
    [ 'Enos',            '04-Enos.txt' ],
    [ 'Jarom',           '05-Jarom.txt' ],
    [ 'Omni',            '06-Omni.txt' ],
    [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    [ 'Mosiah',          '08-Mosiah.txt' ],
    [ 'Alma',            '09-Alma.txt' ],
    [ 'Helaman',         '10-Helaman.txt' ],
    [ '3 Nephi',         '11-3 Nephi.txt' ],
    [ '4 Nephi',         '12-4 Nephi.txt' ],
    [ 'Mormon',          '13-Mormon.txt' ],
    [ 'Ether',           '14-Ether.txt' ],
    [ 'Moroni',          '15-Moroni.txt' ],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    # lowercase the entire text
    text = text.lower()
    # split the text by whitespace to get a list of words
    word_list = text.split()

    # convert each word to the longest run of characters
    # eliminate any words that are empty after conversion to characters

    for i in range(len(word_list)):
        regex1 = re.compile('(^[a-zA-Z]*)\W([a-zA-Z]+)\W*')
        if regex1.match(word_list[i]):
            groups = regex1.search(word_list[i])
            word_list[i] = groups.group(1)
            if len(word_list[i]) < len(groups.group(2)):
                word_list[i] = groups.group(2)
        else:
            word_list[i] = RE_LETTERS.sub('', word_list[i])

    # remove any blank items from the list
    word_list = list(filter(None, word_list))

    # count up the occurance of each word into a dictionary of: word -> count
    bom_dict = dict()
    for i in range(len(word_list)):
        if word_list[i] in bom_dict:
            bom_dict[word_list[i]] += 1
        else:
            bom_dict[word_list[i]] = 1

    # create a WordData item for each word in our list of words
    bom_word_data = []
    for key in bom_dict:
        bom_word_data.append(WordData(book, key, bom_dict[key], round(bom_dict[key]/len(word_list)*100, 1)))

    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]
    bom_word_data = bubble_sort(bom_word_data, 'percent', True)

    # return
    return bom_word_data

################################
###   Prints a words list

def print_words(words, threshold=None, word=None):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word
    for w in words:
        if word == None:
            if w.percent > threshold:
                print('{},{},{},{}'.format(w.book, w.word, w.count, w.percent))
        else:
            if w.word == word:
                print('{},{},{},{}'.format(w.book, w.word, w.count, w.percent))
    # print an empty line
    print()



#######################
###   Main loop

def main():
    '''Main program'''
    master = []
    # loop through the filenames and analyze each one
    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)
    print('INDIVIDUAL BOOKS > 2%')
    for i in FILENAMES:
        with open(i[1], 'r') as file:
            text = file.read()

        word_list = analyze_text(i[0], text)
        print_words(word_list, 2)
        master = merge_lists(master, word_list)

    # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')
    print_words(master, 2)
    # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')
    print_words(master, None, 'christ')
    # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')
    with open('00-Book of Mormon.txt', 'r') as file:
        text = file.read()
        word_list = analyze_text('Book of Mormon', text)
        print_words(word_list, 2)


#######################
###   Runner

if __name__ == '__main__':
    main()
