# 1
# def max_number():
#     numbers_ = list(map(int,input().split(" ")))
#     print(max(numbers_))
# max_number()

# 2
# def sum_number():
#     numbers_ = map(int, input().split(" "))
#     summ = 0
#     for x in numbers_:
#         summ += x
#     print(summ)
# sum_number()

# 3
# def multiple_number():
#     numbers_ = map(int, input().split(" "))
#     summ = 1
#     for x in numbers_:
#         summ *= x
#     print(summ)
# multiple_number()

# 4
# string1 = input("")[::-1]
# print(string1)

# 5
# def factorial():
#     number_ = int(input())
#     factor = 1
#     list1 = [*range(1, number_ + 1)]
#     for x in list1:
#         factor *= x
#     print(factor)
# factorial()

# 6
# def capitalsmall():
#     word = input("Слово: ")
#     big = 0
#     for c in word:
#         if c.isupper():
#             big += True
#     small = 0
#     for c in word:
#         if c.islower():
#             small += True
#     print("Больших букв:", big, ",маленьких букв:", small)
# capitalsmall()

# 7
# def palindrom():
#     word = input().lower()
#     if word == word[::-1]:
#         print("Слово является палиндромом.")
#     else:
#         print("Слово не является палиндромом")
# palindrom()

# 8
# def bank():
#     money = int(input("Деньги: "))
#     time = int(input("Срок: "))
#     summ = money * (10 / 100 + 1) ** time
#     print("Вы получите", summ, "тысяч сум в конце")
# bank()

# 9
# def divide15():
#     nums = [45, 55, 60, 37, 100, 105, 220]
#     for x in nums:
#         if x % 15 == 0:
#             print(x, end=" ")
# divide15()