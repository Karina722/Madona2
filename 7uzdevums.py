"""
Uzrakstiet programmu Python, lai aprēķinātu 
četru ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu,
divkāršojot un paņemot tās absolūto vērtību.
"""
sk1=int(input("ievadi 1.skaitli:"))
sk2=int(input("ievadi 2.skaitli:"))
sk3=int(input("ievadi 3.skaitli:"))
sk4=int(input("ievadi 4.skaitli:"))

suma=sk1+sk2+sk3+sk4
if sk1==sk2==sk3==sk4:
      print(abs((sk1*sk2*sk3*sk4)*2))

else:
    print(suma)

