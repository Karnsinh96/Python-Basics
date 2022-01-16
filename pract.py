import pandas as pd
import numpy as np

a=np.random.randint(1,7)
print(a)

b=np.random.randint(1,100,size=[9])
print(b)
print(type(b))
a=list(b)
print(a)
print(type(a))
a.append("Star")
print(a)