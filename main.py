# Кортеж (tuple, immutable) не изменямый список

channels = ["red", "green", "blue"]

r, g, b = channels # распаковка

print(r)
print(g)

r, *g = channels
print(r)
print(g)

channels = [128, 200, 155]
r, g, b = channels
print(r, g, b)
