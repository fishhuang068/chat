# 第五天：更進階的程式邏輯
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #\ufeff 會出現奇怪空格, utf-8-sig可以解決此問題
        for line in f:
            lines.append(line.strip())
    return(lines)

#def convert(lines):
lines = read_file('input.txt')
for line in lines:
    print(line)
   
new = []
person = None
for line in lines:
    if line == 'Allen':
        person = 'Allen'
        continue
    elif line == 'Tom':
        person = 'Tom'
        continue
        
    if person:    
        new.append(person + ':' + line)
print(new)

Allen
哈囉
你好
Tom
你好
今天一樣是買三份雞肉飯嗎?
Allen
對
飲料一樣紅茶
Tom
半糖去冰對不對
Allen
對，謝謝，我十分鐘後到

['Allen:哈囉', 'Allen:你好', 'Tom:你好', 'Tom:今天一樣是買三份雞肉飯嗎?', 'Allen:對', 'Allen:飲料一樣紅茶', 'Tom:半糖去冰對不對', 'Allen:對，謝謝，我十分鐘後到']

#===================
# 完整建構程式的寫法
#===================
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #\ufeff 會出現奇怪空格, utf-8-sig可以解決此問題
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:    
            new.append(person + ':' + line)
    print(new)
    return new
    
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
    
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
    
main()

#-----------------
# LINE 的對話紀錄
#-----------------
    
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: #\ufeff 會出現奇怪空格, utf-8-sig可以解決此問題
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    person = None
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0    
    allen_image_count = 0
    viki_image_count = 0 
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':   
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else : 
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':   
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else : 
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen 說了', allen_word_count, "個字，傳了", allen_sticker_count, '個貼圖', allen_image_count, '個圖片')
    print('Viki 說了', viki_word_count, "個字，傳了", viki_sticker_count, '個貼圖', viki_image_count, '個圖片')
    return new
    

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

    
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)
    
main()

# Allen 說了 96 個字，傳了 0 個貼圖 2 個圖片
# Viki 說了 163 個字，傳了 1 個貼圖 4 個圖片