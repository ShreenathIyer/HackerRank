'''
When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In a new kind of PDF viewer, the selection of each word is independent of the other words; this means that each rectangular selection area forms independently around each highlighted word.

In this type of PDF viewer, the width of the rectangular selection area is equal to the number of letters in the word times the width of a letter, and the height is the maximum height of any letter in the word.

Consider a word consisting of lowercase English alphabetic letters, where each letter is 1mm wide. Given the height of each letter in millimeters (mm), find the total area that will be highlighted by blue rectangle in mm^2 when the given word is selected in our new PDF viewer.

Input Format:

The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter (i.e., ha, hb, hc,.., hy, hz). 
The second line contains a single word, consisting of lowercase English alphabetic letters.

Constraints:

1 <= h? <= 7, where ? is an English lowercase letter.
Word contains no more than 10 letters.

Output Format:

Print a single integer denoting the area of highlighted rectangle when the given word is selected. The unit of measurement for this is square millimeters (mm^2), but you must only print the integer.

Sample Input:

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output:

9
'''
#!/bin/python

import sys
import string

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()

max_ht = 1

for charac in word:
    ind = string.lowercase.index(charac)
    curr_ht = h[ind]
    if max_ht < curr_ht:
        max_ht = curr_ht

area = len(word) * max_ht
print area
