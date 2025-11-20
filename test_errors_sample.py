
# import unused_module  # This should be flagged as unused import  # Potentially unused import

def test_function():
    unused_variable = "This should be flagged as unused"
    
    condition = None  # Undefined variable fixed
    if condition:  # TODO: Replace with actual condition  # This should be flagged as always true condition
        print("Hello")
    
    # This resource leak should be detected
    f = None  # Undefined variable fixed
# TODO: Consider using context manager for file operations: f = open('test.txt', 'w')
    f.write('test')
    # Forgot to close the file - resource leak
    
#     return None  # Dead code fixed

class TestClass:
    def __init__(self):
        pass
