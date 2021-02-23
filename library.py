from dataclasses import dataclass
from book import Book

@dataclass
class Library:
	id : int
	books : int #list of books actuall but fuck it
	time : int
	books_per_day : int