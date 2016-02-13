import FA02.prod.DataSet as DataSet

ds = DataSet.DataSet()
s = ds.f(0, 5)
print s

constant = ds.LHP(6)
print constant

whatwewant = (.95 - 0.5)/constant
print('What we want:')
print(whatwewant)
print ' '
integration =ds.RHP(1.8946, 7, ds.f)

result = constant * integration + 0.5
print 'the answer is:'
print result
print 'the answer should be'
print .95