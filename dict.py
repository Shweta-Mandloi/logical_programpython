# A dictionary stores data in key : value pairs.
student = {"name": "Shweta", "age": 20}  #  Returns the value of a key.
print(student.get("name"))    # Shweta
print(student.get("marks", 23))  # 23

#  keys() 
print(student.keys())     # Return all keys        

# values()
print(student.values())   #  Return all values   

# items()  
print(student.items()) # Return key-value pairs         

#  update() 
student.update({"age": 21, "marks": 95}) #Add or update multiple items
print(student)                     

# pop() 
print(student.pop("age")) # Remove key and return its value    
print(student)                     

#  popitem()
print(student.popitem())   #Remove and return last inserted pair

# clear()  
student.clear() 
student.clear()
print(student)                    

#  copy()  
student = {"name": "Shweta"} # Copy dictionary
new_student = student.copy()
print(new_student)                 

#  fromkeys()  
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0) # Create dict from keys with same default value
print(new_dict)                   

