# a1
import a
obj1=a.Animal()
obj1.display()

import b
obj2=b.Bird()
obj2.display()

# a2
from a import Animal
obj3=Animal()
obj3.display()

from b import Bird
obj4=Bird()
obj4.display()
import a
print(dir(a))