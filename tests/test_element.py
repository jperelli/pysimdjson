import pytest

import csimdjson


def test_is_null(parser):
    assert parser.parse("{}").is_null is False
    assert parser.parse("null").is_null is True


def test_json_pointer(parser):
    """Ensure JSON pointers work as expected and all possible exceptions
    are converted to Python types.
    """
    doc = parser.parse('{"key": "value", "array": [0, 1, 2]}')

    doc.at('key')
    doc.at('array/0')

    with pytest.raises(csimdjson.NoSuchFieldError):
        doc.at('no_such_key')

    with pytest.raises(csimdjson.IndexOutOfBoundsError):
        doc.at('array/9')

    with pytest.raises(csimdjson.IncorrectTypeError):
        doc.at('array/not_a_num')

    with pytest.raises(csimdjson.InvalidJSONPointerError):
        doc.at('array/')
