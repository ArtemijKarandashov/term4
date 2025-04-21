import pytest
from custom_exceptions import NegativeHeightException, ZeroHeightException
from binary_tree_task import generate_tree, generate_tree_rec


def test_generate_same_trees():
    bin_tree = {}
    bin_tree_rec = {}
    generate_tree_rec(tree = bin_tree_rec)
    generate_tree(tree = bin_tree)# Тут такие костыли только потому опреатор == отказывается выполнять рекурсию и выдает None
    assert bin_tree == bin_tree_rec 
    

def test_negative_height():
    with pytest.raises(NegativeHeightException):
        generate_tree(height=-1)


def test_negative_height_rec():
    with pytest.raises(NegativeHeightException):
        generate_tree_rec(height=-1)


def test_some_tree():
    some_bin_tree = {}
    generate_tree(tree = some_bin_tree,height=3)
    assert some_bin_tree == {1: [{4: [{13: []}, {11: []}]}, {2: [{7: []}, {5: []}]}]}


def test_zero_height():
    with pytest.raises(ZeroHeightException):
        generate_tree(height=0)


def test_zero_height_rec():
    with pytest.raises(ZeroHeightException):
        generate_tree_rec(height=0)