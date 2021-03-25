import string
import random

width = 15
height = 15

grid = [[random.choice(string.uppercase) for i in xrange(0, width) for j in xrange(0, height)]]
word = 'Hello'
word = random.choice([word, word[::-1]])

