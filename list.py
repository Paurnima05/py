# Program for list and its functions
Num = [7, 5, 0, 8, 1, 9, 4, 4, 11, 2, 6, 10, 3]

print("1. Original List:", Num)

Num.append(96)
print("2. After appending:", Num)

Num.sort()
print("3. After Sorting in Ascending Order:", Num)

Num.sort(reverse=True)
print("4. After Sorting in Descending Order:", Num)

Num.remove(8)
print("5. After Removing:", Num)

Num.insert(2, 108)
print("6. After Inserting:", Num)

Index = Num.index(4)
print("7. Index of 4:", Index)

count = Num.count(4)
print("8. Occurrence of number 4:", count)

pop = Num.pop(7)
print("9. Popping element at 7th Index:", pop)

Num.extend([-1, 6, -3, 24])
print("10. After extending:", Num)

Num2 = Num.copy()
print("12. After copying:", Num2)

Num.clear()
print("13. After clearing:", Num)
