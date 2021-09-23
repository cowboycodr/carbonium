class ModifiedDictionary(dict):
  '''
  Modified dictionary
  '''

  def __init__(self):
    super()

  def unpack(self):
    for key in self:
      yield (key, self[key])

  def to_dict(self):
    return dict(self)