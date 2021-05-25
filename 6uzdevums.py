"""
Uzrakstiet programmu Python, lai parādītu rītdienas datumu.
"""
import datetime 
sodiena = datetime.date.today()
rit=sodiena+datetime.timedelta(days=1) 
print('Rītdienas datums: ', rit)

