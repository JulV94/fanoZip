def fano_zip(inFile, bOutFile):
    charCount = count_char(inFile)


def count_char(inFile):
    print("Analysing the file...")
    charCount = dict()
    with open(inFile) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            else:
                if c not in charCount.keys():
                    charCount[c] = list([1, ""])
                else:
                    charCount[c][0] += 1
    f.close()
    return charCount


def find_compression(charRatio):
    print("Finding the best compression encryption...")
    charRatio = recursive_bit_assign(charRatio, charRatio)
    return charRatio

def recursive_bit_assign(charRatio, subGroup):
    if len(subGroup) > 1:
        charSum = 0
        for key in subGroup:
            charSum += subGroup[key][0]
        currentSum = 0
        groups = (dict(), dict())
        for key in subGroup:
            currentSum += subGroup[key][0]
            if 2*currentSum <= charSum:
                charRatio[key][1] += '0'
                groups[0][key] = subGroup[key]
            else:
                charRatio[key][1] += '1'
                groups[1][key] = subGroup[key]
        charRatio = recursive_bit_assign(charRatio, groups[0])
        charRatio = recursive_bit_assign(charRatio, groups[1])
    #else:
        #print(subGroup)
        #charRatio[subGroup][1] += '0'
    return charRatio


charCount = find_compression(count_char('test'))
print(charCount)