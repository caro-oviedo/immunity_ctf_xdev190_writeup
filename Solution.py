scrambled_key = [0xB1,0xA1,0xA1,0x79,0xD1,0x41,0x50,0x58,0x5D,0x54,0xC5,0x41,0x04,0x9D,0x50,0x25,0x25,0x58,0x45,0x50,0x45,0x54,0x59,0xD5,0x44,0x99,0x54,0x21,0x55,0x5D,0x44,0x5D,0x21,0x58,0x8D,0x50,0x25,0x58,0x45,0x50,0x45,0x54,0x59,0x61]
real_key = []

for number in scrambled_key:
    bin_number = format(number, '08b')
    
    z5 = int(bin_number[0])
    z4 = int(bin_number[1])
    z3 = int(bin_number[2])
    z2 = int(bin_number[3])
    z1 = int(bin_number[4])
    z0 = int(bin_number[5])
    fix_0 = int(bin_number[6])
    assert fix_0 == 0
    z6 = int(bin_number[7])

    solve_value = []
    solve_value.append(0)
    solve_value.append(z6)
    solve_value.append(z5 ^ 1)
    solve_value.append(z4)
    solve_value.append(z3)
    solve_value.append(z2 ^ 1)
    solve_value.append(z1)
    solve_value.append(z0 ^ 1)

    d = ''.join(map(str, solve_value))
    real_key.append(chr(int(d,2)))
    #print hex(int(d,2))

print ''.join(real_key)
print len(real_key)


