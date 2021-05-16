def rec_items(x):
    for key,value in x.items():
        print(key)
    for k1,v1 in value.items():
         print(k1)
    for k2,v2 in v1.items():
        print(k2,v2)

x={"a":{"b":{"c":"d"}}}
rec_items(x)
