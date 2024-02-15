import re

class Cleaner: # Default is kotlin
    @staticmethod
    def remove_emptylines(content):
        return re.sub(r'[ |\t]*\n+', '\n', content,flags=re.DOTALL)
    

class KotlinCleaner(Cleaner):
    pass


class PythonCleaner(Cleaner):
    pass
