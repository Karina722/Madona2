"""
Uzrakstiet programmu Python, lai pārbaudītu, vai norādītā
vērtība ir vērtību grupā.

Testa dati:
3 -> [1, 5, 8, 3]: taisnība
-1 -> [1, 5, 8, 3]: nepatiesa
"""
def testa_dati(dati, n):
    for value in dati:
        if n == value:
            return True
    return False
print(testa_dati([1, 5, 8, 3], 3))
print(testa_dati([5, 8, 3], -1))