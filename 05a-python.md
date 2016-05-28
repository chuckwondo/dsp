# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Python lists and tuples are similar in that they are both container sequences that can hold items of various types (including other lists and tuples), with the ability to address items by a 0-based positional index. The primary distinction is that lists are mutable whereas tuples are not. This means that lists are not hashable, but tuples are. Therefore tuples work as keys in dictionaries, but lists do not.
>
> In addition, tuples are often used to represent data records, where item position is significant. For example, if tuples were used to represent students, each tuple would contain the same number of items, and the items would be given in the same order for each tuple, where the first item might be the student ID.

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Python lists and sets are similar in that they are collections of mixed data, and both are mutable (although a `frozenset` is an immutable set). However, there are a number of notable differences:
>
> * Each element of a set is unique, whereas a list may contain duplicates.
> * Elements of a set are unordered, whereas elements of a list are ordered.
> * Elements of a list are directly accessible via a 0-based index, whereas set elements are not directly accessible.
> * A set may contain only immutable elements, whereas there is no such restriction on list elements. This means that sets cannot contain contain other (mutable) sets (but may contain `frozenset`s), lists, or dictionaries, for example.
>
> Here is an example of using a list:
>
>     >>> l = [99, "luftballoons", ("a", 1), 99]
>     >>> l
>     [99, 'luftballoons', ('a', 1), 99]
>     >>> l + [{'major-version': 3}]
>     [99, 'luftballoons', ('a', 1), 99, {'major-version': 3}]
>     >>> l[1]
>     'luftballoons'
>
> Here is an example of using a set:
>
>      >>> s = {99, "luftballoons", "a", 1, 99}
>      >>> s
>      {1, 99, 'a', 'luftballoons'}
>      >>> s | {'a', 'b'}
>      {1, 99, 'a', 'b', 'luftballoons'}
>      >>> s - {1}
>      {99, 'a', 'luftballoons'}
>
> In general, finding an element in a set is faster than finding an element in a list because elements in a set are hashed, and can thus be found in constant time. The average time to find an element in a list grows as the size of the list grows (linearly for unsorted lists, logarithmically for sorted lists).

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> The `lambda` keyword creates an anonymous function. However, the body of a lambda function is limited to being a pure expression. For example, the body cannot make assignments nor use statements such as `for`, `while`, etc.
>
> Anonymous functions are best used as arguments to higher-order functions. Due to the restrictions mentioned above, creating complex lambdas is either impossible or unreadable.
>
> Here is an example of using a `lambda` in the `key` argument to `sorted` to sort tuples of first names and last names by last name:

```python
>>> johns = [('John', 'Keating'), ('John', 'Gilling'), ('John', 'Winter')]
>>> sorted(johns, key=lambda name_tuple: name_tuple[1])
[('John', 'Gilling'), ('John', 'Keating'), ('John', 'Winter')]
```

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehensions build new lists by filtering and transforming items from other sequences or any other iterable type.
>
> Here is an example of creating a list of squares of even numbers from 0 through 10:

```python
>>> [x ** 2 for x in range(11) if x % 2 == 0]
[0, 4, 16, 36, 64, 100]
```

> Here's the equivalent using `map` and `filter`:

```python
>>> list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(11))))
[0, 4, 16, 36, 64, 100]
```

> Generally speaking, list comprehensions provide a more compact, readable notation than using `map` and `filter`, especially when used together and with lambda expressions.
>
> Both list comprehensions and uses of `map` and `filter` may quickly become unreadable, at which point resorting to writing explicit loop constructs may be necessary for achieving better readability. Alternatively, with `map` and `filter`, if use of `lambda` expressions is impossible or becomes unreadable, it is possible to refactor them into proper functions, which then may improve readability without having to resort to explicit loop constructs. The same may be applied to list comprehensions.
>
> Here is an example of a set comprehension for obtaining the unique first names of students in a class, where a student is represented by a tuple comprising the student's ID, first name, and last name:

```python
>>> students = {(1, 'John', 'Keating'), (2, 'John', 'Gilling'), (3, 'John', 'Winters'), (4, 'Chuck', 'Daniels')}
>>> {s[1] for s in students}
{'Chuck', 'John'}
```

> Here is an example of a dictionary comprehension using the same set of students, creating a dictionary mapping IDs to students:

```python
>>> {s[0]: s for s in students}
{1: (1, 'John', 'Keating'),
 2: (2, 'John', 'Gilling'),
 3: (3, 'John', 'Winters'),
 4: (4, 'Chuck', 'Daniels')}
```

### Complete the following problems by editing the files below:

### Q5. Datetime

Use Python to compute days between start and stop date.

a.

```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```

> 937

b.
```
date_start = '12312013'
date_stop = '05282015'
```

> 513

c.
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

### Q6. Strings

Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

### Q7. Lists

Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

### Q8. Parsing

Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
