# Python cheat sheet

## Algemene functies

Lengte opvragen

```
>>> a = 'Hello world!'
>>> len(a)
12
>>> a = [1, 2, 3]
>>> len(a)
3
>>> a = {'one': 1, 'two': 2}
>>> len(a)
2
```

Klasse opvragen

```
>>> a = 'Hello World!'
>>> type(a)
str
>>> a = [1, 2, 3]
>>> type(a)
list
```

Hulp vragen aan de interpreter

```
>>> help(len)
```

## Variabelen

### String

Definieer een string

```
>>> a = 'hi there'
```

Splits een string

```
>>> a.split(' ')
['hi', 'there']
```

Vervang een letter in de string

```
>>> a.replace('e', 'o')
hi thoro
```

Verwijder whitespace voor- en achteraan een string

```
>>> b = ' Hi there.  '
>>> b.strip()
'Hi there.'
```

### Integer

Integers delen door integers

```
>>> 1 / 2
0
```

Lijst van opeenvolgende integers vragen

```
range(5)
[0, 1, 2, 3, 4]
```

### Float

Integer delen door float

```
>>> 1.0 / 2
0.5
```

Check of een float een geheel getal is

```
>>> b = 2.0
>>> b.is_integer()
True
```

### List

Een item van een list opvragen

```
>>> a = ['I', 'like', 'Python']
>>> a[0]
'I'
```

Meerdere items uit een list opvragen (geeft ook een list terug)

```
>>> a[1:3]
['like', 'Python']
```

of 

```
>>> a[1:]
['like', 'Python']
```

of

```
>>> a[-2:]
['like', 'Python']
```

Extra item aan een list toevoegen

```
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
```

Laatste item van een list verwijderen

```
>>> a = [1, 2, 3, 4]
>>> a.pop()
4
>>> a
[1, 2, 3]
```

Een item uit een list verwijderen

```
>>> a = ['one', 'two', 'three']
>>> a.remove('two')
>>> a
['one', 'three']
```

Een item vervangen

```
>>> a = ['I', 'like', 'R']
>>> a[2] = 'Python'
>>> a
['I', 'like', 'Python']
```

Een item toevoegen aan een list op een specifieke plaats

```
>>> a = ['I', 'like', 'Python']
>>> a.insert(1, 'really')
>>> a
['I', 'really', 'like', 'Python']
```

Kijken of een item voorkomt in een lijst

```
>>> a = ['I', 'like', 'Python']
>>> 'Python' in a
True
```

Itereren over een list

```
>>> a = [1, 2, 3]
>>> for item in a:
....    print item
1
2
3
```

### Dict

Item opvragen uit een dict

```
>>> a = {'one': 1, 'two': 2}
>>> a['one']
1
```

Een lijst opvragen met de keys van een dict

```
>>> a.keys()
['one', 'two']
```

Kijken of een key voorkomt in een dict

```
>>> 'three' in a.keys()
False
```

of

```
>>> a.has_key('three')
False
```

Itereren over de items van een dict

```
>>> for key in a.keys()
....    print key
....    print a[key]
'one'
1
'two'
2
```

of

```
>>> for key, value in a.iteritems():
....    print key
....    print value
'one'
1
'two'
2
```

### Functions

Een functie definiëren

```
>>> def sayHi(name):
....    print 'Hello', name
```

Een functie callen

```
>>> sayHi('Bart')
Hello Bart
```

## Werken met files

Een file openen

```
>>> f = open('test.txt')
```

Een file sluiten

```
>>> f.close()
```

Schrijven naar een file

```
>>> f.open('test.txt', 'w+')
>>> f.write('This is line1\n')
>>> f.write('And this is line2\n')
>>> f.close()
```

Lezen van een file

```
>>> f = open('test.txt')
>>> content = f.read()
```

Een lijn lezen van een file

```
>>> f = open('test.txt')
>>> f.next()
'This is line 1\n'
```

Alle lijnen lezen van een file, en als een list teruggeven

```
>>> f = open('test.txt')
>>> f.readlines()
['This is line1\n', 'And this is line2\n']
```

Files zoeken

```
glob
```

Directory van je script opvragen (lukt niet in de interpreter)

```
import os
dir = os.path.dirname(os.paht.realpath(__file__))
print dir
```

## Csv files

### Csv files lezen

```
import csv
f = open('data.csv')
reader = csv.reader(f, delimiter=',')
for row in reader:
    print row
```

### Csv files schrijven