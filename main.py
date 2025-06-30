# Списки (list)
import ast

import a

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

а = ["a", "b", "c"]
b = a[:] # a.copy()
b.append("d")
print(id(a))
print(id(b))
print(a)
print(b)
