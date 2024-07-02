from prefect import flow, task
from prefect.blocks.system import String


@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    print(msg)
    return msg


@task(name="Print Hello Again")
def print_hello_again(name):
    msg = f"Hello {name}!"
    print(msg)

    string_block = String.load("what")
    print(string_block.value)

    return msg


@flow(name="Hello Flow")
def hello_world(name="world!!!!!!"):
    message = print_hello(name)
    message2 = print_hello_again(message)
    return message2
