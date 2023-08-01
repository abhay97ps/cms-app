from typing import Dict
"""
Generate mysql queries for available filters 

Supported Keys:
1. Company: str
2. Revenue: int
3. City: str
4. State: str
5. Title: str
"""

def generate_filtered_record_view_query(
        table_name: str, 
        columns: Dict[str, any]=None, 
        order_by: str=None, 
        limit: int=None)-> str:
    # Start building the base query
    query = f"SELECT {', '.join(columns) if columns else '*'} FROM {table_name} "

    # Add WHERE clause if condition is provided
    condition = f"WHERE TRUE "
    if columns is not None:
        for key in columns:
            if columns[key] is '' or columns[key] is None:
                continue
            elif key == 'Company':
                condition += f"AND Company == \'{columns['Company']}\' "
            elif key == 'Revenue':
                condition += f"AND Revenue == {columns['Revenue']} "
            elif key == 'State':
                # check and convert to two letter as required
                condition += f"AND State == {columns['State']} "
    
    query += condition

    # Add ORDER BY clause if order_by is provided
    if order_by:
        query += f" ORDER BY {order_by}"

    # Add LIMIT clause if limit is provided
    if limit:
        query += f" LIMIT {limit}"

    return query


