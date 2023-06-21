# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
def is_lucky_ticket(ticket_number):
    if ticket_number < 100000 or ticket_number > 999999:
        raise ValueError("Ticket number should be a six-digit number")

    digits = [int(digit) for digit in str(ticket_number)]
    sum_first_half = sum(digits[:3])
    sum_second_half = sum(digits[3:])
    
    return sum_first_half == sum_second_half

ticket_number = int(input("Введите номер билета (шестизначное число): "))
if is_lucky_ticket(ticket_number):
    print("Билет счастливый!")
else:
    print("Билет несчастливый.")