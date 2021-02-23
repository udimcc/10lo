from book import Book
from library import Library
from dataclasses import dataclass

def get_input(file_path):
	with open(file_path) as f:
		num_of_books, num_of_libs, days_of_scan = f.readline().split()
		list_of_scored = [int(s) for s in f.readline().split()]

		librarys = []

		for lib in range(int(num_of_libs)):
			book_of_lib, time, books_per_day = f.readline().split()

			books = f.readline().split()
			actual_books = []
			for book_id in books:
				actual_books.append(Book(book_id, list_of_scored[int(book_id)]))
			
			librarys.append(Library(lib, actual_books, time, books_per_day))

	return InputCluster(librarys, num_of_books ,days_of_scan)


@dataclass
class InputCluster:
	librarys : int # list of libs
	num_of_books : int
	days_of_scan : int
