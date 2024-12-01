CREATE TABLE library.books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT NOT NULL,
    ISBN VARCHAR(20) UNIQUE NOT NULL,
    copies INT NOT NULL DEFAULT 1
);


CREATE TABLE library.loans (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    borrower_name VARCHAR(255) NOT NULL,
    borrowed_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

CREATE TABLE library.reservations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    reserver_name VARCHAR(255) NOT NULL,
    reservation_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-------------------------------------------------- add data
-- Add books data with 10 copies each, duplicates removed
INSERT INTO library.books (book_name, author, year_published, ISBN, copies) VALUES
('1984', 'George Orwell', 1949, '9780451524935', 10),
('Pride and Prejudice', 'Jane Austen', 1813, '9780141040349', 10),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565', 10),
('The Catcher in the Rye', 'J.D. Salinger', 1951, '9780316769488', 10),
('Moby-Dick', 'Herman Melville', 1851, '9780142437247', 10),
('War and Peace', 'Leo Tolstoy', 1869, '9780199232765', 10),
('The Odyssey', 'Homer', -700, '9780140268867', 10),
('Crime and Punishment', 'Fyodor Dostoevsky', 1866, '9780140449136', 10),
('The Brothers Karamazov', 'Fyodor Dostoevsky', 1880, '9780374528379', 10),
('Great Expectations', 'Charles Dickens', 1861, '9780141439563', 10),
('Jane Eyre', 'Charlotte Bronte', 1847, '9780142437209', 10),
('Wuthering Heights', 'Emily Bronte', 1847, '9780141439556', 10),
('Frankenstein', 'Mary Shelley', 1818, '9780486282114', 10),
('Dracula', 'Bram Stoker', 1897, '9780486411095', 10),
('The Divine Comedy', 'Dante Alighieri', 1320, '9780142437223', 10),
('Les Miserables', 'Victor Hugo', 1862, '9780451419439', 10),
('Anna Karenina', 'Leo Tolstoy', 1877, '9780143035008', 10),
('Madame Bovary', 'Gustave Flaubert', 1856, '9780140449129', 10),
('The Count of Monte Cristo', 'Alexandre Dumas', 1844, '9780140449266', 10),
('The Iliad', 'Homer', -750, '9780140275360', 10),
('Catch-22', 'Joseph Heller', 1961, '9781451626650', 10),
('The Hobbit', 'J.R.R. Tolkien', 1937, '9780547928227', 10),
('Fahrenheit 451', 'Ray Bradbury', 1953, '9781451673319', 10),
('Brave New World', 'Aldous Huxley', 1932, '9780060850524', 10),
('Animal Farm', 'George Orwell', 1945, '9780451526342', 10),
('Gone with the Wind', 'Margaret Mitchell', 1936, '9781451635621', 10),
('The Alchemist', 'Paulo Coelho', 1988, '9780061122415', 10),
('Lord of the Flies', 'William Golding', 1954, '9780399501487', 10),
('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 1967, '9780060883287', 10),
('Slaughterhouse-Five', 'Kurt Vonnegut', 1969, '9780440180296', 10),
('Don Quixote', 'Miguel de Cervantes', 1605, '9780060934347', 10),
('Ulysses', 'James Joyce', 1922, '9780199535675', 10),
('The Sound and the Fury', 'William Faulkner', 1929, '9780679732242', 10),
('Beloved', 'Toni Morrison', 1987, '9781400033416', 10),
('Lolita', 'Vladimir Nabokov', 1955, '9780679723165', 10),
('The Metamorphosis', 'Franz Kafka', 1915, '9780486290300', 10),
('The Stranger', 'Albert Camus', 1942, '9780679720201', 10),
('The Grapes of Wrath', 'John Steinbeck', 1939, '9780143039433', 10),
('Heart of Darkness', 'Joseph Conrad', 1899, '9780141441672', 10),
('Invisible Man', 'Ralph Ellison', 1952, '9780679732761', 10),
('On the Road', 'Jack Kerouac', 1957, '9780140283297', 10),
('To the Lighthouse', 'Virginia Woolf', 1927, '9780156907392', 10),
('A Farewell to Arms', 'Ernest Hemingway', 1929, '9780684801469', 10),
('The Sun Also Rises', 'Ernest Hemingway', 1926, '9780743297332', 10),
('The Old Man and the Sea', 'Ernest Hemingway', 1952, '9780684801223', 10),
('Mrs. Dalloway', 'Virginia Woolf', 1925, '9780156628709', 10),
('Sense and Sensibility', 'Jane Austen', 1811, '9780141439662', 10),
('Little Women', 'Louisa May Alcott', 1868, '9780142408766', 10),
('Rebecca', 'Daphne du Maurier', 1938, '9780380730407', 10),
('The Handmaid\'s Tale', 'Margaret Atwood', 1985, '9780385490818', 10),
('The Picture of Dorian Gray', 'Oscar Wilde', 1890, '9780141439570', 10),
('A Tale of Two Cities', 'Charles Dickens', 1859, '9780141439600', 10),
('David Copperfield', 'Charles Dickens', 1850, '9780140439441', 10),
('Middlemarch', 'George Eliot', 1871, '9780141439549', 10),
('Oliver Twist', 'Charles Dickens', 1838, '9780141439747', 10),
('Gulliver\'s Travels', 'Jonathan Swift', 1726, '9780141439495', 10),
('The Scarlet Letter', 'Nathaniel Hawthorne', 1850, '9780142437261', 10),
('The Secret Garden', 'Frances Hodgson Burnett', 1911, '9780064401883', 10),
('The Hunchback of Notre-Dame', 'Victor Hugo', 1831, '9780140443530', 10),
('The Call of the Wild', 'Jack London', 1903, '9780486264720', 10),
('White Fang', 'Jack London', 1906, '9780486269688', 10),
('Treasure Island', 'Robert Louis Stevenson', 1883, '9780141321004', 10),
('Robinson Crusoe', 'Daniel Defoe', 1719, '9780141439829', 10),
('The Three Musketeers', 'Alexandre Dumas', 1844, '9780140449273', 10),
('Twenty Thousand Leagues Under the Sea', 'Jules Verne', 1870, '9780140432718', 10),
('The Time Machine', 'H.G. Wells', 1895, '9780451528551', 10),
('Journey to the Center of the Earth', 'Jules Verne', 1864, '9780141441979', 10),
('The War of the Worlds', 'H.G. Wells', 1898, '9780451530653', 10),
('Dracula', 'Bram Stoker', 1897, '9780142437308', 10),
('The Jungle Book', 'Rudyard Kipling', 1894, '9780141325293', 10),
('The Tale of Peter Rabbit', 'Beatrix Potter', 1902, '9780723247708', 10),
('Charlotte\'s Web', 'E.B. White', 1952, '9780064400558', 10),
('Alice\'s Adventures in Wonderland', 'Lewis Carroll', 1865, '9780141321073', 10),
('The Wonderful Wizard of Oz', 'L. Frank Baum', 1900, '9780486291160', 10),
('Anne of Green Gables', 'L.M. Montgomery', 1908, '9780141321592', 10),
('The Wind in the Willows', 'Kenneth Grahame', 1908, '9780141321134', 10),
('Peter Pan', 'J.M. Barrie', 1911, '9780141322575', 10),
('Black Beauty', 'Anna Sewell', 1877, '9780141321035', 10),
('Heidi', 'Johanna Spyri', 1881, '9780141322568', 10),
('The Secret of Chimneys', 'Agatha Christie', 1925, '9780007119297', 10),
('Persuasion', 'Jane Austen', 1817, '9780141439683', 10),
('Northanger Abbey', 'Jane Austen', 1818, '9780141439799', 10),
('Emma', 'Jane Austen', 1815, '9780141439584', 10),
('Mansfield Park', 'Jane Austen', 1814, '9780141439805', 10),
('Love in the Time of Cholera', 'Gabriel Garcia Marquez', 1985, '9780307389732', 10),
('The Kite Runner', 'Khaled Hosseini', 2003, '9781594631931', 10),
('A Thousand Splendid Suns', 'Khaled Hosseini', 2007, '9781594483851', 10),
('The Road', 'Cormac McCarthy', 2006, '9780307387899', 10),
('Life of Pi', 'Yann Martel', 2001, '9780156027328', 10),
('The Book Thief', 'Markus Zusak', 2005, '9780375842207', 10),
('The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005, '9780307454546', 10);