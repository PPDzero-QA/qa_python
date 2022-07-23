# Список реализованных тестов

- Проверка метода __init\__
  - Проверка атрибута books_rating
  - Проверка атрибута favorites
- Проверка метода add_new_book
  - Проверка добавления двух книг
  - Нельзя добавить одну и туже книгу дважды
  - Проверка что при добавлении книги у нее по умолчанию установлен рейтинг 1
- Проверка метода set_book_rating
  - Проверка что можно установить корректный рейтинг книге (от 1 до 10)
  - Книге нельзя установить рейтинг больше 10 (11)
  - Книге нельзя установить рейтинг меньше 1 (0)
  - Нельзя установить рейтинг книге, которой не существует
- Проверка метода get_book_rating
  - Проверка получения рейтинга книги (рейтинг устанавливается по умолчанию)
  - Нельзя получить рейтинг книги, которой не существует
- Проверка метода get_books_rating
  - Проверка что метод возвращает добавленные книги как словарь
- Проверка метода get_books_with_specific_rating
  - Метод возвращает список книг с указанным рейтингом и что у этих книг точно этот рейтинг (5)
  - Если нет книг по указанному рейтингу, метод возвращает пустой список
- Проверка метода add_book_in_favorites
  - Проверка добавления двух книг в избранное (2 книги из 3 существующих)
  - Нельзя добавить книгу в избранное если ее нет в переменной books_rating
  - Нельзя добавить одну и туже книгу в избранное дважды
- Проверка метода delete_book_from_favorites
  - Удаление из избранного двух книг из трёх
  - Книгу нельзя удалить из избранного если ее нет в избранном
- Проверка метода get_list_of_favorites_books
  - Проверка что метод выводит список книг из избранного такой же какой хранится в переменной favorites