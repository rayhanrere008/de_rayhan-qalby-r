CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    category_id INTEGER REFERENCES categories(id),
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(id),
    user_id INTEGER REFERENCES users(id),
    content VARCHAR NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NULL
);

-- Insert Data di Tabel users
INSERT INTO users (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3'),
('user4', 'password4'),
('user5', 'password5');

-- Insert Data di Tabel Categories
INSERT INTO categories (name) VALUES
('Electronics'),
('Clothing'),
('Music'),
('Books'),
('Sports & Outdoors');

-- Insert Data di Tabel Posts
INSERT INTO posts (user_id, category_id, title, content) VALUES
(1, 1, 'Xiaomi 13T Dominasi', 'Xiaomi 13T menjadi handphone dengan kualitas yang sangat bagus di kelas mid range.'),
(2, 2, 'Outfit Skena atau Starboy?', 'Semua outfit memiliki ciri khas dan kenyamanannya sendiri jadi tidak bisa dibeda-bedakan'),
(3, 3, 'Musik Taylor Swift Cocok Untuk Mahasiswa', 'Faktanya banyak sekali mahasiswa mendengarkan musik taylor swift dalam keseharian dan kuliah mereka'),
(4, 4, 'Must-Read Books of the Year', 'Novel Harry Potter tetap menjadi terbaik di kalangan orang pencinta genre supranatural'),
(5, 5, 'Indonesia Kalahkan Vietnam', 'Gol Tunggal Egy Maulana membuat Indonesia Menaklukan Vietnam di GBK');

-- Insert Data di Tabel Comments
INSERT INTO comments (post_id, user_id, content) VALUES
(1, 1, 'Great review, very informative!'),
(2, 2, 'I love skena outfit'),
(3, 3, 'Hindia tetap menjadi terbaik bagi saya'),
(4, 4, 'These book recommendations are fantastic!'),
(5, 5, 'Semoga di Leg 2 di Vietnam menang lagi');
