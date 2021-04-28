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