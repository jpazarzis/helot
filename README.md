## helot
A collection of usefull general utilitiy components to facilitate database, flat file and XML access and many more.

For the database related functionality, It does not implement a traditional ORM like solution but a very light wrapper
of a select statement, which when executed it returns python objects containing all the available fields as properties 
that can be accessed using the dot notation.  

This library is favouring simplicity over comprehension while it allows the user to easily build on top of it, in case 
that he wants to specialize its behaviour

## Installation
#### Using pip
```
pip install helot
```

#### Get the full source code
```git clone https://github.com/jpazarzis/helot```

## List of components

### Enumerator
Creates a C++ like enumerator that can be used as such
###### Example
```python
    from helot import Enumerator
    d = Enumerator('CAT', 'DOG', 'HORSE')
    assert d.DOG == 'DOG'
```


#### DataTable
Creates a data table that can be populated from various data sources, including databases or 
delimited files.  Holds all the data in memory and supports quick transformations and both
row and column access interfaces

#### file_stream
A generator of data rows that can be feed by any delimited file. 

#### mysql_stream
A generator of data rows created by a select statement on a mysql database

#### execute_non_query
Executes non query sql statements (for example insert or update)

#### SqliteStream
A generator of data rows created by a select statement on a sqlite database

#### Configuration
Provides an easy to use configuration object that can be globally used and initialized by an ini file