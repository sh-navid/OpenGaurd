class File:
    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            content = file.read()
        return content
    
    @staticmethod
    def write(path,content):
        with open(path, 'w') as file:
            file.write(content)
        return content