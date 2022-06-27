CREATE TABLE writer_table
(
    id   SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE book_table
(
    id        INTEGER PRIMARY KEY,
    author_id INTEGER REFERENCES writer_table (id),
    name      TEXT
);

INSERT INTO writer_table (name)
values ('Лев, Толстой');

INSERT INTO writer_table (name)
values ('Александр, Пушкин');

INSERT INTO writer_table (name)
values ('Стивен, Кинг');

INSERT INTO book_table
values (12, 1, 'Анна Каренина');
INSERT INTO book_table
values (135, 1, 'После бала');
INSERT INTO book_table
values (2, 1, 'Три медведя');

INSERT INTO book_table
values (3, 2, 'Капитанская дочка');
INSERT INTO book_table
values (45, 2, 'Дубровский');
INSERT INTO book_table
values (69, 2, 'Евгений Онегин');

INSERT INTO book_table
values (1337, 3, 'Оно');
INSERT INTO book_table
values (322, 3, 'Сияние');
