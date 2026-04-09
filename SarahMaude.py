# n = 3
# for i in range(1, n+1):
#     for j in range(0, n):
#         pass

# i = 0
# n = 19
# while i <= n:
#     i += 1
#     print(i)

tp_1 = [10, 11, 12, 13, 14]
tp_2 = [10, 11, 12, 13, 14]
i = 0
total = 0
while i < len(tp_1):
    note_1 = tp_1[i]
    total += note_1
    note_2 = tp_2[i]
    note_addition = note_1 + note_2
    print(note_addition)
    i += 1

print("-----")
print(total)
