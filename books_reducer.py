import math
from typing import List, Dict
from collections import defaultdict
from library import Library
from book import Book


def reduce_books(all_libs: List[Library], activated_indicies: List[int], days_remaining:int):
    libs = _get_activated_libs(all_libs, activated_indicies)
    _crop_libs(libs, days_remaining)
    dups = _get_dups(libs)

    for dup_book, dup_book_libs in dups.items():
        min_spd_lib = min(dup_book_libs, key=lambda l: _get_spd(l))
        max_spd_lib = max(dup_book_libs, key=lambda l: _get_spd(l))

        chosen_lib = None
    
        # All spd are equal
        if min_spd_lib == max_spd_lib:
            min_last_book_val_lib = min(dup_book_libs, key=lambda lib: lib.books[-1].score)
            chosen_lib = min_last_book_val_lib
        else:
            chosen_lib = min_spd_lib

        dup_book_libs.remove(chosen_lib)

        for lib in dup_book_libs:
            lib.books.remove(dup_book) 

def _get_activated_libs(libs, activated_indicies):
    activated_libs = []
    for i, lib in enumerate(libs):
        if i in activated_indicies:
            activated_libs.append(lib)

    return activated_libs

def _crop_libs(libs: List[Library], days_remaining):
    for lib in libs:
        max_books = days_remaining * lib.books_per_day
        lib.books = lib.books[:max_books]

def _get_dups(libs: List[Library]) -> Dict[Book, Library]:
    books_to_libs = defaultdict(list)
    for lib in libs:
        for book in lib.books:
            books_to_libs[book].append(lib)

    dups = {}
    for book, libs in books_to_libs.items():
        if len(libs) > 1:
            dups[book] = libs

    return dups

def _get_spd(lib: Library):
    return math.ceil(len(lib.books) / lib.books_per_day)
