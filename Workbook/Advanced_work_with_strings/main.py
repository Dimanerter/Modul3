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