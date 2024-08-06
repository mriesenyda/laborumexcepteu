from typing import Tuple

class DisjointTriple:
    def __init__(self, first: bool, second: bool, third: bool):
        self.first = first
        self.second = second
        self.third = third

def get_nightmare() -> DisjointTriple:
    # Your implementation here
    return DisjointTriple(True, False, True)  # Example values
