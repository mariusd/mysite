#!/usr/bin/env python

"""Program for printing numbers in sevenseg format."""

SEVENSEG_DIGITS = """\
 ###           ###    ###           ###    ###    ###    ###    ### 
#   #      #      #      #  #   #  #      #          #  #   #  #   #
#   #      #      #      #  #   #  #      #          #  #   #  #   #
#   #      #      #      #  #   #  #      #          #  #   #  #   #
               ###    ###    ###    ###    ###           ###    ### 
#   #      #  #          #      #      #  #   #      #  #   #      #
#   #      #  #          #      #      #  #   #      #  #   #      #
#   #      #  #          #      #      #  #   #      #  #   #      #
 ###           ###    ###           ###    ###           ###    ### """

def generate_sevenseg(digits):
    """Iterate over lines of digits in seven-segment format.

    >>> print '\\n'.join(generate_sevenseg([1, 2, 3, 4, 5]))
            ###    ###           ### 
        #      #      #  #   #  #    
        #      #      #  #   #  #    
        #      #      #  #   #  #    
            ###    ###    ###    ### 
        #  #          #      #      #
        #  #          #      #      #
        #  #          #      #      #
            ###    ###           ### 

    >>> list(generate_sevenseg([1, 2, 3, 42, 5]))
    Traceback (most recent call last):
    ...
    ValueError: all digits must be in range 0..9
    """
    if not all(0 <= d <= 9 for d in digits):
        raise ValueError("all digits must be in range 0..9")
    for line in SEVENSEG_DIGITS.split('\n'):
        yield "  ".join([line[(7 * i):(7 * i + 5)] for i in digits])

def test(verbose=True):
    """Run all doctests in this module."""
    import doctest
    doctest.testmod(verbose=verbose)

def main():
    """Main method."""
    import sys
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: python sevenseg.py <number>"
        sys.exit(1)
    try:
        number = sys.argv[1]
        print '\n'.join(generate_sevenseg([int(d) for d in number]))
    except ValueError, e:
        print >> sys.stderr, "Error:", e
    
if __name__ == "__main__":
    main()


