--Create categories
INSERT INTO products_productcategory (name) VALUES('Consoles');
INSERT INTO products_productcategory (name) VALUES('Games');
INSERT INTO products_productcategory (name) VALUES('Other');

--Create products
INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('NINTENDO 64', 'The Nintendo 64 was one of the first gaming consoles to have four controller ports.The most graphically demanding Nintendo 64 games that arrived on larger 32 or 64 MB cartridges are the most advanced and detailed of the 32-bit/64-bit generation. In order to maximize use of the Nintendo 64 hardware developers had to create their own custom microcode. Nintendo 64 games running on custom microcode benefited from much higher polygon counts in tandem with more advanced lighting, animation, physics and AI routines than its 32-bit competition.', 2, 99.95, false, 'NINTENDO');
INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('Sega Genesis Model 2', 'Go with SEGA GENESIS, the leader in 16-bit video game technology, and get it all! Ultra-challenging gameplay. Superior arcade-quality graphics Digital Sound and stereo music synthesizer. Realistic voices. With many hits to choose from.', 2, 49.95, false, 'SEGA');
INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('NINTENDO GameCube', 'GameCube is Nintendo''s first video game console to access game data from a disk, not a cartridge. The processor and disk drive perform together at lightening speed to make load times imperceptible. This stylish system gives developers the creative power to get great results far more quickly than with any other format.', 2, 149.95, false, 'NINTENDO');
INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('Nintendo Entertainment System','The Nintendo Entertainment System (shortened as NES) also known as the Family Computer or Famicom in Japan is the first video game console made by Nintendo in Japan, Europe, the United States. It came out in 1985 in the United States and was very popular.', 2, 99.99, false, 'NINTENDO');

--Create images for products
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://cdn11.bigcommerce.com/s-x2tp8/images/stencil/1000x1000/products/8790/8041/Sega_Genesis_Console_Model_2__60377.1584552605.jpg?c=2', 2);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://upload.wikimedia.org/wikipedia/commons/e/e9/Nintendo-64-wController-L.jpg', 1);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://media.gamestop.com/i/gamestop/10160759/Nintendo-64-Green?$zoom$', 1);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://www.retrocollect.com.au/image/catalog/games/console/N64-Console-Set.jpg', 1);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://www.denofgeek.com/wp-content/uploads/2018/04/underrated-sega-genesis-games.png?resize=768%2C432', 2);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/GameCube-Set.jpg/2880px-GameCube-Set.jpg', 3);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/NES-Console-Set.jpg/2880px-NES-Console-Set.jpg', 4);

