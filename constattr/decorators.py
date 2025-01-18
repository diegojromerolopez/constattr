from constattr.const_enformcer_meta import ConstantEnforcerMeta


def constclassattrs(cls: type):
    return ConstantEnforcerMeta(cls.__name__, cls.__bases__, dict(cls.__dict__))
