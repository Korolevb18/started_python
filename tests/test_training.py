from selene import browser, have



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


def sum(a: int, b: int):
    return a + b

print(sum(10, 15))


#def get_user_info(name, age):
#    return name, age

#name, age = 'Иван', 34
#print(name, age)

def get_user_name_age(name, age):
    return name, age

print(get_user_name_age('Петр', 38))


def empty_function():
    print("Привет")

empty_function()

def is_adult(age):
    return age >= 18

age = 19
if is_adult(age)==True:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(
        page_url="https://companyname.com/login",
        button_text="Register"
    )

def format_func_call(func, **kwargs):
    """Форматирует вызов функции с именованными аргументами."""
    name = func.__name__.replace('_', ' ').title()
    values = ', '.join(kwargs.values())
    result = f"{name} [{values}]"
    print(f'"{result}"')
    return result


def open_browser(browser_name):
    actual_result = format_func_call(open_browser, browser_name=browser_name)
    assert actual_result == f"Open Browser [{browser_name}]"
    return actual_result


def go_to_companyname_homepage(page_url):
    actual_result = format_func_call(go_to_companyname_homepage, page_url=page_url)
    assert actual_result == f"Go To Companyname Homepage [{page_url}]"
    return actual_result


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = format_func_call(
        find_registration_button_on_login_page,
        page_url=page_url,
        button_text=button_text
    )
    expected = f"Find Registration Button On Login Page [{page_url}, {button_text}]"
    assert actual_result == expected
    return actual_result
