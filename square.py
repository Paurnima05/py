def perfect_square(x) :
  if x >= 0:
    sr = int(x ** 0.5)
    return(sr * sr == x)

number = int(input("Enter a number: "))
if perfect_square(number):
      print(number, "is a perfect square")
else :
      print(number, "is not a perfect square")