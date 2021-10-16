def bit_count_list(n, bitstr, bit):
    bit_result = []
    for i in range(n):
        substr = bitstr[i:n]
        bitcount = bitstr.count("1", i, n-1)
        if bitcount == bit and substr not in bit_result:
            bit_result.append(substr)
    return len(bit_result)


if __name__ == '__main__':
    resultlist = []
    testcase = int(input())
    for i in range(testcase):
        n = int(input())
        bitstr = str(input())
        bit = int(input())
        resultlist.append(bit_count_list(n, bitstr, bit))
    for i in resultlist:
        print(i)

# 1	testcases
# 5	String length
# 11010	String
# 2	Combination

# 11 110 101 1010
