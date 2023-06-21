# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number % 100) // 10
units = number % 10
result = hundreds + tens + units
print("Сумма цифр:", result)