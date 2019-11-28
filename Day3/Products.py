l = [{"id": "1", 'name': "oneplus8", 'cost': "10000", 'brand': "oneplus", 'rating': "5", 'discount': '60%', 'category': 'earphone'},
     {"id": "2", 'name': "iphone", 'cost': "70000", 'brand': "apple", 'rating': "3", 'discount': '40%',
      'category': 'phone'},
     {"id": "3", 'name': "note10", 'cost': "9000", 'brand': "samsung", 'rating': "4", 'discount': '70%',
      'category': 'tablet'}]

print("1.Sort by Cost low to high"
      "2.Sort by Cost high to low"
      "3.Sort by Rating"
      "4.Sort by discount low to high"
      "5.Sort by discount high to low")
choice = int(input("Enter the choice"))
if choice == 1:
    mysort = lambda el: el["cost"]
    l.sort(key=mysort)
    print(l)
elif choice == 2:
    mysort = lambda el: el["cost"]
    l.sort(reverse=True, key=mysort)
    print(l)
elif choice == 3:
    mysort = lambda el: el["rating"]
    l.sort(key=mysort)
    print(l)
elif choice == 4:
    mysort = lambda el: el["discount"]
    l.sort(key=mysort)
    print(l)
elif choice == 5:
    mysort = lambda el: el["discount"]
    l.sort(reverse=True, key=mysort)
    print(l)

newobj = filter(lambda el: el["brand"] == "samsung", l)
for i in newobj:
    print("{name}:{brand}".format(**i))
newobj1 = filter(lambda el: el["name"] == "oneplus", l)
for j in newobj1:
    print("{name}:{brand}".format(**j))
newobj2 = filter(lambda el: el["category"] == "phone", l)
for f in newobj2:
    print("{name}:{brand}".format(**f))
