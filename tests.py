from main import BooksCollector


class TestBooksCollector:

    def test_books_rating(self):
        collector = BooksCollector()
        collector.books_rating = {'name': 1}

        assert collector.books_rating == {'name': 1}

    def test_favorites(self):
        collector = BooksCollector()
        collector.favorites = [1, 'Hello World!']

        assert collector.favorites == [1, 'Hello World!']

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_rating) == 2

    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.books_rating) == 1

    def test_add_new_book_default_rating_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_set_book_rating_set_10_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 10)

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 10

    def test_set_book_rating_set_rating_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)

        assert collector.books_rating['Гордость и предубеждение и зомби'] != 11

    def test_set_book_rating_set_rating_lower_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        assert collector.books_rating['Гордость и предубеждение и зомби'] != 0

    def test_set_book_rating_set_rating_book_which_is_not(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)

        try:
            collector.books_rating['Гордость и предубеждение и зомби']
        except KeyError:
            return True

    def test_get_book_rating_at_the_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_book_rating_get_rating_book_which_is_not(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    def test_get_books_rating_get_the_added_book_as_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert collector.get_books_rating() == collector.books_rating

    def test_get_books_with_specific_rating_get_book_with_rating_5(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('PyTest для чайников')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('PyTest для чайников', 5)

        assert (collector.get_books_with_specific_rating(5) == ['Гордость и предубеждение и зомби', 'PyTest для чайников']
               and collector.books_rating['Гордость и предубеждение и зомби'] == 5 and collector.books_rating['PyTest для чайников'] == 5)

    def test_get_books_with_specific_rating_get_rating_for_which_there_is_no_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert collector.get_books_with_specific_rating(3) == []

    def test_add_book_in_favorites_add_two_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('PyTest для чайников')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.favorites == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_add_book_which_is_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert  collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить') == None

    def test_add_book_in_favorites_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('PyTest для чайников')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('PyTest для чайников')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('PyTest для чайников')

        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_delete_book_which_is_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить') == None

    def test_get_list_of_favorites_books_get_two_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('PyTest для чайников')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == collector.favorites
