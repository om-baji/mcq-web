import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cpp_mcq_db"]
collection = db["questions"]

questions = [
    {
        "number": 1,
        "question": "Which of the following is the correct syntax of including a user-defined header file in C++?",
        "options": [
            "#include 'userdefined'",
            "#include <userdefined.h>",
            "#include <userdefined>",
            "#include 'userdefined.h'"
        ],
        "correct_answer": "#include 'userdefined.h'"
    },
    {
        "number": 2,
        "question": "Which of the following is used for comments in C++?",
        "options": [
            "/* comment */",
            "// comment",
            "Both // and /* */",
            "# comment"
        ],
        "correct_answer": "Both // and /* */"
    },
    {
        "number": 3,
        "question": "Which of the following data types is not supported in C++?",
        "options": [
            "int",
            "float",
            "boolean",
            "double"
        ],
        "correct_answer": "boolean"
    },
    {
        "number": 4,
        "question": "What is the correct output of the following C++ code?\n\n```cpp\nint main() {\n    int x = 5;\n    x++;\n    cout << x;\n    return 0;\n}\n```",
        "options": [
            "5",
            "6",
            "Error",
            "7"
        ],
        "correct_answer": "6"
    },
    {
        "number": 5,
        "question": "Which of the following operators cannot be overloaded in C++?",
        "options": [
            "+",
            "*",
            "::",
            "[]"
        ],
        "correct_answer": "::"
    },
    {
        "number": 6,
        "question": "Which of the following is the default return type of the main function in C++?",
        "options": [
            "int",
            "void",
            "float",
            "char"
        ],
        "correct_answer": "int"
    },
    {
        "number": 7,
        "question": "Which of the following is not a valid access modifier in C++?",
        "options": [
            "public",
            "private",
            "protected",
            "friend"
        ],
        "correct_answer": "friend"
    },
    {
        "number": 8,
        "question": "Which of the following is the correct way to declare an array in C++?",
        "options": [
            "int arr[10];",
            "array<int> arr(10);",
            "int arr = new int[10];",
            "arr<int> = {1,2,3,4};"
        ],
        "correct_answer": "int arr[10];"
    },
    {
        "number": 9,
        "question": "Which of the following concepts is used to implement late binding in C++?",
        "options": [
            "Inheritance",
            "Virtual functions",
            "Operator overloading",
            "Function overloading"
        ],
        "correct_answer": "Virtual functions"
    },
    {
        "number": 10,
        "question": "What is the size of the int data type in C++?",
        "options": [
            "2 bytes",
            "4 bytes",
            "8 bytes",
            "It depends on the compiler"
        ],
        "correct_answer": "It depends on the compiler"
    },
    {
        "number": 11,
        "question": "Which of the following is true about C++?",
        "options": [
            "C++ is a procedural programming language",
            "C++ supports both procedural and object-oriented programming",
            "C++ is a strictly object-oriented programming language",
            "C++ does not support pointers"
        ],
        "correct_answer": "C++ supports both procedural and object-oriented programming"
    },
    {
        "number": 12,
        "question": "Which of the following statements is true for a constructor in C++?",
        "options": [
            "It must have a return type",
            "It cannot be overloaded",
            "It is called automatically when an object is created",
            "It can be virtual"
        ],
        "correct_answer": "It is called automatically when an object is created"
    },
    {
        "number": 13,
        "question": "Which of the following is the correct syntax to declare a pointer in C++?",
        "options": [
            "int* ptr;",
            "int ptr*;",
            "int *ptr;",
            "Both int* ptr; and int *ptr; are correct"
        ],
        "correct_answer": "Both int* ptr; and int *ptr; are correct"
    },
    {
        "number": 14,
        "question": "Which of the following features does not belong to object-oriented programming in C++?",
        "options": [
            "Encapsulation",
            "Polymorphism",
            "Data hiding",
            "Pointers"
        ],
        "correct_answer": "Pointers"
    },
    {
        "number": 15,
        "question": "Which of the following is true for the 'new' keyword in C++?",
        "options": [
            "It is used to deallocate memory",
            "It is used to allocate memory dynamically",
            "It is used to declare new variables",
            "It is used to initialize variables"
        ],
        "correct_answer": "It is used to allocate memory dynamically"
    },
    {
        "number": 16,
        "question": "Which of the following loops in C++ is known as an exit-controlled loop?",
        "options": [
            "for",
            "while",
            "do-while",
            "None of the above"
        ],
        "correct_answer": "do-while"
    },
    {
        "number": 17,
        "question": "Which of the following correctly describes a destructor in C++?",
        "options": [
            "It is used to initialize objects",
            "It is used to deallocate memory",
            "It is called explicitly to destroy an object",
            "It has the same name as the class and has no return type"
        ],
        "correct_answer": "It has the same name as the class and has no return type"
    },
    {
        "number": 18,
        "question": "Which of the following is not a type of inheritance in C++?",
        "options": [
            "Single inheritance",
            "Multiple inheritance",
            "Multilevel inheritance",
            "Friend inheritance"
        ],
        "correct_answer": "Friend inheritance"
    },
    {
        "number": 19,
        "question": "Which of the following operators in C++ is used to access a member function of a class through an object?",
        "options": [
            "->",
            ".",
            "::",
            "*"
        ],
        "correct_answer": "."
    },
    {
        "number": 20,
        "question": "Which of the following is the correct way to declare a constant variable in C++?",
        "options": [
            "const int x = 5;",
            "int const x = 5;",
            "Both const int x = 5; and int const x = 5;",
            "#define x 5"
        ],
        "correct_answer": "Both const int x = 5; and int const x = 5;"
    },
    {
        "number": 21,
        "question": "What is the default value of a static variable in C++?",
        "options": [
            "0",
            "1",
            "NULL",
            "Garbage value"
        ],
        "correct_answer": "0"
    },
    {
        "number": 22,
        "question": "Which of the following is true about function overloading in C++?",
        "options": [
            "Functions with the same name must have the same number of parameters",
            "Functions with the same name can have different return types",
            "Functions with the same name must have different numbers or types of parameters",
            "Functions with the same name can have the same signature"
        ],
        "correct_answer": "Functions with the same name must have different numbers or types of parameters"
    },
    {
        "number": 23,
        "question": "Which of the following is the correct syntax to declare a reference variable in C++?",
        "options": [
            "int &ref;",
            "int ref&;",
            "int *ref;",
            "int ref*;"
        ],
        "correct_answer": "int &ref;"
    },
    {
        "number": 24,
        "question": "Which of the following keywords is used to prevent a class from being inherited in C++?",
        "options": [
            "static",
            "final",
            "sealed",
            "virtual"
        ],
        "correct_answer": "final"
    },
    {
        "number": 25,
        "question": "Which of the following is true for the 'this' pointer in C++?",
        "options": [
            "'this' is a pointer to the current object",
            "'this' is a reference to the current object",
            "'this' is a pointer to the parent object",
            "'this' is a reference to the parent object"
        ],
        "correct_answer": "'this' is a pointer to the current object"
    }
]

result = collection.insert_many(questions)
print(f"Inserted {len(result.inserted_ids)} questions into the database.")
