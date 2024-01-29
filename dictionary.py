#creating dictionary.adding .updating,deleting,created nested dictionary

dic_names=dict([(1,"A"),(2,"B"),(3,"C"),(4,"D"),(5,"E")])
print(dic_names)
dic_names[6]="F"
print(dic_names)
dic_names[6]="S"
print(dic_names)
del dic_names[6]
print(dic_names)

print("nested dic:",dic_names[5])
