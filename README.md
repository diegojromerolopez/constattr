# constattr
Ensure your constants class attributes are not re-assigned in python.

## Usage
Decorate your class with `constclassattrs` and when a class attribute that is uppercase
is re-assigned the exception `ConstantAssignmentError` will be raised.

## Example

```python
from constattr.decorators import constclassattrs


@constclassattrs
class Example1:
    MY_CONST1 = '1'
    MY_CONST2 = '2'


# This will raise the ConstAssignmentError exception
Example1.MY_CONST1 = 'new value for the constant'
```

## Limitations
If your class has a metaclass defined, it will work, but in case of conflict
the MRO in the metaclass will choose the [ConstantEnforcerMeta](/constattr/const_enforcer_meta.py)
class first.

## Dependencies
This package has no dependencies.

## License
[MIT](LICENSE) license, but if you need any other contact me.
