#!/usr/bin/python3

def main():
    sentence = input("Please type in a sentence.: ")
    result = word_counter(sentence)
    print(result)

def word_counter(text):
    count = {}

    for word in text.split():
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    return count



main()