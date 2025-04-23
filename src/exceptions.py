import sys
from logger import logging

def error_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occurred in python script name {0} @ line number {1}, error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self, msg, error_detail: sys):
        super().__init__(msg)
        self.error_message = error_message(msg, error_detail)

    def __str__(self):
        return self.error_message
