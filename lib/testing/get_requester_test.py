import json
from GetRequester import GetRequester

class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [{ 'name': 'Daniel', 'occupation' : 'LG Fridge Salesman' }, { 'name': 'Joe', 'occupation': 'WiFi Fixer' }, { 'name': 'Avi', 'occupation': 'DJ' }, { 'name': 'Howard', 'occupation': 'Mountain Legend' }]

def test_get_response():
    '''get_response_body function returns response.'''
    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    JSON_STRING = '[{"name":"Daniel","occupation":"LG Fridge Salesman"},{"name":"Joe","occupation":"WiFi Fixer"},{"name":"Avi","occupation":"DJ"},{"name":"Howard","occupation":"Mountain Legend"}]'
    
    requester = GetRequester(URL)
    response_body_str = requester.get_response_body()
    
    # Parse both JSON strings and compare the resulting Python data structures
    response_data = json.loads(response_body_str)
    expected_data = json.loads(JSON_STRING)
    
    assert response_data == expected_data

def test_load_json():
        '''load_json function returns response.'''
        requester = GetRequester(URL)
        assert(requester.load_json() == CONVERTED_DATA)
