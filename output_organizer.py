from book import Book
from library import Library
from typing import List, Dict
from submit import LibraryBooksTuple, SubmitInfo

result_dict = {}

def update_result_dict(updated_result_dict : Dict[Library, List[Book]]):
    for key in updated_result_dict:
        result_dict.setdefault(key, []).extend(updated_result_dict[key])

def finish_run():
    result = SubmitInfo([])
    for key in result_dict:
        result.librarys_selected_with_books.append(LibraryBooksTuple(key, result_dict[key]))