import argparse
import os
from itertools import permutations
from math import log, floor
from colorama import Fore

def generate_word_list(words, append_word, prefix_word, separator):
    # Generate all permutations of the words
    word_permutations = permutations(words)
    
    # Create a list to store the generated word lists
    word_lists = []
    
    # Iterate over the permutations and create word lists
    for permutation in word_permutations:
        if separator:
            word_list = separator.join(permutation)
        else:
            word_list = ''.join(permutation)
        
        if prefix_word:
            word_list = prefix_word + word_list
        if append_word:
            word_list += append_word
        word_lists.append(word_list)
    
    return word_lists

# Function to convert file size to human-readable format
def convert_size(size_bytes):
    if size_bytes == 0:
        return '0 B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(floor(log(size_bytes, 1024)))
    p = pow(1024, i)
    size = round(size_bytes / p, 2)
    return f'{size} {size_name[i]}'

if __name__ == '__main__':

    print(Fore.WHITE + """
    
    ██████╗ █████╗ ██████╗ ████████╗     ██████╗██████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
    ██║     ███████║██████╔╝   ██║       ██║     ██████╔╝██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
    ██║     ██╔══██║██╔═══╝    ██║       ██║     ██╔══██╗██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
    ╚██████╗██║  ██║██║        ██║██╗    ╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
    ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                            
                     Created by """ + Fore.WHITE + "BoΠeShΔdϴw³ | https://github.com/B0neShAd0w/Capt-Cruncher\n")


# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate word lists based on input words.')
parser.add_argument('--input', metavar='word(s)', type=str, nargs='+', help='supply words separated by a space')
parser.add_argument('--separator', metavar='sep', type=str, default=None, help='separator between each input words')
parser.add_argument('--append', metavar='char(s)', type=str, help='append char(s) to each result')
parser.add_argument('--prefix', metavar='char(s)', type=str, help='prefix char(s) to the each result')
parser.add_argument('--output', metavar='file', type=str, default='wordlist.txt', help='output file')
args = parser.parse_args()

# Check if input words are provided
if args.input:
    # Remove leading or trailing separators from input words
    words = [word.strip() for word in args.input]
    
    result = generate_word_list(words, args.append, args.prefix, args.separator)

    # Calculate the line count of the generated results
    line_count = len(result)

    with open(args.output, 'w') as file:
        # Write the generated word lists to the output file
        for word_list in result:
            file.write(word_list + '\n')
        
    # Calculate the file size of the output file
    file_size = os.path.getsize(args.output)
    file_size_str = convert_size(file_size)
    
    print(f'Please be patient while the list is generated...\n')
    print(f'Generated {line_count} combinations.\n')
    print(f'Output file size: {file_size_str}')

    # Print the output file name
    print(f'Output file name: {args.output}\n')
else:
    print('No input words provided.\n')
