# Python Object-Oriented Programming (OOP)

# Module 10 – Real-World Application Architecture

# Module_10_Code_Examples.md

**Level:** Advanced

**Topics Covered**

- Project Structure
- Packages & Modules
- Configuration Management
- Logging Framework
- Custom Exceptions
- Exception Handling
- Unit Testing
- Multi Module Application

---

# Part 1 – Professional Project Structure

A real Python application is divided into layers.

```
student_management/

│

├── main.py

│

├── config/

│   └── settings.py

│

├── models/

│   └── student.py

│

├── services/

│   └── student_service.py

│

├── exceptions/

│   └── custom_exceptions.py

│

├── utils/

│   └── logger.py

│

├── tests/

│   └── test_student.py

│

├── requirements.txt

└── README.md
```

---

# Understanding Layers

```
main.py

   |

Service Layer

   |

Model Layer

   |

Database / Repository
```

---

# 1. Creating Python Package

Each folder contains:

```
__init__.py
```

Example:

```
models

|

__init__.py

student.py
```

This makes it a Python package.

---

# 2. Model Layer

## File:

```
models/student.py
```

---

```python
from dataclasses import dataclass


@dataclass
class Student:

    id: int

    name: str

    marks: int


    def display(self):

        return (
            f"{self.id} "
            f"{self.name} "
            f"{self.marks}"
        )
```

---

# Usage

```python
student = Student(
    101,
    "Alex",
    95
)


print(student.display())
```

Output

```
101 Alex 95
```

---

# 3. Custom Exceptions

## File:

```
exceptions/custom_exceptions.py
```

---

```python
class StudentException(Exception):

    pass



class InvalidMarksError(StudentException):

    pass



class StudentNotFoundError(StudentException):

    pass
```

---

# Exception Hierarchy

```
Exception

   |

StudentException

   |

----------------

|

InvalidMarksError

StudentNotFoundError
```

---

# 4. Service Layer

## File:

```
services/student_service.py
```

---

```python
from models.student import Student

from exceptions.custom_exceptions import (
    InvalidMarksError
)


class StudentService:


    def create_student(
        self,
        id,
        name,
        marks
    ):


        if marks < 0 or marks > 100:

            raise InvalidMarksError(
                "Marks should be between 0-100"
            )


        return Student(
            id,
            name,
            marks
        )
```

---

# Using Service

```python
service = StudentService()


student = service.create_student(
    101,
    "Alex",
    90
)


print(student)
```

Output

```
Student(id=101,name='Alex',marks=90)
```

---

# 5. Configuration Management

## File:

```
config/settings.py
```

---

```python
class Settings:


    DATABASE = "college.db"


    APP_NAME = "Student Management"


    VERSION = "1.0"
```

---

# Usage

```python
from config.settings import Settings


print(Settings.APP_NAME)

print(Settings.DATABASE)
```

Output

```
Student Management

college.db
```

---

# 6. Logging Framework

## File:

```
utils/logger.py
```

---

```python
import logging


class Logger:


    @staticmethod
    def get_logger():


        logging.basicConfig(

            level=logging.INFO,

            format=
            "%(levelname)s:%(message)s"

        )


        return logging.getLogger(
            "Application"
        )
```

---

# Using Logger

```python
from utils.logger import Logger


logger = Logger.get_logger()


logger.info(
    "Application Started"
)


logger.error(
    "Database Error"
)
```

Output

```
INFO:Application Started

ERROR:Database Error
```

---

# 7. Main Application

## File:

```
main.py
```

---

```python
from services.student_service import (
    StudentService
)

from utils.logger import Logger

from exceptions.custom_exceptions import (
    InvalidMarksError
)


logger = Logger.get_logger()



def main():


    service = StudentService()


    try:


        student = service.create_student(

            101,

            "Alex",

            95

        )


        print(student)


        logger.info(
            "Student Created Successfully"
        )


    except InvalidMarksError as e:


        logger.error(e)



if __name__ == "__main__":

    main()
```

---

# Output

```
Student(
id=101,
name='Alex',
marks=95
)

INFO:Student Created Successfully
```

---

# 8. Configuration Loader Example

Using JSON.

## config.json

```json
{
    "database":"college.db",
    "debug":true,
    "version":"1.0"
}
```

---

## config_loader.py

```python
import json



class ConfigLoader:


    @staticmethod
    def load(filename):

        with open(filename) as file:

            return json.load(file)
```

---

# Usage

```python
from config_loader import ConfigLoader


config = ConfigLoader.load(
    "config.json"
)


print(config["database"])
```

Output

```
college.db
```

---

# 9. Unit Testing Using unittest

## File:

```
tests/test_student.py
```

---

```python
import unittest


from models.student import Student



class TestStudent(unittest.TestCase):


    def test_student_creation(self):


        student = Student(

            101,

            "Alex",

            90

        )


        self.assertEqual(
            student.name,
            "Alex"
        )


        self.assertEqual(
            student.marks,
            90
        )



if __name__=="__main__":

    unittest.main()
```

---

# Running Test

Command:

```
python -m unittest
```

Output:

```
OK
```

---

# 10. pytest Example

Install:

```
pip install pytest
```

---

File:

```
test_student.py
```

---

```python
from models.student import Student



def test_student():

    student = Student(

        1,

        "Alex",

        90

    )


    assert student.marks == 90
```

---

Run:

```
pytest
```

---

# 11. requirements.txt

Stores dependencies.

Example:

```
pytest==8.0

requests==2.31
```

Install:

```
pip install -r requirements.txt
```

---

# 12. Complete Execution Flow

```
main.py

 |

 |

StudentService

 |

 |

Student Model

 |

 |

Exception Handling

 |

 |

Logger
```

---

# Industry Style Improvements

Current:

```
models

services

utils
```

Enterprise:

```
app

├── api

├── core

├── database

├── models

├── services

├── repositories

├── exceptions

└── tests
```

---

# Concepts Used From Previous Modules

| Module | Usage |
|-|-|
| Module 1 | Classes |
| Module 2 | Relationships |
| Module 3 | Encapsulation |
| Module 4 | Inheritance |
| Module 5 | Polymorphism |
| Module 6 | Magic Methods |
| Module 7 | ABC |
| Module 8 | Dataclasses |
| Module 9 | SOLID + Patterns |
| Module 10 | Application Architecture |

---

# Final Learning Outcome

After completing Module 10:

You can build:

✅ Multi-file Python applications

✅ Maintainable project structures

✅ Logging systems

✅ Exception frameworks

✅ Config-driven applications

✅ Unit-tested Python projects

---

# Final OOP Journey Completed

```
Basic OOP

↓

Advanced OOP

↓

SOLID Principles

↓

Design Patterns

↓

Real Application Architecture
```

You are now ready for:

- Python Backend Development
- Django / FastAPI
- Automation Frameworks
- Data Engineering Applications
- Enterprise Python Projects
