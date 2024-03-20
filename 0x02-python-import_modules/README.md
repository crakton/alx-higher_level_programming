# Python - import & modules

In this project, I learn how to make operations with `import`, `modules`. How to use imported function, create a modules


## Function Prototypes:

Prototypes for functions written in this project:

| File                       | Prototype                                                         |
| -------------------------- | ------------------------------------------------------------------|
| `add_0.py`                 | `def add(a, b)`                                                   |
| `calculator_1.py`          | `def add(a, b)`, `def sub(a, b)`, `def mul(a, b)`, `def div(a, b)`|
| `variable_load_5.py` | **simple variable**|

## Tasks:

0. Import a simple function from a simple file `mandatory`
 * use print with string format
 * assign value `1` to variable `a` and value `2` to variable `b` then use the
   variables as args when calling `add` function
1.  My first toolbox! 
 * Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
2. How to make a script dynamic!**
 * Write a program that prints the number of arguments and the list of its arguments.
3. Infinite addition 
 * The output should be the result of the addition of all arguments, followed by a new line
 * casting arguments into integers by using `int()`
4. Who are you?
 * program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
 * print only names that don't start with `__`
5. Everything can be imported
 * a program that imports the variable a from the file `variable_load_5.py` and prints its **value**.
6. Build my own calculator!
 * a program that imports all functions from the file `calculator_1.py` and handles basic operation
 * if number arguments is not 3 print `Usage: ./100-my_calculator.py <a> <operator> <b>` and exit with value **1**
 * operator can be: `+`, `-`, `*`, `/`
 * If the operator is not one of the above: print `Unknown operator. Available operators: +, -, * and /` exit with value 1
 * variable `a` and `b` is cast to `int`
 * result should be printed like this: `<a> <operator> <b> = <result>`, followed by a new line
