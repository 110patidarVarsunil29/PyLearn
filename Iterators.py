lists = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]

for i in lists:
    print("In for loop ", i)

listsIterator = iter(lists)
while True:
    try:
        i = next(listsIterator)
        print("And how iterator is actually implemented ", i)
    except StopIteration:
        break

print("Before TopTen class!!!!!!!!!!!!")
class TopTen:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
for i in values:
    print(i)
