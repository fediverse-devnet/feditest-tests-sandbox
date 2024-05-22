from feditest import test


@test
def value_error() -> None:
    """
    This test always raises a ValueError.
    """
    raise ValueError('This test raises a ValueError.')


@test
def attribute_error() -> None:
    """
    This test always raises an AttributeError.
    """
    a = None
    return a.b


@test
def type_error() -> None:
    """
    This test always raises a TypeError.
    """
    a = None
    return a + 2


@test
def assertion_error() -> None:
    """
    This test fails a standard Python assertion.
    """
    assert False

