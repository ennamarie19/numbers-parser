import pytest
import pytest_check as check


from datetime import datetime
from numbers_parser import Document
from numbers_parser.cell import EmptyCell


def test_duration_formatting():
    doc = Document("tests/data/duration_112.numbers")
    for sheet in doc.sheets:
        table = sheet.tables[0]
        for row in table.iter_rows(min_row=1):
            if type(row[13]) != EmptyCell:
                duration = row[6].formatted_value
                ref = row[13].value
                check.equal(duration, ref)


def test_date_formatting():
    doc = Document("tests/data/date_formats.numbers")
    for sheet in doc.sheets:
        table = sheet.tables[0]
        for row in table.iter_rows(min_row=1):
            if type(row[6]) == EmptyCell:
                assert type(row[7]) == EmptyCell
            else:
                date = row[6].formatted_value
                ref = row[7].value
                check.equal(date, ref)


@pytest.mark.experimental
def test_custom_formatting():
    doc = Document("tests/data/test-custom-formats.numbers")
    for sheet in doc.sheets:
        table = sheet.tables[0]
        for row in table.iter_rows(min_row=1):
            value = row[1].formatted_value
            ref = row[2].value
            check.equal(value, ref)
