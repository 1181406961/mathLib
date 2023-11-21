import math
from typing import Union, Iterable

from globals import EPSILON

Number = Union[int, float]


class Vector:

    def __init__(self, lst: Iterable[Number]):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""

    def __add__(self, another: 'Vector'):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector((a + b for a, b in zip(self, another)))

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."
        return Vector((a - b for a, b in zip(self, another)))

    def norm(self):
        """返回向量的模"""

    def normalize(self):
        """返回向量的单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")

    def dot(self, another):
        """向量点乘，返回结果标量"""
        assert len(self) == len(another), \
            "Error in dot product. Length of vectors must be same."

    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""

    def __rmul__(self, k):
        """返回数量乘法的结果向量：k * self"""

    def __truediv__(self, k):
        """返回数量除法的结果向量：self / k"""

    def __pos__(self):
        """返回向量取正的结果向量"""

    def __neg__(self):
        """返回向量取负的结果向量"""

    def __iter__(self):
        """返回向量的迭代器"""
        return iter(self._values)

    def __getitem__(self, index):
        """取向量的第index个元素"""

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __eq__(self, other: 'Vector'):
        if not isinstance(other, Vector) or len(self) != len(other):
            return False
        return all(a == b for a, b in zip(self, other))
