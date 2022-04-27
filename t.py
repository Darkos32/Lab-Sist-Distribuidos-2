from matplotlib.pyplot import get


m = {"a":1}
m["b"] = 2
for x in m:
    print(m.get(x))