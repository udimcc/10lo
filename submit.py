from dataclasses import dataclass

@dataclass
class SubmitInfo():
	librarys_selected_with_books : int # list[LibraryBooksTuple]

@dataclass
class LibraryBooksTuple:
	library : int # Libray
	books_selected : int # list[Book] 