"""Parser benchmarks, styled after the ones used by orjson."""
from json import loads as json_loads

import pytest
from orjson import loads as orjson_loads
from rapidjson import loads as rapidjson_loads
from simplejson import loads as simplejson_loads

import csimdjson


def csimdjson_loads(content):
    return csimdjson.parser().parse(content).up


@pytest.mark.slow
@pytest.mark.parametrize(
    ['group', 'func'],
    [
        ('csimdjson', csimdjson_loads),
        ('orjson', orjson_loads),
        ('rapidjson', rapidjson_loads),
        ('simplejson', simplejson_loads),
        ('json', json_loads)
    ]
)
@pytest.mark.parametrize(
    'path',
    [
        'jsonexamples/canada.json',
        'jsonexamples/twitter.json',
        'jsonexamples/github_events.json',
        'jsonexamples/citm_catalog.json',
        'jsonexamples/mesh.json'
    ]
)
def test_loads_json(group, func, path, benchmark):
    benchmark.group = f'{path} deserialization'
    benchmark.extra_info['group'] = group

    with open(path, 'r') as src:
        content = src.read()
        benchmark(func, content)
