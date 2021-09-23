from reactive import Reactive

class Computed(Reactive):
    def __init__(self, value: function, deps: list):
        super()

        self.__deps = []
        self.__value = value

    @property
    def deps(self):
        deps = {
            '__self__': self.__value
        }

        for dep in self.__deps: 
            deps[dep.name] = dep.value

    @property
    def value(self):
        new = self.__value(self.deps)

        if new != self.history:
            self.__history.append(new)
            return new
        else: 
            return self.__history[-1]

        return new

    @value.setter
    def value(self):
        pass