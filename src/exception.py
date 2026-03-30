import sys
from src.logger import logging

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    
    return error_message
class CustomException(Exception):
    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)

        if error_detail is None:
            _, _, exc_tb = sys.exc_info()
        else:
            _, _, exc_tb = error_detail

        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
        else:
            file_name = "Unknown"
            line_number = "Unknown"

        self.error_message = (
            f"Error occurred in script [{file_name}] "
            f"at line [{line_number}] : {str(error_message)}"
        )

    def __str__(self):
        return self.error_message
    


        