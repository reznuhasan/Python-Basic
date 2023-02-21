marks={"ban":40,"eng":90,"math":34,"rst":60}
marks['ban']=70
marks['math']=80
del marks['eng']
# mark_keys=marks.keys()
# print(mark_keys)
# mark_values=marks.values()
# print(mark_values)
# mark_items=marks.items()
# print(mark_items)
# for k,v in marks.items():
#     print(f"{k} {v}")
for i,key in enumerate(marks):
    print(i,key)