import re
import random

CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# \S means any char except white-space

class Variable: # Default is kotlin
    @staticmethod
    def find_variables(content):
        return re.findall(r'(va[r|l][ ]+)(.*?)([ ]*=)([ ]*)(.*?)([ |\n|;|//|/*]+)', content)
    

    @staticmethod
    def generate_random_name(length):
        return "_"+("".join([random.choice(CHARS) for _ in range(0,length)]))
    

class KotlinVariable(Variable):
    pass

class PythonVariable(Variable):
    @staticmethod
    def find_variables(content):
        return re.findall(r'([ ]+)(.*?)([ ]*=)([ ]*)(.*?)([ |\n|;|#]+)', content)
    

class JsVariable(Variable):
    @staticmethod
    def find_variables(content):
        x= re.findall(r'(const[ ]+|var[ ]+|let[ ]+)(.*?)([ ]*=)([ ]*)(.*?)([ |\n|;|//|/*|=>]+)', content)
        print("----")
        print(x)
        return x