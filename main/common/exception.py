from main.common.type.des_enum import DescEnum

class SysException(Exception):

    def __init__(self, code: DescEnum, data=None):
        self.code = code
        self.data = data
