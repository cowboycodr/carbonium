import traceback

class Reactive(object):
    def __init__(self, value):
        self.__value = value

        (filename, line, func, text) = traceback.extract_stack()[-2]
        self.__name = text[:text.find('=')].strip()


        self.__listeners = {
            'change': []
        }

        self.__history = [self.value]

    @property
    def name(self):
      return self.__name

    @property
    def history(self):
        return self.__history

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new):
        self.__history.append(self.__value)
        self.__value = new

        self.onchange()

    def add_event_listener(self, event, callback):
        self.__listeners[event].append(callback)

    def onchange(self):
        if len(self.__listeners) > 0:
            for listener in self.__listeners['change']:
                listener(self.value)

    def when(self, target, callback):
        def inner(new):
            if (new == target):
                callback()

        self.add_event_listener('change', inner)

if __name__ == '__main__':
    value = Reactive(0)

    def callback():
        print('The value is 1')

    value.when(1, callback)

    value.value = 1