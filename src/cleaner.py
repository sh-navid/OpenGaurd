import re

class Cleaner:
    @staticmethod
    def remove_emptylines(content):
        return re.sub(r'[ |\t]*\n+', '\n', content,flags=re.DOTALL)
