## Tarea 2: Ejercicios de Python

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%202/Tarea2.md) para ver cómo se hizo la Tarea 2**

Haremos algunos de los ejercicios de [Basic Python Exercises](https://developers.google.com/edu/python/exercises/basic).

### Ejercicio 1

Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.

Note: python does not have a ++ operator, but += works.


### Ejercicio 2

Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.


### Ejercicio 3

Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.


### Ejercicio 4
Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged.


### Ejercicio 5

Read any text file specified on the command line. Do a simple split() on whitespace to obtain all the words in the file. Rather than read the file line by line, it's easier to read it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file to a list of all the words that immediately follow that word in the file. The list of words can be be in any order and should include duplicates. So for example the key "and" might have the list ["then", "best", "then", "after", ...] listing all the words which came after "and" in the text. We'll say that the empty string is what comes before the first word in the file.

With the mimic dict, it's fairly easy to emit random text that mimics the original. Print a word, then look up what words might come next and pick one at random as the next work. Use the empty string as the first word to prime things. If we ever get stuck with a word that is not in the dict, go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a random.choice(list) method which picks a random element from a non-empty list.

For fun, feed your program to itself as input. Could work on getting it to put in linebreaks around 70 columns, so the output looks better.
