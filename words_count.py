# 文字計數
wc = {} # words_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    #print(words)
    #print(wc)
    #break   # 強制讀完第一筆留言就先終止

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
        
# I 2434388
# a 1861333
# to 1480993
 # 1381435
# the 2814086
# and 2034994
# is 1111026
# it 1043972    
    
while True:
    word = input('請問你想什麼值:')
    if word == 'q':
        break
    elif word in wc:
        print(word, '出現過的次數為:', wc[word], '次','\n')
    else:
        print('這個字沒有出現過喔!','\n')
print('感謝使用本查詢功能')   

# 請問你想什麼值:fish
# fish 出現過的次數為: 566 次 

# 請問你想什麼值:ivan
# 這個字沒有出現過喔! 

# 請問你想什麼值:feifei
# 這個字沒有出現過喔! 

# 請問你想什麼值:love
# love 出現過的次數為: 149056 次 

# 請問你想什麼值:q
# 感謝使用本查詢功能    