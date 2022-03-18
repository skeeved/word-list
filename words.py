#!/usr/bin/python3
"""
startswith: one char
endswith: one char
contains: one or more chars
notcontains: one or more chars
at: one or more chars, `a=4,u=2`
notat: one or more chars, each char can be repeated, `l=1,a=3,a=4,l=5`
"""
import argparse


def generate_word_list(input_file='words_alpha.txt', output_file='words-short.txt'):
    count = 0
    words = list()
    with open(input_file, 'r') as raw_words:
        for word in raw_words:
            word = word.strip().lower()
            if len(word) == 5:
                words.append(word)
                count += 1
    with open('words.txt', 'w') as five_letter_words:
        words.sort()
        for word in words:
            five_letter_words.write(word + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--contains', default='')
    parser.add_argument('-n', '--notcontains', default='')
    parser.add_argument('-a', '--at', default='')
    parser.add_argument('--notat', default='')
    parser.add_argument('-f', '--file', default='words.txt')
    args = parser.parse_args()

    print(f"\n\nWord Finder")
    print("===================================")
    count = 0
    matches = list()
    with open(args.file, 'r') as words:
        for word in words:
            found = True
            word = word.strip()

            if args.contains:
                all_match = True
                for i in args.contains:
                    if i not in word:
                        all_match = False
                if not all_match:
                    continue
            if args.notcontains:
                no_match = True
                for i in args.notcontains:
                    if i in word:
                        no_match = False
                        break
                if not no_match:
                    continue
            if args.at:
                all_match = True
                items = args.at.split(',')
                for item in items:
                    c, i = item.split('=')
                    i = int(i) - 1
                    if not word[i] == c:
                        all_match = False
                        break
                if not all_match:
                    continue
            if args.notat:
                no_match = False
                items = args.notat.split(',')
                for item in items:
                    c, i = item.split('=')
                    i = int(i) - 1
                    if word[i] == c:
                        no_match = True
                        break
                if no_match:
                    continue
            count += 1
            matches.append(word)
            print(f"{count:4}: {word}")
    print("===================================")
    print(f"Contains letters:         {args.contains}")
    print(f"Does not contain letters: {args.notcontains}")
    print(f"Has letters at:           {args.at}")
    print(f"Does not have letters at: {args.notat}")
    print(f"Found {count} words")
