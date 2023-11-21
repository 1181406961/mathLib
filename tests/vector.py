''''
测试向量相关的方法
'''
import math

from Vector import Vector
from globals import EPSILON


def test_add():
    '''
    测试两个向量相加
    :return:
    '''
    v1, v2 = Vector([1, 2]), Vector([3, 4])
    # 1+3, 2+4
    assert v1 + v2 == Vector([1 + 3, 2 + 4])


def test_sub():
    '''
    测试两个向量相减
    :return:
    '''
    v1, v2 = Vector([1, 2]), Vector([3, 4])
    assert v2 - v1 == Vector([3 - 1, 4 - 2])


def test_eq():
    '''
    :return:
    '''
    assert (Vector([1, 1]) == None) is False
    assert (Vector([1, 1]) == [1, 1]) is False


def test_norm():
    v = Vector([2, 2])
    assert abs(v.norm() - math.sqrt(2 ** 2 + 2 ** 2)) < EPSILON


def test_normalize():
    v = Vector([2, 2])
    assert abs(v.normalize().norm() - 1) < EPSILON
