
class BaseException(Exception): 
    def __init__(self, msg): 
        self.msg=msg
        super().__init__(msg)


class ProblemNotSpecified(BaseException): 
    def __init__(self, msg): 
        super().__init__(msg)

class ProblemNotFound(BaseException):
    def __init__(self, msg):
        super().__init__(msg)

class InputFileNotFound(BaseException): 
    def __init__(self, msg):
        super().__init__(msg)
