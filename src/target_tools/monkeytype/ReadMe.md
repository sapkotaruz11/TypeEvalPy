# setup support for monkeytype

## general workflow

Monkeytype can provide the type annotations for the function call arguments as well as Class variables.
To run the type annotations using monkeytype, we need to initialize a script where we can then import the function or class we want to type annotate and then call the function or instantiate the class in the script. 

Suppose we have a file called *main.py* with following code:
```python
def add (a, b):
    c = a +b 
    print (c)
    return
```

Lets take MyScript.py as a base script to run the analysis.

*MyScript.py*
``` python
from main import add

add(2,5)

```
After calling the intended class/function from the base script, we can run then run the base script using

```shell
monkeytype run myscript.py
```

After executing the base script with monkeytype, we can either add the annotation to the same python file or create a stub file that contains the  type annotation for the "add" function. We can also annotate the files in sub-directory. For that, we can call the file using the path from the base script.

To add annotation directly to the source code , we can run 
```shell
monkeytype apply main
```
or if the main is inside some directory, we can perfrom the type annotations using :
```shell
monkeytype apply some/main
```

To create a stub file with annnotation we can run

```shell
monkeytype stub main > main.pyi
```

The generated annotations look as follows in the stub file or with similar representation on the source file if we select that option:
```python
def add(a: int, b: int) -> None: ...
```

The source file with type annotation should be parsed by a AST parser.