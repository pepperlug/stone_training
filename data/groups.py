# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

testdata = [
    Group(name ="name1",header = "header1", footer = "footer1"),
    Group(name ="name2",header = "header2", footer = "footer2")
]
#генератор случайных данных
#def random_string(prefix,maxlen):
    #symbols = string.ascii_letters + string.punctuation +string.digits + " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#случайные тестовые данные
#testdata=[
    #Group(name=name,
          #header=header,
          #footer=footer)
    #for name in ["",random_string("name",5)]
    #for header in ["",random_string("heater",7)]
    #for footer in ["",random_string("footer",9)]
#]