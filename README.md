# PyWordForWord

Python version of WordForWord - a series of text processing methods

For the sake of this lab, words are not and do not have punctuation.
So treat punctuation like whitespace.

Four phases of text processing to do. Write a method for each one.

`func print(filename)`
Write a method that reads the contents of a file, line by line, and creates a String object,
making sure all the newlines are preserved.

`func wc(String input)`
commonly called "wc"; count the number of characters in a file, number of words, number of lines.
Returns an tuple with the number of lines, words and characters.

`func wordFrequency(String input)`
word count. words in the string, produce a dictionary with (str word, int numOfTimes).

`func letterFrequency(String input)`
letter frequency, write a program that collects the frequency of each letter within the input. produces a dictionary with letters as the key, number of occurences as value.

Input like `The Blue Fox is blue.` would produce a map like

| Word | Count |
|------|-------|
| the  | 1     |
| blue | 2     |
| fox  | 1     |
| is   | 1     |

The class would also have a method `frequency(word)` which returns the relative frequency of the word in the input text.
So `frequency("blue")` would return 0.4 as a result.
This means you need to track the total number of words in the input, 
as frequency is `numberOfOccurences / totalNumberOfWords`

You probably need to make this all methods on a c   lass, not just a simple
script file. That way the total number of words can be kept ina instance var, making
the frequency calculation very easy.

notice how if you had a `letterFrequency(letter)` it'd work too.

Finally, read thru all the files in `testdata/` and perform the text processing on
each file. Capture all the output results into a file and post that as `ResultsOfProcessing.txt` in the repo.

Take a look at Part Deux of this lab -> [Notes](Notes.md)