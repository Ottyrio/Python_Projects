def net_sal(basic_sal, allowence, deduction):
    print('basic_sal', basic_sal)
    print('allowence', allowence)
    print('deduction', deduction)
    net = basic_sal + allowence - deduction
    return net
n = net_sal(133000, 50000, 60000)
print('Net_Salary: ', n)