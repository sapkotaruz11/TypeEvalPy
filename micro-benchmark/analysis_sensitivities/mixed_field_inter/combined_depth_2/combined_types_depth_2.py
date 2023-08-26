# A class CombinedTypes is defined that has a field-sensitive member variable 'x'.
# The constructor takes a boolean parameter and assigns different values to 'x' based on the boolean value.
# The get_value method returns 'x', which can have a combined return type of [int, str].
# The field sensitivity allows 'x' to store different types of values in different contexts.
# The code involves calling a separate function 'my_function' to perform the decision.
# The code also includes a nested class 'Nested' to demonstrate multiple depth in field sensitivity.


def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World"
    return x


class CombinedTypes:
    def __init__(self, my_bool):
        self.nested = self.Nested(my_bool)

    class Nested:
        def __init__(self, y):
            self.value = y

    def get_value(self):
        return my_function(self.nested.value)


obj = CombinedTypes(True)
result1 = obj.get_value()

obj.nested.value = False
result2 = obj.get_value()