from nostril import nonsense
real_test = ['bunchofwords', 'getint', 'xywinlist', 'ioFlXFndrInfo',
             'DMEcalPreshowerDigis', 'httpredaksikatakamiwordpresscom']
junk_test = ['faiwtlwexu', 'asfgtqwafazfyiur', 'zxcvbnmlkjhgfdsaqwerty']
for s in real_test + junk_test:
    print('{}: {}'.format(s, 'nonsense' if nonsense(s) else 'real'))