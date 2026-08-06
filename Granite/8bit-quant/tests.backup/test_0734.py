import re
import string
from src_0734 import task_func
import pytest

def test_task_func():
    assert task_func("Hello world!") == 2
    assert task_func("This is a test.") == 3
    assert task_func("I am testing this function.") == 6
    assert task_func("I, me, my, myself, we, our, ourselves, you, your, yours, yourself, yourselves, he, him, his, himself, she, her, hers, herself, it, its, itself, they, them, their, theirs, themselves, what, which, who, whom, this, that, these, those, is, are, was, were, be, been, being, have, has, had, having, do, does, did, doing, an, the, and, but, if, or, because, as, until, while, of, at, by, for, with, about, against, between, into, through, during, before, after, above, below, to, from, up, down, in, out, on, off, over, under, again, further, then, once.") == 0
    assert task_func("") == 0