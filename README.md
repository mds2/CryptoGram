### Search-based cryptogram solver

I wrote this after becoming frustrated with the shortcomings of
my MCMC-based cryptogram solver.

It attempts to find the original message and substitution cipher
of a message encrypted with a simple substition cipher based on
matching dictionary words.

It often runs into two kinds of trouble :
With long inputs, the search may take a long time to complete, while, with
shorter inputs, it often finds far too many plausible source messages
and substitution ciphers.

## How to use it

    $ python3
    Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
    [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from CryptoSolve import *
    >>> msg = "here is a message we would like to encrypt"
    >>> c = WordUtil.random_cipher()
    >>> print(c.apply(msg))
    smgm xu d emuudcm im iprfa fxnm yp mtlgqby
    >>> import itertools
    >>> solutions = solve("smgm xu d emuudcm im iprfa fxnm yp mtlgqby")
    >>> for solution in itertools.islice(solutions, 0, 10):
    ...   print(solution)
    ... 
    here us a message fe flick cube yl entropy
    vere us a message fe flick cube yl entropy
    were us a message fe flick cube yl entropy
    dere us a message fe flick cube yl entropy
    
and then it takes an awfully long time to find the next six.

## How it works

It does a priority queue (A star) search through partial cipher solutions
by looking at the dictionary words a word can map to, and trying the partial
cipher induced by each mapping.  It stops a given search branch
when the partial mapping it's constructing reaches a contradiction (one letter
mapping to two, or two letters mapping to one)

# Hashing

To quickly find the words that a given scrambled word can map to it relies
on a pre-processed data structure with a simple hashing trick.

It goes through the letters of a word in order, and the first letter it finds
it maps to "a", the second unique letter it finds it maps to "b", etc.

So "abba" maps to "abba".  "deed" also maps to "abba".
And "fruitjuice" maps to "abcdefcdgh" -- note the recurring "cd" for the letters
"u" and "i"

    $ python3
    Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
    [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from CryptoSolve import *
    >>> WordHash.hash_word("fruitjuice")
    'abcdefcdgh'
    >>> WordHash.hash_word("bloatjoads")
    'abcdefcdgh'
    >>> 

Any simple substitution cipher applied to "fruitjuice" will produce the same
hash.

It then pre-populates two maps (one from a very thorough dictionary, and one
from a smaller word corpus of more common words) to be able to quickly
look up which words a given word can hash to.

# Search

Given a cipher-encryptd string, it first lowercases it, removes all non
alphabetic characters other than spaces, and breaks it into words.

It then constructs a priority queue of partial solutions paired with
words in the encrypted text that haven't been considered.

Then, for each word in the list (TODO : play with order here) it first goes
through each word it might hash to in the simple dictionary, and, for any
that are compatible with the existing partial cipher solution, it
places that solution onto the priority queue with the same priority as the
partial soluton it deduced it from (incorporating the new word into the
partial cipher and removing a word from the words to be looked at when
constructing the new partial solution).  It does the same thing for the
extensive dictionary, but adds 1 to the priority for each of these partial
solutions.

The dictionary-building step removes words from the thorough dictionary
that also occur in the simple dictionary, to avoid covering the same
solutions twice.
