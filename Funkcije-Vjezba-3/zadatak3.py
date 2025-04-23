def je_prost(broj):
    prost = True
    for x in range(2, broj // 2):
        if broj % x == 0:
            prost = False
    return prost

print(je_prost(7))
print(je_prost(8))