per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты:"))
TKB = float((per_cent['ТКБ']) * (money/100))
SKB = float((per_cent['СКБ']) * (money/100))
VTB = float((per_cent['ВТБ']) * (money/100))
SBER = float((per_cent['СБЕР']) * (money/100))
deposit = [TKB, SKB, VTB, SBER]
print("Накопленные средства за  вклад в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))