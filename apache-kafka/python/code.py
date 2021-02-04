import asyncio
from faker import Faker
import json
from dataclasses import dataclass, field
import random
from pathlib import Path

def faker_demo():
    print('faker demo')
    fake = Faker()
    for _ in range(3):
        email = fake.email()
        name = fake.name()
        print(f"email: {email}")
        print(f"name: {name}")

# asyncio is a library to write concurrent code using the async/await syntax.
# Python 3.7+
# https://docs.python.org/3/library/asyncio.html
async def concurrent():
    print('hello')
    await asyncio.sleep(1)
    print('world')

# https://docs.python.org/3/library/json.html
def json_demo():
    jay = {
        "id": 100,
        "programming_lang": "python",
        "topic": "data streaming",
    }

    # encode
    # print json with pretty printing
    print(json.dumps(jay, indent=2))

    # decode
    jay = json.loads('["code", {"prog_langs":["java", "go", "python", "dart"]}]')
    print(jay)

def programming_languages():
    return ["go", "dart", "python", "java"]

# Data Classes
# since Python 3.7 (backport for Python 3.6)
# https://pypi.org/project/dataclasses/
@dataclass
class Developer:
    id: int = field(default=0)
    programming_lang: str = field(default_factory=lambda:random.choice(["go", "python", "dart"]))
    # from typing import List
    # programming_lang: List[int] = field(default_factory=lambda: ["go", "python", "dart"] )

    def whoami(self) -> str:
        return f"id: {self.id}; programming language: {self.programming_lang}"

def random_pw_objects():
    fake = Faker()
    d = { fake.password(length=16): object() for _ in range(random.randint(1, 5)) }
    print(d)
    # output ex.: {'#u_K8F7nC(1s7Vev': <object object at 0x7f1632d64a10>, '$@3#wC@rY3HiLVfA': <object object at 0x7f1632d64a40>}
    # output ex.: {'8(pCC3gx^#6!X$9A': <object object at 0x7f60ed2dda10>}

def current_path():
    path_of_this_file = Path(__file__).parents[0]
    print(path_of_this_file)

def under_construction():
    foobar = True
    if foobar:
        print('foobar')

def main():
    asyncio.run(concurrent())
    faker_demo()
    json_demo()

    dev = Developer(100)
    print(dev.whoami())

    random_pw_objects()
    current_path()

    under_construction()

if __name__ == "__main__":
    main()
