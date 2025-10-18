# Python Quest Outline for Joshua

## Chapter 1: Enter the Guild of Pythonistas
1. Setup & First Spells: install CPython from python.org; launch REPL with `python`/`py`; run scripts via `python quest.py`.
2. Variables & Data Types: assign numbers/strings/bools with `=`; inspect type using `type()`; grasp truthy vs falsy values.
3. Strings & Formatting: slice substrings `text[0:3]`; format with f-strings `f"score {points}"`; clean input using `.strip()` and `.lower()`.
4. Control Flow Charms: branch with `if/elif/else`; compare using `==`, `!=`, and membership `in`; chain conditions using `and`/`or`.
5. Loop Lore: iterate using `for` and `range`; loop through lists and tuples; manage repetition with `while` plus `break`.

## Chapter 2: Data Structure Dungeons
1. Lists & Tuples: build collections with `[]` vs `()`; mutate lists via `.append()`/`.pop()`; unpack tuple values into variables.
2. Dictionaries & Sets: create dict literals `{key: value}`; retrieve values with `.get()` defaults; combine sets with union/intersection.
3. Functions & Modules: define functions using `def` and `return`; leverage default and keyword arguments; guard scripts with `if __name__ == "__main__":`.
4. Error Handling: capture specific exceptions `except ValueError`; raise custom errors with `raise`; finish cleanup work inside `finally`.
5. File Handling: open files using `with open(...) as f`; read lines with `.read()`/`.readlines()`; write text using `.write()` and newline control.

## Chapter 3: Object-Oriented Orders
1. Classes & Objects: declare classes with `__init__`; set instance vs class attributes; invoke instance methods via `self`.
2. Inheritance & Polymorphism: derive subclasses from a base; call parent behavior using `super()`; override methods to specialize behavior.
3. Special Methods: implement `__str__`/`__repr__` for display; define comparisons with `__lt__`/`__eq__`; support iteration through `__iter__` and `__next__`.
4. Encapsulation Habits: signal internal attributes with `_name`; create computed attributes via `@property`; model data with `@dataclass`.
5. Packages & Project Layout: organize modules inside packages with `__init__.py`; manage virtual environments using `python -m venv`; install dependencies with `pip install`.

## Chapter 4: Adventurer's Toolkit
1. Functional Side Quests: craft lambda expressions; transform iterables using `map` and `filter`; build list and dict comprehensions.
2. Iterators & Generators: obtain iterators with `iter()` and `next()`; create generators using `yield`; compose generator expressions `(x for x in ...)`.
3. Working with Libraries: calculate with `math` and constants; produce randomness via `random.randint`; chain data using `itertools` utilities.
4. Testing & Debugging: write tests with `unittest.TestCase`; run suites through `python -m unittest`; inspect state using `pdb.set_trace()`.
5. Data Handling: load and dump JSON with `json.load`/`json.dump`; read CSV files via `csv.reader`; call web APIs using `requests.get`.

## Bonus Boss Battles
1. Async Beginnings: declare coroutines with `async def`; execute loops with `asyncio.run`; await concurrent tasks using `asyncio.gather`.
2. Type Checking: annotate code with `typing.List` and `Optional`; validate with `mypy`; use `TypedDict` for structured dicts.
3. Performance Awareness: time snippets using `timeit`; reason about list vs dict complexity; cache results via `functools.lru_cache`.
4. Packaging Adventures: build CLIs with `argparse`; prepare metadata using `setup.cfg` or `pyproject.toml`; publish to TestPyPI with `twine upload`.
