# install
sudo pip install pythonpy; alias py='pythonpy'

# arithmetic
$ py '24 * 60 ** 2'
86400

# floating point numbers
$ py '1.0/98'
0.010204081632

# number sequence
$ py 'range(3)'
0
1
2

# list comprehensions
$ py '[x**2 for x in range(1,5)]'
1
4
9
16

# math library usage
$ py 'math.exp(1)'
2.71828182846

# random library usage
$ py 'random.random()'
0.103173957713

# multiply each line of input by 7.
$ py 'range(3)' | py -x 'int(x)*7'
0
7
14

# append ".txt" to each line of input
$ py 'range(3)' | py -x 'x + ".txt"'
0.txt
1.txt
2.txt

# Sometimes you want to treat the input as a python list.
# reverse a list
$ py 'range(4)' | py -l 'sorted(l, reverse=True)'
3
2
1
0

# sum a list of numbers
$ py 'range(4)' | py -l 'sum(int(x) for x in l)'
6

# count the lines of input
$ py 'range(17)' | py -l 'len(l)'
17

# Other times you just want to filter out lines from the input.
# get only even numbers 
$ py 'range(8)' | py -x 'x if int(x)%2 == 0 else None'
0
2
4
6

# The shorthand -fx (filter on x) is also available.
# get only odd numbers
$ py 'range(8)' | py -fx 'int(x)%2 == 1'
1
3
5
7

# get words starting with "and"
$ cat /usr/share/dict/words | py -fx 're.match(r"and", x)' | head -5
and
andante
andante's
andantes
andiron

#get verbs starting with ba
$ cat /usr/share/dict/words | py -fx 're.match(r"ba.*ing$", x)' | head -5
baaing
babbling
babying
babysitting
backbiting

# get long palindromes
$ cat /usr/share/dict/words | py -fx 'x==x[::-1] and len(x) >= 5' | head -5
civic
deified
kayak
level
ma'am

# ignore AttributeErrors if they pop up with (--i).
# get the local network ip
$ ifconfig | py -x --i 're.search(r"192\.168[\d\.]+", x).group()'
192.168.1.41
