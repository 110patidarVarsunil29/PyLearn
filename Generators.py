
def counter():
    i = 1
    while (i <= 10):
        yield i
        i += 1

for i in counter():
    print(i)


def numbers():
    i=1
    while(i<=20):
        if i % 2==0:
            yield 'Even'
        else:
            yield 'Odd'
        i+=1
for i in numbers():
    print(i)

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n += 1

values=topten()
for i in values:
    print(i)