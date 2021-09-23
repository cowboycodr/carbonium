import re

from utils import ModifiedDictionary

class Lexer:
  def __init__(self):
    self.tokens = ModifiedDictionary()

    self.tokens['element'] = [re.compile('<(.*?)>(.*?)</(.*?)>'), re.compile('<(.*?)/>')]

  def tokenize(self, word):
    for key, value in self.tokens:
      pass

if __name__ == '__main__':
  l = Lexer()

  l.tokenize('work')