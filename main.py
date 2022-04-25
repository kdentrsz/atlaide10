sum = int(input("Сумма покупки: "))
end = 0
final = 0
if sum >= 200:
  end = sum/ 100 * 10
  final = sum - end
print(f"{final}€")