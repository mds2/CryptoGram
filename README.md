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

# Hashing

# Search
