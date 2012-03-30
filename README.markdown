Released Python 2 methods that act like unbound methods from Python 3. You can
actually call them without an instance.

Normal Python 2 behavior:

```python
    >>> class MyClass(object):
    ...     def my_method(self):
    ...         return self
    >>> MyClass.my_method(1)
    Traceback (most recent call last):
        ...
    TypeError: unbound method my_method() must be called with MyClass instance
               as first argument (got int instance instead)

```

Released behavior:

```python
    >>> from released import object
    >>> class MyClass(object):
    ...     def my_method(self):
    ...         return self

    >>> # An instance method like before.
    >>> my_instance = MyClass()
    >>> my_instance.my_method
    <bound method MyClass.my_method of <MyClass object at ...>>
    >>> my_instance.my_method()
    <MyClass object at ...>

    >>> # As a released class method.
    >>> MyClass.my_method
    <function my_method at ...>
    >>> MyClass.my_method(1)
    1

```
