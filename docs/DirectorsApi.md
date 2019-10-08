# DirectorsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_director**](#create_director) | **POST** /directors | 
[**delete_director**](#delete_director) | **DELETE** /directors/{director_id} | 
[**get_director**](#get_director) | **GET** /directors/{director_id} | 
[**get_director_products**](#get_director_products) | **GET** /directors/{director_id}/products | 
[**get_directors**](#get_directors) | **GET** /directors | 
[**get_product_directors**](#get_product_directors) | **GET** /products/{product_id}/directors | 
[**update_director**](#update_director) | **PUT** /directors/{director_id} | 


## **create_director**
> Director create_director(body)



Create new director

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
body = kinow_client.Director() # Director | 

try: 
    api_response = api_instance.create_director(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->create_director: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Director**](#Director)|  | 

### Return type

[**Director**](#Director)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_director**
> delete_director(director_id)



Delete director

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
director_id = 56 # int | 

try: 
    api_instance.delete_director(director_id)
except ApiException as e:
    print("Exception when calling DirectorsApi->delete_director: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_director**
> Director get_director(director_id, image_type=image_type)



Get director

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
director_id = 789 # int | Director ID to fetch
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_director(director_id, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_director: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**| Director ID to fetch | 
 **image_type** | **str**|  | [optional] 

### Return type

[**Director**](#Director)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_director_products**
> Products get_director_products(director_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, features=features, filters=filters)



Get director products

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
director_id = 789 # int | Director ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)
ip = 'ip_example' # str | filter by customer ip (optional)
features = 'features_example' # str |       ```      features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict      _______________        {      \"*\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"1\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```      Operator can be strict, contains, gt or lt.      To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |       ```      name[value]=string&name][operator]=contains&date_add[value]=string&date_add[operator]=lt      _______________        {      \"name\": {      \"value\": \"string\",      \"operator\": \"contains\"      },      \"date_add\": {      \"value\": \"string\",      \"operator\": \"lt\"      }      } ```      Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_director_products(director_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, features=features, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_director_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**| Director ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 
 **ip** | **str**| filter by customer ip | [optional] 
 **features** | **str**|       &#x60;&#x60;&#x60;      features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict      _______________        {      \&quot;*\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;1\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;      Operator can be strict, contains, gt or lt.      To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      name[value]&#x3D;string&amp;name][operator]&#x3D;contains&amp;date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt      _______________        {      \&quot;name\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      },      \&quot;date_add\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;lt\&quot;      }      } &#x60;&#x60;&#x60;      Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**Products**](#Products)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_directors**
> Director1 get_directors(page=page, per_page=per_page, image_type=image_type)



Get directors list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_directors(page=page, per_page=per_page, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_directors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **image_type** | **str**|  | [optional] 

### Return type

[**Director1**](#Director1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_directors**
> Director1 get_product_directors(product_id, page=page, per_page=per_page, image_type=image_type)



Get directors of a product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
product_id = 789 # int | Product ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_product_directors(product_id, page=page, per_page=per_page, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_product_directors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **image_type** | **str**|  | [optional] 

### Return type

[**Director1**](#Director1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_director**
> update_director(director_id, body)



Update director

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.DirectorsApi()
director_id = 56 # int | 
body = kinow_client.Director() # Director | 

try: 
    api_instance.update_director(director_id, body)
except ApiException as e:
    print("Exception when calling DirectorsApi->update_director: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**|  | 
 **body** | [**Director**](#Director)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

