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
```python
    from helot import execute_query
    for row in execute_query('Select name from person'):
        print(row.name)
    
```

#### Configuration
Provides an easy to use configuration object that can be globally used and 
initialized by an ini file
