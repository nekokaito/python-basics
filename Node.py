head = []

for i in range(len(head)):
            if len(head) % 2 != 0:
                v = (len(head) // 2) + 1
                print(head[v - 1::])
            else:
                v = len(head) // 2
                print(head[v::])