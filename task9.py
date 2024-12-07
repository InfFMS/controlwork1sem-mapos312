q = 0
for x in range(1, 2097153):
        if 2097152 % x == 0:
            q += 1
print(q)