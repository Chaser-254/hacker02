# Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
#  The iterator object is initialized using the iter() method.
#  It uses the next() method for iteration.

iterable_value ='Hacker'
iterable_obj = iter(iterable_value)

while True:
    try:

        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break

