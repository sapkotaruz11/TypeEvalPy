# setup support for pyannotate

## general workflow
To evaluate the types using pyannotate, We need a script to intiate the annotator. In this script we can either add the source code directly or call the function that we want to perfrom the type annotation on. This tool can provide type annotations for call arguments and return types.

After initializing the script, Then we can start annotation collection, and finally dump the annotations to the desired file and directory.



``` python
from pyannotate_runtime import collect_types
 if __name__ == '__main__':
    collect_types.init_types_collection()
    with collect_types.collect():
        *some_code*
    collect_types.dump_stats('*target_filename*.json')
```

 To analyse the code, we can either directly add the code to be analyzed directly the analysis script.

``` python
from pyannotate_runtime import collect_types
 if __name__ == '__main__':
    collect_types.init_types_collection()
    with collect_types.collect():
        def add( a, b):
            c = a+b
            print(c)
        add(a,b)
    collect_types.dump_stats('*target_filename*.json')
```

We can also import the module and call the desired function to be annotated.

``` python
from pyannotate_runtime import collect_types
from main import add
 if __name__ == '__main__':
    collect_types.init_types_collection()
    with collect_types.collect():
        add(a,b)
    collect_types.dump_stats('*target_filename*.json')
```


The analysis result is provided in json format. The example Json of anlysis can be :

```json 
[
    {
        "path": "myscript.py",
        "line": 6,
        "func_name": "add",
        "type_comments": [
            "(int, int) -> None"
        ],
        "samples": 1
    }
]

```
The analysis gives the file path, line number the annotated function name with the type annotation of input arguments and the return type of the function.


The analysis can also be done using the open and close brackets using the commands such as collect_types.start() and 
collect_types.stop() and placing the code in between instead of using the context manager  "with collect_types.collect():"

```python
from pyannotate_runtime import collect_types
if __name__ == '__main__':
    collect_types.init_types_collection()
    collect_types.start()
    def add(a,b):
        c = a + b
        print(c)
        return c
    add(2,3)
    collect_types.stop()
    collect_types.dump_stats('type_info.json')
```

To acquire the type annotations for the TypeEvalPy we have two option: 

## match the annotation from json file with source code

In this approach, for each function annotated, we have to look for the json entry of that function and manully match the types of types of the function arguments using the postion of the arguments 

"type_comments": [
            "(int, int) -> None" ]  

and 
func ( a , b):
        ----
        return c

We can map the arguments types in the type comments with the actual arguments from the function code


## annotate the source file directly

We can also annotate the source file directly after we run the intialization script. We can use the script 
```shell
pyannotate -w main.py
```
The -w flag is to provide the writing command. The annotation is provided as comments as:

```python
def add (a, b):
    # type: (int, int) -> None
```

This annotation is unlikely to be sucessfully parsed by the AST to get the types. I tried parsing it using a simple script. We might have to manually acquire the type annotations similar to the previous approach.