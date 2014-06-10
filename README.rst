Installation
------------

::

  sudo pip install pythonpy && alias py='pythonpy'

::

For a permanent alias (For Bash users):

::

  echo "alias py='pythonpy'" >> ~/.bashrc
  
::

Float arithmetic
----------------

::

  $ py '3 * 1.5'
  4.5

::

Exponentiation
--------------

::

  $ py '7**3'
  343
  
::

Number sequence
---------------

::

  $ py 'range(3)'
  0
  1
  2

::

List comprehensions
-------------------

::

  $ py '[x**2 for x in range(1,5)]'
  1
  4
  9
  16

::

Math library usage
------------------

::

  $ py 'math.exp(1)'
  2.71828182846

::

Random library usage
--------------------

::

  $ py 'random.random()'
  0.103173957713

::

Multiply each line of input by 7.
---------------------------------

::

  $ py 'range(3) | py -x 'int(x)*7'
  0
  7
  14

::
  
Append ".txt" to each line of input
-----------------------------------

::

  $ py 'range(3)' | py -x 'x + ".txt"'
  0.txt
  1.txt
  2.txt

::

Sometimes you want to treat the input as a python list
------------------------------------------------------

Reverse a list
~~~~~~~~~~~~~~

::

  $ py 'range(4)' | py -l 'sorted(l, reverse=True)'
  3
  2
  1
  0

::

Sum a list of numbers
---------------------

::

  $ py 'range(4)' | py -l 'sum(int(x) for x in l)'
  6

::

Count the lines of input
------------------------

::

  $ py 'range(17)' | py -l 'len(l)'
  17

::

Other times you just want to filter out lines from the input
------------------------------------------------------------

Get only even numbers 
~~~~~~~~~~~~~~~~~~~~~

::

  $ py 'range(8)' | py -x 'x if int(x)%2 == 0 else None'
  0
  2
  4
  6

::

The shorthand -fx (filter on x) is also available
-------------------------------------------------

Get only odd numbers
~~~~~~~~~~~~~~~~~~~~
  
::

  $ py 'range(8) | py -fx 'int(x)%2 == 1'
  1
  3
  5
  7

::

Get words starting with "and"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ cat /usr/share/dict/words | py -fx 're.match(r"and", x)' | head -5
  and
  andante
  andante's
  andantes
  andiron

::

Get verbs starting with ba
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ cat /usr/share/dict/words | py -fx 're.match(r"ba.*ing$", x)' | head -5
  baaing
  babbling
  babying
  babysitting
  backbiting

::

Get long palindromes
~~~~~~~~~~~~~~~~~~~~

::

  $ cat /usr/share/dict/words | py -fx 'x==x[::-1] and len(x) >= 5' | head -5
  civic
  deified
  kayak
  level
  ma'am

::

Ignore AttributeErrors if they pop up with (--i)
------------------------------------------------

Get the local network ip
~~~~~~~~~~~~~~~~~~~~~~~~

::
 
  $ ifconfig | py -x --i 're.search(r"192\.168[\d\.]+", x).group()'
  192.168.1.41

::
