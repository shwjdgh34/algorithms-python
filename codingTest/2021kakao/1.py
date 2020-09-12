import re


def solution(new_id):

    # level 1
    new_id = new_id.lower()
    # print(new_id)
    # level 2
    patt = re.compile('[^a-z0-9-_.]')
    new_id = patt.sub('', new_id)
    # print(new_id)
    # level 3
    patt2 = re.compile('[.]{2,}')
    new_id = patt2.sub('.', new_id)
    # print(new_id)

    # level 4 - 1
    patt3 = re.compile('^[.]')
    new_id = patt3.sub('', new_id)
    # print(new_id)
    # level 4 - 2
    patt4 = re.compile('[.]$')
    new_id = patt4.sub('', new_id)
    # print(new_id)

    # level 5
    if len(new_id) == 0:
        new_id = 'a'
    # print(new_id)

    # level 6
    new_id = new_id[:15].rstrip('.')
    # print(new_id)

    # level 7
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    return new_id


print(solution('...!@BaT#\*..y.abcdefghijklm')
      )
