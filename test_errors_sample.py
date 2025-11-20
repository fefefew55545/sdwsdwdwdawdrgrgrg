
import unused_module  # This should be flagged as unused import

def test_function():
    unused_variable = "This should be flagged as unused"
    
    if True:  # This should be flagged as always true condition
        print("Hello")
    
    # This resource leak should be detected
    f = open('test.txt', 'w')
    f.write('test')
    # Forgot to close the file - resource leak
    
    return None

class TestClass:
    def __init__(self):
        pass
