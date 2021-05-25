"""
Uzrakstiet programmu Python, 
kas atgriezīs ar true vērtību, 
ja divas norādītās veselu skaitļu vērtības
 ir vienādas vai to summa vai starpība ir 5.
"""
def parbaudit(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(parbaudit(9, 4))
print(parbaudit(4, 2))
print(parbaudit(9, 2))