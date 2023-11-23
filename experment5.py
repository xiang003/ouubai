###第一题
def spin_words(sentence):
    words = sentence.split()
    res = []
    for word in words:
        if len(word) >= 5:
            res.append(word[::-1])
        else:
            res.append(word)
    return ' '.join(res)
###第二题
def find_outlier(integers):
    inte = list()
    for integer in integers:
        if integer % 2 == 0:
            inte.append(0)
        else:
            inte.append(1)
    if inte.count(1) > inte.count(0):
        return integers[inte.index(0)]
    else:
        return integers[inte.index(1)]
###第三题
def is_pangram(s):
    s = s.lower()
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s:
            return False
    return True
###第四题
def validate_sudoku(board):
    valid = lambda r: set(r) == set(range(1,10))
    return (all(map(valid, board))
        and all(valid(r) for r in zip(*board))
        and all(valid(r) for v in zip(*(iter(board),)*3) for r in v)
        and all(valid(r) for r in zip(*((w for k in zip(*(iter(board),)*3) for j in zip(*k) for w in j),)*9)))
