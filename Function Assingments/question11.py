# A nested function is a function defined inside another function.
# The inner function is local to the outer function and can only be called from within the outer function.

def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # invoking the inner (nested) function

outer_function()  # invoking the outer function
