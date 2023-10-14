import sys


def error_message_detail(error, error_detail:sys):
   filename=exc_tb.tb_frame.f_code.co_filename
   _,_,exc_tb=error_detail.exc_info()
   error_message="Error seen in python script"+filename+" "+"Line no:"+exc_tb.tb_lineno+" Error: "+str(error)
   return  error_message


class CustomException(Exception):
   def __init__(self,error_message,error_detail:sys):
      super().__init__(error_message)
      self.error_message=error_message_detail(error_message,error_detail=error_detail)

   def __str__(self):
      return self.error_message
      
        