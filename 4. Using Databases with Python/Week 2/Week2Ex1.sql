-- 1. Create a SQLITE database or use an existing database and create a table in the database called "Ages": 
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

-- 2. Then make sure the table is empty by deleting any rows that you previously inserted.
DELETE FROM Ages;

-- 3.  Insert these rows and only these rows with the following commands: 
INSERT INTO Ages (name, age) VALUES ('Xin', 17);
INSERT INTO Ages (name, age) VALUES ('Miku', 29);
INSERT INTO Ages (name, age) VALUES ('Dakota', 16);
INSERT INTO Ages (name, age) VALUES ('Sandy', 18);
INSERT INTO Ages (name, age) VALUES ('Jan', 36);

-- 4. Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

-- 5. Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333. 