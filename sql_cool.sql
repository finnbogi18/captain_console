INSERT INTO products_productcategory (name) VALUES('Consoles');
INSERT INTO products_productcategory (name) VALUES('Games');
INSERT INTO products_productcategory (name) VALUES('Other');

INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('NINTENDO 64', 'The Nintendo 64 was one of the first gaming consoles to have four controller ports.The most graphically demanding Nintendo 64 games that arrived on larger 32 or 64 MB cartridges are the most advanced and detailed of the 32-bit/64-bit generation. In order to maximize use of the Nintendo 64 hardware developers had to create their own custom microcode. Nintendo 64 games running on custom microcode benefited from much higher polygon counts in tandem with more advanced lighting, animation, physics and AI routines than its 32-bit competition.', 2, 99.95, false, 'NINTENDO');
INSERT INTO products_product (name, description, category_id, price, on_sale, manufacturer) VALUES ('Sega Genesis Model 2', 'Go with SEGA GENESIS, the leader in 16-bit video game technology, and get it all! Ultra-challenging gameplay. Superior arcade-quality graphics Digital Sound and stereo music synthesizer. Realistic voices. With many hits to choose from.', 2, 49.95, false, 'SEGA');

INSERT INTO products_productimage (image, product_id_id) VALUES ('https://cdn11.bigcommerce.com/s-x2tp8/images/stencil/1000x1000/products/8790/8041/Sega_Genesis_Console_Model_2__60377.1584552605.jpg?c=2', 2);
INSERT INTO products_productimage (image, product_id_id) VALUES ('https://upload.wikimedia.org/wikipedia/commons/e/e9/Nintendo-64-wController-L.jpg', 1);



https://cdn11.bigcommerce.com/s-x2tp8/images/stencil/1000x1000/products/8790/8041/Sega_Genesis_Console_Model_2__60377.1584552605.jpg?c=2