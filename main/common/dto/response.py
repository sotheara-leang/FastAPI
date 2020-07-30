from main.common.type.des_enum import DescEnum
from main.common.type.sys_code import SysCode


class ResponseDto(object):

    def __init__(self, code: DescEnum, data=None):
        self.status = code.value
        self.message = code.desc
        self.data = data

    @classmethod
    def success(cls, data=None):
        return ResponseDto(SysCode.SUCCESS, data)

    @classmethod
    def fail(cls, code=None, data=None):
        if code is not None:
            return ResponseDto(code, data)
        else:
            return ResponseDto(SysCode.SYS_ERROR, data)

    @classmethod
    def not_found(cls):
        return ResponseDto(SysCode.NOT_FOUND)

    @classmethod
    def existed(cls):
        return ResponseDto(SysCode.EXISTED)

    @classmethod
    def invalid(cls, data=None):
        return ResponseDto(SysCode.INVALID, data)
