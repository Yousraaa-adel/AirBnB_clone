#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import models

# base1 = BaseModel()
# base2 = BaseModel()
# base1.name = "Yousra"
# base1.num = 100
# base2.name = "Yassin"
# base2.num = 77
# x = models.storage.new(base1)
# s = models.storage.new(base2)
# models.storage.save()
# y = models.storage.reload()
# # print(x)
# # print("======")
# # print("======")
# # print("======")
# print(y)
# # print(base1)

all_objs = storage.all()
print("-- Reloaded objects --")
print(all_objs)
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print("======")
print("======")
print("======")
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)