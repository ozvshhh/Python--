import copy
S = list(input())
print(S)
tag_number = S.count('<')
tags_box = []
tag_place_recorder = []
for i in range(tag_number):
    
    tag_start = S.index('<')
    tag_place_recorder.append(S.index('<'))
    print('tag_start',tag_start)
    tag_end = S.index('>')
    print('tag_end',tag_end)
    tag_once_save =[]
    
    for i in range(tag_start,tag_end+1,1):
        tag_once_save.append(S.pop(tag_start))
        s_tag_once_save = ''.join(tag_once_save)
    tags_box.append(s_tag_once_save)

print(tags_box)

#띄어쓰기 기준으로 단어 분리하기
S = ''.join(S)
print(S)
word_box = []
word_box = list(map(str,S.split()))

#단어 뒤집기
for i in range(len(word_box)):
   reverser = list(word_box[i])
   reverser.reverse()
   word_box[i] = ''.join(reverser)


'''
for i in range(len(tags_box)):
    hey = ''
    for j in range(len(tags_box[i])):
        hey = hey + tags_box[i][j]
    print(hey,end='')
'''
print(tags_box)
print(tag_place_recorder)
print(word_box)

for i in range(len(word_box)+len(tags_box)):
    tag_count = 0
    word_count = 0
    if tag_place_recorder[tag_count] == i:
        print(tags_box[tag_count],end='',sep='')
        tag_count += 1
    else:
        print(word_box[word_count],end='')
        word_count += 1