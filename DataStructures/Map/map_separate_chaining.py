from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random 

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def rehash(my_map):  ##!!REVISAR EL REHASH POR LA NATURALEZA DEL SEPARATE CHAINING!!##
    """
    Realiza un rehash de la tabla de simbolos.
    Para realizar un rehash se debe seguir los siguientes pasos:
    Crear una nueva tabla map_separate_chaining con capacity que sea el siguiente primo al doble del capacity actual.
    Recorrer la tabla actual y reinsertar cada elemento en la nueva tabla.
    Asignar la nueva tabla como la tabla actual.
    Retornar la tabla nueva.
    """
    cap_anterior = my_map["capacity"]
    cap_nueva = mf.next_prime(2*cap_anterior)

    nuevo = new_map(cap_nueva, my_map["limit_factor"], my_map["prime"])
    nuevo["capacity"] = cap_nueva
    for i in range(my_map["capacity"]):
        entry = lt.get_element(my_map["table"], i)
        if me.get_key(entry) is not None:
            llave = me.get_key(entry)
            valor = me.get_value(entry)
            h = mf.hash_value(nuevo, llave)
            ocupied, pos = find_slot(nuevo, llave, h)
            if ocupied: #Si existe la llave, se cambia el valor
                me.set_value(lt.get_element(nuevo["table"], pos), valor)
            else: #No existe y se debe agregar la llave-valor y añadir 1 en current factor
                me.set_key(lt.get_element(nuevo["table"], pos), llave)
                me.set_value(lt.get_element(nuevo["table"], pos), valor)
                nuevo["size"] += 1
                nuevo["current_factor"] = nuevo["size"]/nuevo["capacity"]
    return nuevo

def new_map(num_elements, load_factor, prime=109345121):
    y=mf.next_prime(num_elements//load_factor)
    x = lt.new_list()
    for i in range(y):
        lt.add_last(x, me.new_map_entry(None,None))
    map = {"prime": prime,
           "capacity": y,
           "scale": random.randrange(1, prime-1),
           "shift":random.randrange(0, prime-1),
           "table": x,
           "current_factor": 0,
           "limit_factor": load_factor,
           "size": 0
    }
    return map

#def put(mapa, key, value):

#def contains(mapa, key):

#def get(mapa, key):

#def remove(mapa, key):

def size(mapa):
    return mapa["size"]

#def is_empty(mapa):

#def key_set(mapa):

#def value_set(mapa):