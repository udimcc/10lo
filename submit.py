from dataclasses import dataclass

@dataclass
class SubmitInfo():
	librarys_selected_with_books : int # list[LibraryBooksTupl]e

@dataclass
class LibraryBooksTuple:
	library : int # Libray
	books_selected : int # list[Book] 

def submit_info_to_submit_file(sf_path, si : SubmitInfo):
	lines_list = []
	librarys_selected_with_books = si.librarys_selected_with_books
	# add the num of libs
	lines_list.append(str(len(librarys_selected_with_books)))

	for lbtuple in librarys_selected_with_books:
		# add the lib id [space] num-of-books
		lines_list.append(f"{str(lbtuple.library.id)} {str(len(lbtuple.books_selected))}")

		# add the books id
		lines_list.append(f"{' '.join([str(book.id) for book in lbtuple.books_selected])}")

	with open(sf_path,'w') as sf:
		#sf.writelines(lines_list)
		sf.write('\n'.join(lines_list) + '\n')

def submit_file_to_submit_info(sf_path ,librarys):
	with open(sf_path) as sf:
		librarys_selected_with_books = []

		num_of_libs = int(sf.readline())

		for lib in range(num_of_libs):
			lib_id, num_of_books = [int(x) for x in sf.readline().split()]
			books_ids = [int(x) for x in sf.readline().split()]

			librarys_selected_with_books.append(
				LibraryBooksTuple(
					librarys[lib_id],
					# finding corresponding books obj to represent in the sumbit info 
					books_ids_to_books(books_ids, librarys[lib_id].books)))

	return SubmitInfo(librarys_selected_with_books)

def books_ids_to_books(books_ids, all_books):
	final_books = []
	for id_num in books_ids:
		final_books.append(next((book for book in all_books if book.id == id_num), None))
	return final_books