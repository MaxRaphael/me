"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I dont know. I think I now know, it will print a single word in the lsit and then print the next word 
for word in some_words:
    print(word) #It printed every word on different lines

# It will do the same as above
for x in some_words:
    print(x) #It did the same as above

#It will print the entire list
print(some_words) #It pritned the entire list

#I think that this prints a line only if some_words has more than 3 words
if len(some_words) > 5:
    print('some_words contains more than 3 words') #it printed the string because some_words has more than 3 words

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
