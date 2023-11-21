''''
测试向量相关的方法
'''
from Vector import Vector


def test_add():
    '''
    测试两个向量相加
    :return:
    '''
    v1, v2 = Vector([1, 2]), Vector([3, 4])
    # 1+3, 2+4
    assert v1 + v2 == Vector([1 + 3, 2 + 4])
