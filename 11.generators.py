def numbers():
    for i in range(1, 6):
        yield i

gen = numbers()

for num in gen:
    print(num)
