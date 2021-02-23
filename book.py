from dataclasses import dataclass
from typing import List
import operator

@dataclass
class Book:
	id : int
	score : int

def book_sorter(books: List[Book]) -> List[Book]:
    return sorted(books, key=operator.attrgetter('score'), reverse=True)
