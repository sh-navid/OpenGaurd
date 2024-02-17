import re

class Comment: # Default is kotlin
    @staticmethod
    def remove_linear(content):
        """
            // This is a linear comment \n
        """
        return re.sub(r'//.*?\n', '\n', content)
    
    @staticmethod
    def remove_multiline(content):
        """
            /* 
                This is a multiline
                comment
            */
        """
        return re.sub(r'/\*.*?\*/', '\n', content,flags=re.DOTALL)
    

class KotlinComment(Comment):
    pass


class PythonComment(Comment):
    @staticmethod
    def remove_linear(content):
        """
            # This is a linear comment \n
        """
        return re.sub(r'#.*?\n', '\n', content)
    
    @staticmethod
    def remove_multiline(content):
        """
            ''' 
                This is a multiline
                comment
            '''
        """
        content = re.sub(r'""".*?"""', '', content,flags=re.DOTALL)
        return    re.sub(r"'''.*?'''", '', content,flags=re.DOTALL)
    
    
class JsComment(Comment):
    pass