import pytest
from main import BooksCollector

class TestBooksCollector:



    def test_add_new_book_set_one_book_without_genre_add_book_name_in_dict(self, collector, book_name = '7'):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre and collector.books_genre[book_name] == ''

    @pytest.mark.parametrize('book_name', ['', 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq' ])
    def test_add_new_book_set_book_len_0_or_41_not_add_in_dict(self, collector,book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_set_book_genre_set_book_name_and_genre_return_dict_name_keys_and_genre_values(self, collector):
        collector.add_new_book('7')
        collector.set_book_genre('7', 'Ужасы')
        assert collector.books_genre['7'] == 'Ужасы'


    def test_get_book_genre_set_book_name_and_genre_return_genre(self, collector):
        collector.add_new_book('7')
        collector.set_book_genre('7', 'Ужасы')
        assert collector.get_book_genre('7') == 'Ужасы'

    def test_get_books_with_specific_genre_set_book_name_and_genre_return_list_name(self,collector):
        collector.add_new_book('7')
        collector.set_book_genre('7','Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['7']



    def test_get_books_genre_set_book_name_and_genre_return_dict_name_genre(self,collector):
        collector.add_new_book('7')
        collector.set_book_genre('7', 'Ужасы')
        assert collector.get_books_genre() == {'7':'Ужасы'}

    @pytest.mark.parametrize('name ,genre', [['Borat', 'Комедии'], ['Doom', 'Фантастика'],['Up','Мультфильмы']])
    def test_get_books_for_children_set_books_name_and_genre_return_list_book_name(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [name]

    def test_add_book_in_favorites_set_new_book_and_genre_add_book_name_in_list(self, collector):
        collector.add_new_book('7')
        collector.set_book_genre('7','Фантастика')
        collector.add_book_in_favorites('7')
        assert '7' in collector.favorites

    @pytest.mark.parametrize('name ,genre', [['7', 'Ужасы'], ['Doom', 'Фантастика']])
    def test_delete_book_from_favorites_set_2_favourite_books_1_delete_book_1_in_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('7')
        for i in collector.favorites:
            assert 'Doom' in i and '7' not in i

    @pytest.mark.parametrize('name ,genre', [['7', 'Ужасы'], ['Doom', 'Фантастика']])
    def test_get_list_of_favorites_books_set_book_name_genre_return_list_book_name(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]









