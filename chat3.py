# 對話紀錄3
lines = []
with open('3.txt', 'r', encoding ='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
print(lines)
# ['13:32Allen 請問分公司代號是 9432 嗎', '13:34Viki 那是據點代號', '13:34Viki 如果是語音', '13:34Viki 我們的代號是24', '13:34Allen 好']

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(s)
    print('時間:', time)
    print('人名:', name)
    
# ['13:32Allen', '請問分公司代號是', '9432', '嗎']
# 時間: 13:32
# 人名: Allen
# ['13:34Viki', '那是據點代號']
# 時間: 13:34
# 人名: Viki
# ['13:34Viki', '如果是語音']
# 時間: 13:34
# 人名: Viki
# ['13:34Viki', '我們的代號是24']
# 時間: 13:34
# 人名: Viki
# ['13:34Allen', '好']
# 時間: 13:34
# 人名: Allen