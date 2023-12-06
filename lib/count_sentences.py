#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    if self._value.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    if self._value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value.endswith("!"):
      return True
    else:
      return False

  def count_sentences(self):
    replace_punc = self._value.replace('.', ';').replace('!',';').replace('?', ';')
    split_sent = replace_punc.split(';')
    not_empty = [sentence for sentence in split_sent if sentence]
    return len(not_empty)
