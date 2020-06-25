import logging

class InvalidLoginException(Exception):
  pass

class InvalidLoginCredentialsException(InvalidLoginException):
  message = "Invalid Credentials"
  code = 501

  def __init__(self, code = None, message = None):
    self.code = code
    self.message = message

  def __str__(self):
    return self.message

class BannedUserLoginException(InvalidLoginException):
  message = "User Banned"
  code = 502
  
  def __init__(self, code = None, message = None):
    self.code = code
    self.message = message

  def __str__(self):
    return self.message


def checkLogin(user_id:int):
  if user_id == 1:
    raise InvalidLoginCredentialsException
  elif user_id == 2:
    raise BannedUserLoginException

try:
  checkLogin(2)
except InvalidLoginException as e:
  logging.exception(e)
  print(e.message)
  print(e.code)