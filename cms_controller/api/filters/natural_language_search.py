"""
Given a text generated required view of records

1. Extract supported filters from the text
2. Call generate_filtered_record_view_query from structure_search 
"""
from typing import List, Dict
import openai
import json
from structure_search import generate_filtered_record_view_query



def get_filters_from_text(search_text: str, expected_filters: List[str])->str:
    openai.api_key = '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'

    # generate from, eg "extract and return dictionary {List of expected filers} from text if not found set to None"
    prompt = f"Extract for keys in {','.join(expected_filters)} and return a json in text: \"{search_text}\", if key is not present do not include in output"
    # call GPT API with prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0
        )
    # convert response into dictionary 
    response_text = response['choices'][0]['text']
    # call structure_search.generate_filtered_record_view_query
    print(response_text)
    columns = json.loads(response_text.strip())
    query = generate_filtered_record_view_query(table_name='Records', columns=columns)
    # return query
    return query



print(get_filters_from_text(search_text="get records of people with title account manager in companies with revenue 100000 and in state new york", expected_filters=['Company', 'Revenue', 'State', 'Title']))