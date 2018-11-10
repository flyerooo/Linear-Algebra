class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状：（行数，列数）"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

