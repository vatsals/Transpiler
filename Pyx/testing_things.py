import timeit

cy = timeit.timeit('''example_py.test(5)''',setup='import example_py',number=100)
py = timeit.timeit('''example.test(5)''',setup='import example', number=100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))