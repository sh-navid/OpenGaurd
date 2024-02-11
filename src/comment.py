import re

class Comment:
    @staticmethod
    def remove_linear(content):
        """
            \\ This is a linear comment \n
        """
        return re.sub(r'//.*?\n', '', content)
