#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        s = "50000  23 \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 50000)
        self.assertEqual(j, 23)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 19)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 124)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 88)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 173)

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 0)

    def test_eval_5 (self) :
        v = collatz_eval(1, 50000)
        self.assertEqual(v, 323)

    def test_eval_6 (self) :
        v = collatz_eval(533, 503)
        self.assertEqual(v, 123)

    def test_eval_7 (self) :
        v = collatz_eval(2, 1)
        self.assertEqual(v, 1)

    def test_eval_8 (self) :
        v = collatz_eval(24532, 50000)
        self.assertEqual(v, 323)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 19\n100 200 124\n201 210 88\n900 1000 173\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
