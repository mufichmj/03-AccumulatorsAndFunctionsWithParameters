"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Mariah Mufich.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # DONE 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    #TEST - DRIVEN DEVELOPMENT

    n = math.pi
    cosine = math.cos(n)
    summary = sum_of_digits(cosine)
    print()
    print('the cosine of pi should be -1')
    print('adding all the numbers in -1 should add to 1')
    print('the cosine of', n, 'is', cosine)
    print('the sum of the numbers in', cosine, 'is', summary)

    n = math.e
    cosine = math.cos(n)
    summary = sum_of_digits(cosine)
    print()
    print('the cosine of pi should be -.9')
    print('adding all the numbers in -.9 should add to .9')
    print('the cosine of', n, 'is', cosine)
    print('the sum of the numbers in', cosine, 'is', summary)

    n = 1.5707
    cosine = math.cos(n)
    summary = sum_of_digits(cosine)
    print()
    print('the cosine of pi/2 degrees should be 0')
    print('adding all the numbers in 0 should add to 0')
    print('the cosine of', n, 'is', cosine)
    print('the sum of the numbers in', cosine, 'is', summary)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
    sum_square_roots(5)

    sum_square_roots(3)

    sum_square_roots(8)


def sum_square_roots(n):

    answer = 0
    for k in range(n):
        answer += math.sqrt(2 * (k+1))
        #answer = answer + math.sqrt(2*n)
    print(answer)


    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

def sum_of_digits(number):

    if number < 0:

        number = -number



    digit_sum = 0

    while True:

        if number == 0:

            break

        digit_sum = digit_sum + (number % 10)

        number = number // 10



    return digit_sum
main()
