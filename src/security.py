import hashlib

class Security:
    class Hash:
        @staticmethod
        def __abstract(func,text:str):
            return func(text.encode()).hexdigest()

        @staticmethod
        def md5(text:str):
            return Security.Hash.__abstract(hashlib.md5,text)
        
        @staticmethod
        def sha1(text:str):
            return Security.Hash.__abstract(hashlib.sha1,text)
        
        @staticmethod
        def sha256(text:str):
            return Security.Hash.__abstract(hashlib.sha256,text)