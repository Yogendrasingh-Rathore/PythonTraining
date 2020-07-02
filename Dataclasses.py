from dataclasses import dataclass

# Simple DataClass
@dataclass
class Person:
    name: str
    age: int

p = Person('yuvi', 24)
print(p)

# Default Values DataClass
@dataclass
class Person2:
    name: str = 'unknown'
    age: int = 0

p = Person2('yuvi', 24)
print(p)

p2 = Person2()
print(p2)

p.occupation = 'soft engg'
print(p.occupation) 

# Frozen DataClass

@dataclass(frozen=True) #Program will fail here at p.occupation as frozen is set True
class Person3:
    name: str
    age: int

p = Person3('yuvi', 99)
print(p)
p.occupation = 'soft engg'
print(p.occupation)
