###第一题
def naughty_or_nice(data):
    cnt1 = 0
    cnt2 = 0
    for month in data:
        for day in data[month]:
            if data[month][day] == 'Naughty':
                cnt1 += 1
            if data[month][day] == 'Nice':
                cnt2 += 1

    if cnt1 > cnt2:
        return "Naughty!"
    if cnt1 < cnt2:
        return "Nice!"
    else:
        return "Nice!"
###第二题
def get_pins(observed):
    adj = {
        "1": "124",
        "2": "2135",
        "3": "326",
        "4": "4157",
        "5": "52468",
        "6": "6359",
        "7": "748",
        "8": "85790",
        "9": "968",
        "0": "08",
    }
    result = ['']
    for d in observed:
        result = [prefix+c for prefix in result for c in adj[d]]
    return result

###第三题
def protein(rna):
    sq = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if PROTEIN_DICT[codon] == 'Stop':
            break
        sq += PROTEIN_DICT[codon]
    return sq
###第四题
def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False
###第五题
def decodeBits(bits):
    bits = bits.strip('0')
    time_unit = min(map(len, bits.replace('1', ' ').split() + bits.replace('0', ' ').split()))
    word_sep = '0' * 7 * time_unit
    char_sep = '0' * 3 * time_unit
    ones_sep = '0' * 1 * time_unit
    dash = '1' * 3 * time_unit
    dot = '1' * 1 * time_unit
    return bits.replace(dash, '-').replace(dot, '.') \
            .replace(word_sep, '   ').replace(char_sep, ' ').replace(ones_sep, '')

def decodeMorse(morse_code):
    return ' '.join(''.join(map(MORSE_CODE.get, word.split()))
                    for word in morse_code.split('   ')).strip()