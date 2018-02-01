## helot
A collection of useful general utility components to facilitate database, flat 
file and XML access and many more.

  

This library is favouring simplicity over comprehension while it allows the user
to easily build on top of it, in case that he wants to specialize its behaviour.

## Installation
#### Using pip
```
pip3 install helot
```

#### Get the full source code
```git clone https://github.com/jpazarzis/helot```

## Components

#### Mysql database wrapper 
A generator of data rows created by a select statement on a mysql database.

For the database related functionality, It does not implement a traditional ORM 
like solution but a very light wrapper of a select statement, which when
executed it returns python objects containing all the available fields as
properties that can be accessed using the dot notation.

###### Example

Sample code to create and db and call execute query:

```python
import helot

_SQL_INSERT_CAPITAL = '''
Insert into capitals (capital) values ('{capital}')
'''.format

settings = {
    "mysql": {
        "host": "localhost",
        "user": "root",
        "passwd": "vagrant",
        "db": "test"
    }
}

helot.configuration.initialize(settings)

with helot.make_non_query_executor(connect_to_db=False) as execute_query:
    execute_query('DROP Database If EXISTS test')
    execute_query('create Database test')

with helot.make_non_query_executor() as execute_query:
    execute_query('CREATE TABLE capitals (capital varchar(128) DEFAULT NULL)')
    capitals = [
        "London",
        "Washington"
    ]
    for capital in capitals:
        sql = _SQL_INSERT_CAPITAL(capital=capital)
        execute_query(sql)

for row in helot.execute_query('Select capital from capitals'):
    print(row.capital)

```
Executing the script should return the following output:
```
London
Washington

Process finished with exit code 0
```

#### Configuration
Provides an easy to use configuration object that can be globally used and 
initialized by an ini file
