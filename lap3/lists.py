xs = [3, 2, 1]
print (xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print (xs)
xs.append('bar')
print(xs)
x = xs.pop()
print(x, xs)