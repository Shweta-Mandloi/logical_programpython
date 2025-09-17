#List comprehesion method in predefine ---------------------
fruit = ['apple','mango'] # The add value is list this method of append.
fruit.append('banna')
print(fruit)

num = [3,4,2,5]
num.clear()
print(num)

shweta = ['arpit', 'vikas', 'ram']
shweta.copy()
print(shweta)

num = [2,4,2,5,3,4,2]
num2 = num.count(2)
print(num2)

car = ['maruti','audi','fourtuner']  
more_car = ['toyota','BMW']    # Add the item is this list extend method.
(car.extend(more_car))
print(car)

num = [4,6,8,3]
print(num.index(4))

beaty = ['lipbam','ring','facewash']
add_itme = 'cream'
beaty.insert(2,add_itme)
print(beaty)

home = ['cloath','press','watch']
home.pop(1)
print(home)

h = ['cloath','press','watch'] # this is remove method is value given usre and remove 
h.remove('press')
print(h)

beaty = ['lipbam','ring','facewash']  # that is reverse given value 
beaty.reverse()
print(beaty)

num = [3,2,5,1,6]   # this method is assending and desending odere
num.sort()
print(num)
