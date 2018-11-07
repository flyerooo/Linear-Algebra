class Vector:
    def __init__(self, lst):
        self._values = lst

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __iter__(self, item):
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
