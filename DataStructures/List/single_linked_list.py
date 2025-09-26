def new_list():
    newlist={
        "first": None,
        "last": None,
        "size": 0,
    }
    
    return newlist
def get_element(my_list, pos):
    posicion = 0
    node = my_list["first"]
    while posicion < pos:
        node = node["next"]
        posicion += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    existe = False
    temp = my_list["first"]
    count = 0
    while not existe and temp != None:
        if cmp_function(element, temp["info"]) == 0:
            existe = True
        else:
            temp = temp["next"]
            count += 1

    if not existe:
        count = -1
    return count

    """
    new_node es una función auxiliar para funciones donde se tenga que crear un nodo
    """
def new_node():
    nodo={
        "info":None,
        "next":None
    }
    return nodo
    
def add_first(list, element):
    nodo = new_node()
    nodo["info"]=element
    
    if list["size"]==0:
        list["first"]=nodo
        list["last"]=nodo
    else:
        primero = list["first"]
        nodo["next"]=primero
        list["first"]=nodo
    list["size"]+=1
    return list

def add_last(list,element):
    nodo = new_node()
    nodo["info"]=element
    
    if list["size"]==0:
        list["first"]=nodo
        list["last"]=nodo
    else:
        list["last"]["next"]=nodo
        list["last"]=nodo
    list["size"]+=1
    return list

def size (list):
    return list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]

def is_empty(list):
    x = None
    if list["size"]==0:
        x = True
    else:
        x = False
    return x

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def delete_element(my_list,pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
        sig = my_list["first"]["next"]
        my_list["first"]=sig
    else:
        nodo = my_list["first"]
        sig = nodo["next"]
        ant = None
        cont = 0
        while cont < pos:
            ant = nodo
            nodo=nodo["next"]
            sig=nodo["next"]
            cont+=1
        ant["next"]=sig
    my_list["size"]-=1
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif my_list["size"] == 1:
        primero = my_list["first"]["info"]
        my_list["first"]=None
        my_list["last"]=None
    else:
        primero = my_list["first"]["info"]
        my_list["first"]=my_list["first"]["next"]
    my_list["size"]-=1
    return primero

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    elif my_list["size"]==1:
        ultimo = my_list["last"]["info"]
        my_list["first"]=None
        my_list["last"]=None
    else:
        ultimo = my_list["last"]["info"]
        nodo = my_list["first"]
        ant = None
        while nodo["next"] != None:
            ant=nodo
            nodo = nodo["next"]
        my_list["last"]=ant
        ant["next"]=None
    my_list["size"]-=1
    return ultimo

def insert_element(my_list, element, pos):
    nuevo = new_node()
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0:
            nuevo["next"]=my_list["first"]
            my_list["first"]=nuevo
    else:
        nodo = my_list["first"]
        ant = None
        cont = 0
        while cont < pos:
            ant = nodo
            nodo = nodo["next"]
            cont +=1    
        nuevo["next"]=nodo
        ant["next"]=nuevo
        nuevo["info"]=element
        if nodo == None:
            my_list["last"]=nuevo
    my_list["size"]+=1
    return my_list  

def change_info(my_list, pos, new_info):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        nodo = my_list["first"]
        cont = 0
        while cont < pos:
            nodo = nodo["next"]
            cont +=1
        nodo["info"]=new_info
    return my_list

def exchange(my_list,p1, p2):
    if p1 < 0 or p1 > size(my_list) or p2 < 0 or p2 > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif p1!=p2:
        nodo = my_list["first"]
        cont = 1
        ant= None
        sig = None
        
        n1 = my_list["first"]
        ant1 = None
        sig1 = my_list["first"]["next"]
        
        n2 = my_list["first"]
        ant2 = None
        sig2 = my_list["first"]["next"]
       
        while cont < my_list["size"]:
            ant=nodo
            nodo = nodo["next"]
            sig = nodo["next"]
            if cont == p1:
                n1=nodo
                ant1 = ant
                sig1 = sig
            elif cont == p2:
                n2=nodo
                ant2=ant
                sig2=sig    
            cont +=1
        ant1["next"]=n2
        n2["next"]=sig1
        ant2["next"]=n1
        n1["next"]=sig2
        
        if ant1 == None:
            my_list["first"]=n2
        if sig2 == None:
            my_list["last"]=n1
    return my_list

def sub_list(my_list, pos, num_elmts):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos + num_elmts > my_list["size"]:
            num_elmts = my_list["size"]-pos
        s_list = new_list()
        nodo = my_list["first"]
        cont = 0
        
        while cont<pos:
            nodo = nodo["next"]
            cont+=1
        
        while s_list["size"] < num_elmts:
            s_list = add_last(s_list, nodo["info"])
            nodo=nodo["next"]
    return s_list

def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted
sort_criteria = default_sort_criteria

def insertion_sort(my_list, default_sort_criteria):
    sort_list = new_list()
    nodo = my_list["first"]
    
    while nodo != None:
        if sort_list["size"]==0:
            sort_list = add_last(sort_list, nodo["info"])
        else:
            actual = sort_list["first"]
            position = 0
            while position < sort_list["size"] and default_sort_criteria(actual["info"], nodo["info"]):
                actual = actual["next"]
                position +=1
            sort_list = insert_element(sort_list, nodo["info"], position)
        nodo=nodo["next"]
    return sort_list


def shell_sort(my_list, sort_crit):
    h = (3 * my_list["size"] + 1) // 3  
    while h > 0:
        i = h
        while i < my_list["size"]:
            temp = get_element(my_list, i+1)
            j = i
            while j >= h and sort_crit(temp, get_element(my_list, j-h+1)):
                change_info(my_list, j+1, get_element(my_list, j-h+1))
                j -= h
            change_info(my_list, j+1, temp)
            i += 1
        h=h//3
    return my_list

def merge_sort(my_list, sort_crit):
    tam = size(my_list)
    if tam == 0: #lista vacía
        return my_list
    elif tam == 1: #lista 1 elemento, caso recursivo
        return my_list
    else:
        m = tam//2
        izq = new_list()
        for k in range(0, m):
            add_last(izq, get_element(my_list, k))
        izq_f = merge_sort(izq, sort_crit)
        
        der = new_list()
        for l in range (m+1, tam-1):
            add_last(der, get_element(my_list, l))
        der_f = merge_sort(der, sort_crit)
        return merge(izq_f, der_f, sort_crit)
    
def merge(lst1, lst2, sort_crit):
    l=0
    r=0
    new = new_list()
    while l < size(lst1) and r < size(lst2):
        elem_l = get_element(lst1, l)
        elem_r = get_element(lst2, r)
        x = sort_crit(elem_l, elem_r)
        if x == True: # l < r
            add_last(new, elem_l)
            l += 1
        else:
            add_last(new, elem_r)
            r += 1
    return new
            