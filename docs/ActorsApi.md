# ActorsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_actor**](#create_actor) | **POST** /actors | 
[**delete_actor**](#delete_actor) | **DELETE** /actors/{actor_id} | 
[**get_actor**](#get_actor) | **GET** /actors/{actor_id} | 
[**get_actors**](#get_actors) | **GET** /actors | 
[**get_product_actors**](#get_product_actors) | **GET** /products/{product_id}/actors | 
[**update_actor**](#update_actor) | **PUT** /actors/{actor_id} | 


## **create_actor**
> Actor create_actor(body)



Create new actor

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
body = kinow_client.Actor() # Actor | 

try: 
    api_response = api_instance.create_actor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->create_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Actor**](#Actor)|  | 

### Return type

[**Actor**](#Actor)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_actor**
> delete_actor(actor_id)



Delete actor

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
actor_id = 56 # int | 

try: 
    api_instance.delete_actor(actor_id)
except ApiException as e:
    print("Exception when calling ActorsApi->delete_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **int**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_actor**
> Actor get_actor(actor_id, image_type=image_type)



Get actor

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
actor_id = 789 # int | ID of the actor to fetch
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_actor(actor_id, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **int**| ID of the actor to fetch | 
 **image_type** | **str**|  | [optional] 

### Return type

[**Actor**](#Actor)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_actors**
> Actors get_actors(page=page, per_page=per_page, image_type=image_type)



Get actors list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_actors(page=page, per_page=per_page, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_actors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **image_type** | **str**|  | [optional] 

### Return type

[**Actors**](#Actors)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_actors**
> Actors get_product_actors(product_id, page=page, per_page=per_page, image_type=image_type)



Get actors attached to product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
image_type = 'image_type_example' # str |  (optional)

try: 
    api_response = api_instance.get_product_actors(product_id, page=page, per_page=per_page, image_type=image_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_product_actors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **image_type** | **str**|  | [optional] 

### Return type

[**Actors**](#Actors)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_actor**
> update_actor(actor_id, body)



Update actor

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ActorsApi()
actor_id = 56 # int | 
body = kinow_client.Actor() # Actor | 

try: 
    api_instance.update_actor(actor_id, body)
except ApiException as e:
    print("Exception when calling ActorsApi->update_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **int**|  | 
 **body** | [**Actor**](#Actor)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

