import pytest 
from cms_controller.api.filters.structure_search import generate_filtered_record_view_query


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected

@pytest.mark.parametrize(
    "table_name, columns, order_by, limit, expected", 
    [
        ("customers", {'Company': 'Touch', 'State': 'NY'}, None, None, "SELECT Company, State FROM customers WHERE TRUE AND Company == 'Touch' AND State == NY"), 
        ("orders", {'Company': 'Goomle', 'Revenue': '1000000', 'State': 'CA'}, 'Revenue', 10 ,"SELECT Company, Revenue, State FROM orders WHERE TRUE AND Company == 'Goomle' AND Revenue == 1000000 AND State == CA  ORDER BY Revenue LIMIT 10"),
    ]
)
def test_generate_filtered_record_view_query(
    table_name, 
    columns,
    order_by,
    limit,
    expected
):
    query = generate_filtered_record_view_query(table_name, columns, order_by, limit)
    assert query.strip() == expected.strip(), (query)


