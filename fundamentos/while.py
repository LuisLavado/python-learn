# print("1er bucle")
# i = 0
# while i <= 10:
#     i += 1
#     print(i)

# print("2do bucle")
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

print("3er bucle")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("i dejó de ser menor que 10")
