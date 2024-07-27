import time

snorker = { }
head = int(time.time())
snorker[head] = (head, head)

while(1):
    last = [*snorker.keys()][-1]
    snork = input("Snork value: ")
    now = int(time.time())
    print(snork)
    snorker[now] = (snork, last)
    val0=snorker[last][0]
    snorker[last] = (val0, now)
    print(snorker)
