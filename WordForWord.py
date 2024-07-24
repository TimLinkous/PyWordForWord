import os
import string
from collections import defaultdict, Counter
import re


class WordForWord:
    def __init__(self):
        self.total_words = 0
        self.word_counts = defaultdict(int)
        self.letter_counts = defaultdict(int)

    def print_file(self, filename):
    #reads the contents of a file,  
    # line by line, and creates a String object
        with open(filename, 'r') as file:
            content = file.read()
        return content
    
    def wc(self, input_str):
        #count the number of characters in a file, number of words, 
        # number of lines.
        #Returns an tuple with the number of lines, words and characters.
        lines = input_str.split('\n')
        words = input_str.split()
        characters = len(input_str)
        return (len(lines), len(words), characters)
    
    def word_frequency(self, input_str):
        #words in the string, produce a dictionary with 
        # (str word, int numOfTimes)
        words = input_str.lower().translate(str.maketrans('', '', string.punctuation)).split()
        ## Convert the input string to lowercase and remove punctuation
        self.total_words = len(words)  #Update the total number of words
        for word in words:
            if word in self.word_counts: 
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1  #Count the occurrences of each word
        return dict(self.word_counts) #return word counts as dict
    
    def letter_frequency(self, input_str):
        #collects the frequency of each letter within the input. 
        # produces a dictionary with letters as the key, 
        # number of occurences as value.
        letters = re.findall(r'[a-zA-z]', input_str.lower())
        return Counter(letters) 
    #a way to do it using regex 

    def frequency(self, word):
        #returns the relative frequency of the word in the input text
        word = word.lower()
        return self.word_counts.get(word, 0) / self.total_words if self.total_words > 0 else 0

    def letter_freq(self, letter):
        #returns the relative frequency of the letter in the input text
        letter = letter.lower()
        total_letters = sum(self.letter_counts.values())
        return self.letter_counts.get(letter, 0) / total_letters if total_letters > 0 else 0

    def process_files(self, path):
        #result = []
        result_filename = 'Results_of_Processing2.txt'
        with open(result_filename, 'w') as output_file:
            if os.path.isdir(path):
                for filename in os.listdir(path): #for loop that iterates over each entry in the list returned by os.listdir(directory)
                #filename takes on the value of each entry 
                    filepath = os.path.join(path, filename) #constructs the full file path 
                    if os.path.isfile(filepath):
                        self.process_single_file(filepath, filename, output_file)
            elif os.path.isfile(path):
                self.process_single_file(path, os.path.basename(path), output_file)
        return output_file
                    
    def process_single_file(self, filepath, filename, output_file):                
        content = self.print_file(filepath) #reads the contents of the file specified by filepath.
        lines, words, characters = self.wc(content) #calculates the number of lines, words, and characters in the file content.
        word_freq = self.word_frequency(content)
        letter_freq = self.letter_frequency(content)

        output_file.write(f"File: {filename}\n")
        output_file.write(f"Lines: {lines}, Words: {words}, Characters: {characters}\n")
        output_file.write(f"Word Frequencies:\n")
        for word, count in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
            output_file.write(f"{word}: {count}\n")
        output_file.write("Letter Frequencies:\n")
        for letter, count in sorted(letter_freq.items(), key=lambda item: item[1], reverse=True):
            output_file.write(f"{letter}: {count}\n")

if __name__ == "__main__":
    word_processor = WordForWord()
    #process a single file
    #result_one_file = word_processor.process_files('/Users/timl/PythonWork/PyWordForWord/testdata/testdata2.txt')
    #print(f"Processing complete. Results saved to {result_one_file}")

    #process all files
    dir_result_file = word_processor.process_files('/Users/timl/PythonWork/PyWordForWord/testdata')
    print(f"Processing complete. Results saved to {dir_result_file}")







