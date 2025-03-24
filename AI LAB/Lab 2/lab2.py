# # class person:
# #     def __init__(self, name, age, cnic):
# #         self.name = name
# #         self.age = age
# #         self.cnic = cnic
# #
# #     def display(self):
# #         print('Name: ', self.name, ', Age: ', self.age, ', CNIC: ', self.cnic)
# #
# #
# # p=person('Ali',20,1231231232)
# # p.display()
# # p1=person('Ali',22,2361231232)
# # p1.display()
#
# car = ("Ford F-Series", "Toyota", "Tesla", "Honda")
# print(car)
# print(car[1],"  ",car[-1],"\nRange of indexes: ",car[0:-1],"\nCount:",car.count("Toyota"))

# colors ={"red","green","purple","brown","brown"}
# print(colors,"\nThe length of colors is:",len(colors))
# for color in colors:
#     print(color,end="")
# colors.add("yellow")
# print("\nupdated set: ",colors)
# colors.discard("green")
# print("updated set: ",colors)

synonyms={
    "calm":"peaceful",
    "discover":"locate",
    "kindness":"warm-heartedness",
    "mystery":"puzzle",
    "wisdom":"intelligence"
}
print(synonyms)
print(synonyms["wisdom"])
print("len(synonyms)=",len(synonyms))
synonyms["brave"]="courageous"
print(synonyms)
print("all keys",synonyms.keys())
print("all values",synonyms.values())
for synonym in synonyms:
    print(synonym)
    print(synonym[0]," ",synonym[1])