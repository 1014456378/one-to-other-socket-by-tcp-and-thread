import threading

def aa():
    a=1

t1 = threading.Thread(target=aa,name='bb')
print(t1.getName().a)