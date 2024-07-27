import time

snorker = { }
head = int(time.time())
snorker[head] = (head, head)

while(1):
    last = [*snorker.keys()][-1]
    snork = input("Snork value: ")
    now = int(time.time())
    snorker[now] = (snork, head)
    snorker[last] = (snorker[last][0], now)
    for item in snorker:
        print(str(item) + ": " + str(snorker[item]))
