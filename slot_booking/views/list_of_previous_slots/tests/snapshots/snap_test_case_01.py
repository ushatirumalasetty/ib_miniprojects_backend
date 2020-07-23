# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01ListOfPreviousSlotsAPITestCase::test_case status'] = 200

snapshots['TestCase01ListOfPreviousSlotsAPITestCase::test_case body'] = [
]

snapshots['TestCase01ListOfPreviousSlotsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '2',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01ListOfPreviousSlotsAPITestCase::test_case list_of_previous_slots'] = GenericRepr('<HttpResponse status_code=200, "text/html; charset=utf-8">')
