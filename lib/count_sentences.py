#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ''):
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
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self): 
    val1= self.value.replace("?", ".")
    val2 = val1.replace("...", ".")
    val3= val2.replace("!!", ".")

    new_string = val3.split(".")
    new_list = [sentence for sentence in new_string if len(sentence) > 0]
    print(new_list)
    if self.value == "":
      return 0
    else:
      print(len(new_list))
      return(len(new_list))

    
    
  

