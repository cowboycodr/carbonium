import traceback

from carbonium.core import reactive

class Reactive:
  def __init__(self, value) -> None:
      # Reactive properties dependent on self
      self._dependents = []

      (filename, line, func, text) = traceback.extract_stack()[-2]
      self.__name = text[:text.find('=')].strip()

      self.__value = value

  def __update(self, value):
    self.__value = value

    for dependent in self._dependents:
      dependent.react(self.name, self)

  def update(self, instance):
    self.__dependents[instance.name] = instance.value

  def _depend(self, instance):
    instance._dependents.append(instance)

  def react(self):
    ''' Updates affected branches '''
    new = self.value

    print(new)

  @property
  def name(self):
    return self.__name

  @property
  def value(self):
    if isinstance(self.__value, function):
      self.value = function()

    return self.__value

  @value.setter
  def value(self, new):
    self.__update(new)