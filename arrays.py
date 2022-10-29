import collections
from collections import Counter
import mapping as mapping
from numpy import iterable

c = collections.Counter([iterable or mapping])

i = 1
while i == 1:
    q = 0
    t = input("Enter a text: ").replace(",", "").lower()
    t = t.split()
    t = [i for i in t if 4 < len(i) < 100]

    action = input("Choose an action [a, b, c]: ").lower()
    if action == "a":
        counter = Counter(t).most_common(5)
        print(counter)
    elif action == "b":
        print(sorted(set(t)))
    elif action == "c":
        while q != 5:
            word = max(t, key=len)
            print(word)
            t.remove(word)
            q += 1
    else:
        print("Wrong selection")

    i = int(input("Type [1] to continue or another key to exit: "))
