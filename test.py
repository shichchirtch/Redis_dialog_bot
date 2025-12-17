from datetime import date
import datetime
a = date.today()
print(a)

heute = datetime.datetime.now().strftime('%d.%m.%Y')

print(heute)

di = [{1:'one'}, {2:"two"}, {3:"three"}, {4:"four"}]
arr = []
for k, v in di.items():
    arr.append(i.keys())

print(arr)