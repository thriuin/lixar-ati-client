# swagger_client.AISearchApi

All URIs are relative to *https://atip-dev-2-searchapi.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get_combined_requestsget**](AISearchApi.md#api_get_combined_requestsget) | **GET** /api/GetCombinedRequests | Summary search
[**api_get_departmentsget**](AISearchApi.md#api_get_departmentsget) | **GET** /api/GetDepartments | Department recommendation
[**api_get_summariesget**](AISearchApi.md#api_get_summariesget) | **GET** /api/GetSummaries | Summary search


# **api_get_combined_requestsget**
> CombinedResult api_get_combined_requestsget(search, organization=organization, year=year, month=month, items_per_page=items_per_page, page=page)

Summary search

Returns a list of existing information request summaries and a list of deparments that would be able to provide infomration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['code'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AISearchApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | Looking for existing summaries or departments that relate to the search string
organization = 'organization_example' # str | Filter results to the specified organization. (optional)
year = 56 # int | Filter results to the specified year. (optional)
month = 56 # int | Filter results to the specified month. (optional)
items_per_page = 10 # int | Determines how many items to include in one page. (optional) (default to 10)
page = 1 # int | Indicates which result page to display. (optional) (default to 1)

try:
    # Summary search
    api_response = api_instance.api_get_combined_requestsget(search, organization=organization, year=year, month=month, items_per_page=items_per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AISearchApi->api_get_combined_requestsget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Looking for existing summaries or departments that relate to the search string | 
 **organization** | **str**| Filter results to the specified organization. | [optional] 
 **year** | **int**| Filter results to the specified year. | [optional] 
 **month** | **int**| Filter results to the specified month. | [optional] 
 **items_per_page** | **int**| Determines how many items to include in one page. | [optional] [default to 10]
 **page** | **int**| Indicates which result page to display. | [optional] [default to 1]

### Return type

[**CombinedResult**](CombinedResult.md)

### Authorization

[apikeyQuery](../README.md#apikeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_departmentsget**
> DepartmentRecommendationResult api_get_departmentsget(search)

Department recommendation

Returns a list of departmentes based on a search string

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['code'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AISearchApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | Looking for departments that would know about this search string

try:
    # Department recommendation
    api_response = api_instance.api_get_departmentsget(search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AISearchApi->api_get_departmentsget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Looking for departments that would know about this search string | 

### Return type

[**DepartmentRecommendationResult**](DepartmentRecommendationResult.md)

### Authorization

[apikeyQuery](../README.md#apikeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_get_summariesget**
> SummarySearchResult api_get_summariesget(search, organization=organization, year=year, month=month, items_per_page=items_per_page, page=page)

Summary search

Returns a list of existing information request summaries.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['code'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['code'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AISearchApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | Looking for existing summariesthat relate to the search string
organization = 'organization_example' # str | Filter results to the specified organization. (optional)
year = 56 # int | Filter results to the specified year. (optional)
month = 56 # int | Filter results to the specified month. (optional)
items_per_page = 10 # int | Determines how many items to include in one page. (optional) (default to 10)
page = 1 # int | Indicates which result page to display. (optional) (default to 1)

try:
    # Summary search
    api_response = api_instance.api_get_summariesget(search, organization=organization, year=year, month=month, items_per_page=items_per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AISearchApi->api_get_summariesget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Looking for existing summariesthat relate to the search string | 
 **organization** | **str**| Filter results to the specified organization. | [optional] 
 **year** | **int**| Filter results to the specified year. | [optional] 
 **month** | **int**| Filter results to the specified month. | [optional] 
 **items_per_page** | **int**| Determines how many items to include in one page. | [optional] [default to 10]
 **page** | **int**| Indicates which result page to display. | [optional] [default to 1]

### Return type

[**SummarySearchResult**](SummarySearchResult.md)

### Authorization

[apikeyQuery](../README.md#apikeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

