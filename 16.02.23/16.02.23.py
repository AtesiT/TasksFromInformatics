#1      Имеется строка, содержащая буквы латинского алфавита и цифры. Вывести на экран длину наибольшей последовательности цифр, идущих подряд.

anyString = 'erwvtery761vwebye75647sdvt135vrrtu4'

i = 0
j = 0
maxNum = 0
arrayWithNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for anySymbol in anyString:
  if anySymbol in arrayWithNumbers:
    i += 1
  else:
    if i > maxNum:
      maxNum = i
    i = 0
  j += 1
print(maxNum)