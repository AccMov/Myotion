from enum import Enum

class X:
    id : int
    desc : str
    tail: bool = field(repr=False, default=True)

class Y(X, Enum):
    A = 0, 'a'
    B = 1, 'b'

print(Y.A)