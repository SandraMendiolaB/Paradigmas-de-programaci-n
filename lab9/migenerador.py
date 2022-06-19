def migenerador():
	print("Primero")
	yield 10
	print("Segundo")
	yield 20
	print("Tercero")
	yield 30

gen = migenerador()
val1 = next(gen)
print(vall)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)