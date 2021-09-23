import traceback

from reactive import Reactive

class Ref(Reactive):
  def __init__(self, value) -> None:
      super().__init__()

      (filename, line, func, text) = traceback.extract_stack()[-2]
      self.__name = text[:text.find('=')].strip()

      self.__value = value

  @property
  def name(self):
    return self.__name

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, new):
    self.__update(new)

def to_ref(value):
  return Ref(value)