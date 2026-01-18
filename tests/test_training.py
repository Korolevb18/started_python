def test_hello():
    print("Привет всем!")

test_hello()
test_hello()
test_hello()


def hello_new(name):
    print(f"Привет,{name}!")

hello_new("Иван")

print("Привет,"  "и снова здрастье!")
print('Привет, и снова здрастье!')

c = 5
b = 2
if c > b: print('C больше b!')

number = 123 + 321
h = 123 + 321
print(number, h)

a = "Hello, world!".replace("Hello", "Bye")
print(a)
b = "Hello, world!".split()
print(b)
c = "Hello, world!".upper()
print(c)
