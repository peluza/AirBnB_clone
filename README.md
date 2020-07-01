# AirBnB_clone

![HBNB](HBNB_image.png)

## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

## Resources:
Read or watch:

* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://intranet.hbtn.io/concepts/66)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## General
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Usage:
To begin clone ArBnB respository

```
$ git clone https://github.com/peluza/AirBnB_clone.git 
```
    
   Go to the AirBnB folder and execute the console
   
Execution:

    $ ./console.py 



Execution
Your shell should work like this in interactive mode:
``` $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  prompt  quit  show  update
 
(hbnb) 
(hbnb) quit
$
```

Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  prompt  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  prompt  quit  show  update
(hbnb) 
$
```

## Requirements
###  Python Scripts

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7 or more)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Files:

This repository contains the following files:

| File                             | Description                                               |
| -------------------------------- | ----------------------------------------------------------|
| console.py                       | Execute the console                                       |
| models/base_model.py             | Defines all common attributes/methods for other classes   |
| models/amenity.py                | classes Amenity that inherits from BaseModel              |
| models/city.py                   | classes City that inherits from BaseModel                 |
| models/place.py                  | classes Place that inherits from BaseModel                |
| models/review.py                 | classes Review that inherits from BaseModel               |
| models/state.py                  | classes State that inherits from BaseModel                |
| models/user.py                   | class User that inherits from BaseModel                   |
| models/engine/file_storage.py    | Serializes instances to a JSON file and deserializes JSON file to instances| 

## TASKS

[0. README, AUTHORS](https://github.com/peluza/AirBnB_clone/blob/master/README.md)

[1. Be PEP8 compliant!](https://github.com/peluza/AirBnB_clone)
* Write beautiful code that passes the PEP8 checks

[2. Unittests](https://github.com/peluza/AirBnB_clone/tree/master/tests)
* All your files, classes, functions must be tested with unit tests

[3.  BaseModel](https://github.com/peluza/AirBnB_clone/blob/master/models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes

[4. Create BaseModel from dictionary](https://github.com/peluza/AirBnB_clone/blob/master/models/base_model.py)
* Now it’s time to re-create with this dictionary representation.
```
    __init__(self, *args, **kwargs) 
```

[5. Store first object](https://github.com/peluza/AirBnB_clone/blob/master/models/base_model.py)
* Now the flow of serialization-deserialization will be:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

[6. Console 0.0.1 ](https://github.com/peluza/AirBnB_clone/blob/master/console.py)
* Write a program called console.py that contains the entry point of the command interpreter:

[7. Console 0.1](https://github.com/peluza/AirBnB_clone/blob/master/console.py)
* Update your command interpreter (console.py) to have these commands:

| Command       | Description                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------|
| create        | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel                       |
| show          | Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.             |
| destroy       | Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234. |
| all           | Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.                  |
| update        |Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com". |


[8. First User](https://github.com/peluza/AirBnB_clone/blob/master/models/user.py)

* Write a class User that inherits from BaseModel

[9. More classes!](https://github.com/peluza/AirBnB_clone/tree/master/models)

* Write all those classes that inherit from BaseModel:

| Class        | File path               |
| -------------| ------------------------|
| State        | models/state.py         |
| City         | models/city.py          |
| Amenity      | models/amenity.py       |
| Place        | models/place.py         |
| Review       | models/review.py        |


[10. Console 1.0](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

[11. All instances by class name](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to retrieve all instances of a class by using: 
```
<class name>.all().
```

[12. Count instances](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to retrieve the number of instances of a class: 
```
<class name>.count().
```

[13. Show](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to retrieve an instance based on its ID: 
```
<class name>.show(<id>).
```

[14. Destroy](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to destroy an instance based on his ID: 
```
<class name>.destroy(<id>).
```

[15. Update](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to update an instance based on his ID: 
```
<class name>.update(<id>, <attribute name>, <attribute value>).
```

[16. Update from dictionary](https://github.com/peluza/AirBnB_clone/blob/master/console.py)

* Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: 
```
<class name>.update(<id>, <dictionary representation>).
```

[17. Unittests for the Console!](https://github.com/peluza/AirBnB_clone/blob/master/tests/test_console.py)

* Write all unittests for console.py, all features!

the test_console contain :

```
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
```

to execute the console use this command

```
python3 -m unittest tests/test_console.py

```

All your tests should be executed by using this command:

```
python3 -m unittest discover tests
```


AUTHORS

* Erika Osorio [erikaosgue](https://github.com/erikaosgue)

* Edison Isaza [peluza](https://github.com/peluza)
