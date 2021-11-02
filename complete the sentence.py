import time
import random


def switch(_ans, _under, _ges):
    _under = convert(_under)
    for x in range(len(_under)):
        if convert(_ans)[x] == _ges:
            _under[x] = _ges
    new_under = ''.join(_under)
    return new_under


def convert(string):
    lst = []
    lst[:0] = string
    return lst


def points_counter(points, tester, _under):
    if tester == _under:
        points -= 1
        return points, tester
    else:
        points += 5
        tester = _under.copy()
        return points, tester


def loops(_ans, _under, count=0, points=0):
    test_under = _under.copy()
    while _ans != _under:
        ges_letter = input('enter a letter: ')
        count += 1
        for i in range(3):
            if _ans[i].count(ges_letter) != 0:
                _under[i] = switch(_ans[i], _under[i], ges_letter)
        print(' '.join(_under))
        points, test_under = points_counter(points, test_under, _under)
    return count, points


def main():
    _phrases = [['always', 'be', 'yourself'], ['keep', 'it', 'cool'], ['cash', 'is', 'king'],
                ['change', 'is', 'good'], ['just', 'do', 'it'], ['dreams', 'come', 'true'],
                ['focus', 'and', 'win'], ['go', 'for', 'it'], ['learn', 'from', 'yesterday'],
                ['never', 'look', 'back']]
    _ans = _phrases[random.randint(0, 9)]
    _under = [len(_word) * '_' for _word in _ans]
    print(' '.join(_under))
    start = time.time()
    count, points = loops(_ans, _under)
    end = time.time()
    if end - start < 30:
        points += 100
    print('points = ', points)
    print('attempts = ', count)
    print('time = ', int(end - start), 'sec')


main()
