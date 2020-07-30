from main.type.biz_code import ResultCode

class SysException(Exception):

    def __init__(self, code: ResultCode, data=None):
        self.code = code
        self.data = data
