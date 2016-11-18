# Lance-Db
Lance Db is a object based key value pair DBMS designed in python. It is one of my personal projects undertaken to enhance dbms concepts.

To use the db.
1.change path to the lance db folder

2.launch python3 interpreter mode

3. then type import lance as db or any suitable name

4. all methods are to be called using the specified name

For Instance: db.open("xyz")

The Basic usage is as follows:

create(“file name”)- create db file with name

open(“file name”)-open to perform operations Note: If file does not exist it only creates a file after giving a y


insert(str key,<generic> value)-insert key, value pair

find( )-returns dictionary of all key :value pairs

find(str key)- returns matching key value pair as a dictionary

delete(str key)-removes the key value pair with the specified key

removedb(“file name”)-removes the specified db 

update(key, value)-updates the entry for key

getdb( )-prints current open db
