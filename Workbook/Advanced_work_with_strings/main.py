import re

text = """This is first line 
And second line
Last third line"""

print(text)


print("Hello\nWorld")
print("Hello\tWorld")
print("Hello my little\rsister")
print("Hello\bWorld")
print("Hello\\World")
print("Hello\n\vWorld")
print("it\'s a beautiful day")
print("He said, \"Hello\"")


# метод find

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end))
print(s.find("q"))

# метод rfind

s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))

# Метод split

text = "hello world"
result = text.split() 
print(result)

text = "apple,banana,cherry"
result = text.split(',')
print(result)

# Метод join

list_of_string = ['hello', 'world']
result = ' '.join(list_of_string)
print(result)

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)

# Метод strip

clean = '   spacious   '.strip()
print(clean)



# Метод replace

text = "Hello world"
new_text = text.replace('world', '')
print(text, new_text)


text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)

# Program

url_link = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_ , query = url_link.split("?")
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)


# Translate

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

stri = "This is string example"
print(stri.translate(trantab))

trantab = str.maketrans('', '', intab)
stri = "This is string example"
print(stri.translate(trantab))

# from 16 to 2

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
       ]
MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 DF 56 AC".translate(MAP)
print(result)


# Text to Morze

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result_ = ""

for ch in string:
    result_ = result_ + ch.upper().translate(table_morze_dict)

print(result_)

# Форматирование 

for i in range(8):
    s = f"int: {i:d}; hex: {i:#x}; oct: {i:#o}; bin: {i:#b}"
    print(s)

price = 19.99
quantity = 3
total = f"Total: {price* quantity:.2f}"
print(total)

# width = 2
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')

name = 'Alice'
formatted = f"{name:>10}"
print(formatted)

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)

#Метод search
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Знайдено: ", match.group())

