from book import Book
from library import Library
from typing import List, Dict
from submit import LibraryBooksTuple, SubmitInfo, submit_info_to_submit_file

result_dict = {}

def update_result_dict(updated_result_dict : Dict[int, List[Book]]):
    for key in updated_result_dict:
        result_dict.setdefault(key, []).extend(updated_result_dict[key])

def remove_scanned_books(library_list : List[Library], activated_library_indices : List[int], days_to_remove: int):
    updated_result_dict = {}
    for index in activated_library_indices:
        updated_result_dict[library_list[index].id] = []
        for day in range(days_to_remove):
            for books_taken in range(library_list[index].books_per_day):
                updated_result_dict[library_list[index].id].append(library_list[index].books.pop(0))
    update_result_dict(updated_result_dict)

def finish_run(library_list : List[Library]):
    result = SubmitInfo([])
    for key in result_dict:
        selected_library = None
        for library in library_list:
            if library.id == key:
                selected_library = library
        assert("SOMEHOW LIBRARY DOESN'T EXIST")
        result.librarys_selected_with_books.append(LibraryBooksTuple(key, selected_library))
    submit_info_to_submit_file("output.txt", result)
