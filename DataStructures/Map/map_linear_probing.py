from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def new_map()
    map = {"prime": 109345121,
           "capacity"        
    }
    
def contains (my_map, key):
   encontrado = False
   for i in range(1, my_map["capacity"] + 1):
      current = lt.get_element(my_map["table"], i)
      if me.get_key(current) == key:
         encontrado = True
         return encontrado
   return encontrado

 def get(my_map, key):
   for i in range(1, my_map["capacity"] + 1):
      current = lt.get_element(my_map["table"], i)
      if me.get_key(current) == key:
         return me.get_value(current)
   return None  