# dictionary = a collection of {key: value} pairs.
# Ordered and changeable. No duplicates allowed.

#capitals = {"USA": "Washington D.C.",
#            "India": "New Delhi",
#            "China": "Beijing",
#            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital does not exist")
    

# capitals.update({"Germany" : "Berlin"})
# capitals.update({"USA" : "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# keys = capitals.keys()
# for key in capitals.keys():
#    print(key)
# values = capitals.values()
# for value in capitals.values():
#   print(value)
   
# items = capitals.items()    
#for country, cap in capitals.items():
#    print(f"{country}: {cap}")
  
#print(items)

#           KEY       VALUE
#           ||         ||    KEY        VALUE
#           \/         \/     \/         \/       KEY      VALUE
# product = {'itemid' : 1234, 'name' : 't-shirt', 'color' : 'white'}

# print(product['name'])

# product['size'] = 'small'
# print(product)
# del product['size']

# print(product)
# Adding KEY to dictionary.  A LIST VALUE
#                                \/
# product['size'] = ['small', 'medium', 'large']


# print(product)


products = [
  
    {
    'itemid' : '1001', 
    'name' : 't-shirt', 
    'color' : 'white', 
    'size' : ['small', 'medium', 'large']
    },
    
    {
     'itemid' : '1002', 
     'name' : 'sweatshirt', 
     'color' : 'black', 
     'size' : ['medium', 'large', 'x-large']
    },
    
    {
     'itemid' : '1003', 
     'name' : 'hoodie', 
     'color' : 'green', 
     'size' : ['small', 'medium', 'large']
    }

    ]

print(products[0]['itemid'], products[0]['name'], products[0]['size'][0])
