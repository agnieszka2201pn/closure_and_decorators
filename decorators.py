def html_tag(tag='h1'):
    def wrapper(fn):
        def inner(name):
            result = f"<p> {fn(name)} </p>"
            return result.replace(name, f'<{tag}> {name} </{tag}>')
        return inner
    return wrapper



def capitalize(fn): #fn - funkcja którą dekoruję
    def inner(name):
        return fn(name.title())

    return inner

@capitalize
@html_tag('h2')
def hello(name):
    return f"Hello {name}"

@capitalize
@html_tag('span')
def goodbye(name):
    return f"Bye {name}"

print(hello("agnieszka"))
print(goodbye("agnieszka"))

# <p> Hello <h1> Agnieszka </h1> </p>