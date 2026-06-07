# Python Password Strength Analyzer

A command-line password utility written in Python that can generate strong passwords and analyze password strength based on common security requirements.

## Features

* Strong password generation
* Password strength analysis
* Checks minimum length requirement
* Detects uppercase letters
* Detects lowercase letters
* Detects numeric characters
* Detects special characters
* Password improvement suggestions
* Menu-driven interface
* Input validation
* Type-safe implementation using `TypedDict`

## Concepts Used

* Functions
* Lists
* Dictionaries
* Sets
* TypedDict
* Type Hinting
* Loops
* Conditional Statements
* User Input Handling
* Input Validation
* Randomization with `choices()` and `randint()`
* Secure Random Selection with `secrets.choice()`

## Run

```bash
python3 main.py
```

## Strength Rating System

| Score | Strength |
| ----- | -------- |
| 0-1   | Weak     |
| 2-4   | Medium   |
|   5   | Strong   |
