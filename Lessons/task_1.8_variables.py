# Катя узнала, что ей для сна надо 𝑋 минут.
# В отличие от Коли, Катя ложится спать после полуночи в 𝐻 часов и 𝑀 минут.
# Помогите Кате определить, на какое время ей поставить будильник,
# чтобы он прозвенел ровно через 𝑋 минут после того, как она ляжет спать.

# На стандартный ввод, каждое в своей строке, подаются значения 𝑋, 𝐻 и 𝑀.
# Гарантируется, что Катя должна проснуться в тот же день, что и заснуть.
# Программа должна выводить время, на которое нужно поставить будильник:
# в первой строке часы, во второй — минуты.

X = int(input())
H = int(input())
M = int(input())
a = X//60 + H
b = X%60 + M
c = a + b//60
d = b%60
print(c)
print(d)