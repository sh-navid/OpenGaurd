import re
import random

CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class Variable: # Default is kotlin
    @staticmethod
    def find_variables(content):
        return re.findall(r'(va[r|l][ ]+)(.*?)([ ]*=)([ ]*)(.*?)([ |\n|;|//|/*]+)', content)
    

    @staticmethod
    def generate_random_name(length):
        return "_"+("".join([random.choice(CHARS) for _ in range(0,length)]))
    

class KotlinVariable(Variable):
    pass

class PythonVariable:
    @staticmethod
    def find_variables(content):
        return re.findall(r'([ ]+)(.*?)([ ]*=)([ ]*)(.*?)([ |\n|;|#]+)', content)