# CustomersApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cart_to_customer**](#attach_cart_to_customer) | **POST** /customers/{customer_id}/carts | 
[**check_customer_credentials**](#check_customer_credentials) | **POST** /customers/check-credentials | 
[**create_customer**](#create_customer) | **POST** /customers | 
[**create_facebook_id**](#create_facebook_id) | **POST** /customers/facebook | 
[**delete_customer**](#delete_customer) | **DELETE** /customers/{customer_id} | 
[**generate_authentication_token**](#generate_authentication_token) | **GET** /customers/{customer_id}/authentication-token | 
[**get_customer**](#get_customer) | **GET** /customers/{customer_id} | 
[**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
[**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
[**get_customer_address**](#get_customer_address) | **GET** /customers/{customer_id}/address | 
[**get_customer_can_see_product**](#get_customer_can_see_product) | **GET** /customers/{customer_id}/products/{product_id}/can-see | 
[**get_customer_carts**](#get_customer_carts) | **GET** /customers/{customer_id}/carts | 
[**get_customer_current_views**](#get_customer_current_views) | **GET** /customers/{customer_id}/current-views | 
[**get_customer_groups**](#get_customer_groups) | **GET** /customers/{customer_id}/groups | 
[**get_customer_has_access_to_product**](#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
[**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
[**get_customer_orders**](#get_customer_orders) | **GET** /customers/{customer_id}/orders | 
[**get_customers**](#get_customers) | **GET** /customers | 
[**get_facebook_customer**](#get_facebook_customer) | **GET** /customers/facebook/{facebook_id} | 
[**get_payment_methods**](#get_payment_methods) | **GET** /customers/{customer_id}/payments/{payment_name}/payment-methods | 
[**get_pending_payments**](#get_pending_payments) | **GET** /customers/{customer_id}/payments/{payment_name}/pending | 
[**get_prepayment_balances**](#get_prepayment_balances) | **GET** /customers/{customer_id}/prepayment-balance | 
[**get_prepayment_operations**](#get_prepayment_operations) | **GET** /customers/{customer_id}/prepayment-operation/{type} | 
[**stop_subscription**](#stop_subscription) | **PUT** /customers/{customer_id}/unsubscribe | 
[**update_customer**](#update_customer) | **PUT** /customers/{customer_id} | 
[**update_payment_method**](#update_payment_method) | **PUT** /customers/{customer_id}/payments/{payment_name}/payment-method | 


## **attach_cart_to_customer**
> Cart attach_cart_to_customer(customer_id, cart_id)



Attach cart to customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
cart_id = 789 # int | Cart ID to attach

try: 
    api_response = api_instance.attach_cart_to_customer(customer_id, cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->attach_cart_to_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **cart_id** | **int**| Cart ID to attach | 

### Return type

[**Cart**](#Cart)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **check_customer_credentials**
> Customer check_customer_credentials(email, password)



Check customer credentials

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
email = 'email_example' # str | Email of the customer to check
password = 'password_example' # str | Password of the customer to check

try: 
    api_response = api_instance.check_customer_credentials(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->check_customer_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the customer to check | 
 **password** | **str**| Password of the customer to check | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_customer**
> Customer create_customer(body)



Create new customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
body = kinow_client.CustomerCreateRequest() # CustomerCreateRequest | Created user object

try: 
    api_response = api_instance.create_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerCreateRequest**](#CustomerCreateRequest)| Created user object | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_facebook_id**
> create_facebook_id(customer_id, facebook_id)



Create new Facebook ID for user

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID
facebook_id = 'facebook_id_example' # str | Facebook ID

try: 
    api_instance.create_facebook_id(customer_id, facebook_id)
except ApiException as e:
    print("Exception when calling CustomersApi->create_facebook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID | 
 **facebook_id** | **str**| Facebook ID | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_customer**
> delete_customer(customer_id)



Delete customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to delete

try: 
    api_instance.delete_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to delete | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **generate_authentication_token**
> generate_authentication_token(customer_id)



Create authentication token for customer.        You can use it to auto login customer using an iframe or a redirection to the user        Example url: `https://YOUR_PLATFORM.kinow.tv/?authentication_token=AUTHENTICATION_TOKEN`

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to authenticate

try: 
    api_instance.generate_authentication_token(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->generate_authentication_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to authenticate | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer**
> Customer get_customer(customer_id)



Get Customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_subscriptions**
> SubscriptionAccesses get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page, filters=filters)



Get customer accesses for subscription

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |       ```      type[value]=string&type[operator]=strict&cancel[value]=string&cancel[operator]=contains      _______________        {      \"type\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"cancel\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_accesses_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      type[value]&#x3D;string&amp;type[operator]&#x3D;strict&amp;cancel[value]&#x3D;string&amp;cancel[operator]&#x3D;contains      _______________        {      \&quot;type\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;cancel\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_videos**
> SubscriptionAccesses get_customer_accesses_videos(customer_id, page=page, per_page=per_page)



Get customer access for videos

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_videos(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_accesses_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_address**
> Address get_customer_address(customer_id)



Get customer address

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_customer_address(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**Address**](#Address)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_can_see_product**
> get_customer_can_see_product(customer_id, product_id)



Check if the customer can see this product (restriction by group)

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
product_id = 789 # int | Product ID to fetch

try: 
    api_instance.get_customer_can_see_product(customer_id, product_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_can_see_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **product_id** | **int**| Product ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_carts**
> Carts get_customer_carts(customer_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get customer carts

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |       ```      date_add[value]=string&date_add[operator]=lt      _______________        {      \"date_add\": {      \"value\": \"string\",      \"operator\": \"lt\"      }      } ```      Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_customer_carts(customer_id, page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt      _______________        {      \&quot;date_add\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;lt\&quot;      }      } &#x60;&#x60;&#x60;      Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Carts**](#Carts)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_current_views**
> CustomerCurrentViews get_customer_current_views(customer_id)



Get customer current number of views

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_customer_current_views(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_current_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**CustomerCurrentViews**](#CustomerCurrentViews)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_groups**
> Groups get_customer_groups(customer_id, page=page, per_page=per_page)



Get groups attached to this customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_groups(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Groups**](#Groups)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_has_access_to_product**
> get_customer_has_access_to_product(customer_id, product_id)



Get customer access to video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
product_id = 789 # int | Product ID to fetch

try: 
    api_instance.get_customer_has_access_to_product(customer_id, product_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_has_access_to_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **product_id** | **int**| Product ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_has_access_to_video**
> get_customer_has_access_to_video(customer_id, video_id)



Get customer access to video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
video_id = 789 # int | Video ID to fetch

try: 
    api_instance.get_customer_has_access_to_video(customer_id, video_id)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_has_access_to_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **video_id** | **int**| Video ID to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_orders**
> Orders get_customer_orders(customer_id, page=page, per_page=per_page)



Get customer orders

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_orders(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Orders**](#Orders)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customers**
> Customers get_customers(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)



Get customer list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |       ```      email[value]=string&email[operator]=strict&firstname[value]=string&firstname[operator]=contains      _______________        {      \"email\": {      \"value\": \"string\",      \"operator\": \"strict\"      },      \"firstname\": {      \"value\": \"string\",      \"operator\": \"contains\"      }      } ```Operator can be strict, contains, gt or lt. (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)

try: 
    api_response = api_instance.get_customers(page=page, per_page=per_page, filters=filters, sort_by=sort_by, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|       &#x60;&#x60;&#x60;      email[value]&#x3D;string&amp;email[operator]&#x3D;strict&amp;firstname[value]&#x3D;string&amp;firstname[operator]&#x3D;contains      _______________        {      \&quot;email\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;strict\&quot;      },      \&quot;firstname\&quot;: {      \&quot;value\&quot;: \&quot;string\&quot;,      \&quot;operator\&quot;: \&quot;contains\&quot;      }      } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 

### Return type

[**Customers**](#Customers)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_facebook_customer**
> CustomerId get_facebook_customer(facebook_id)



Get customer ID by Facebook ID

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
facebook_id = 789 # int | Facebook ID to fetch

try: 
    api_response = api_instance.get_facebook_customer(facebook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_facebook_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_id** | **int**| Facebook ID to fetch | 

### Return type

[**CustomerId**](#CustomerId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_payment_methods**
> list[PaymentMethods] get_payment_methods(customer_id, payment_name)



Get payment methods saved for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 

try: 
    api_response = api_instance.get_payment_methods(customer_id, payment_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **payment_name** | **str**|  | 

### Return type

[**list[PaymentMethods]**](#PaymentMethods)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_pending_payments**
> list[PaymentDetails] get_pending_payments(payment_name, customer_id)



Get pending payments for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
payment_name = 'payment_name_example' # str | 
customer_id = 789 # int | 

try: 
    api_response = api_instance.get_pending_payments(payment_name, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_pending_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_name** | **str**|  | 
 **customer_id** | **int**|  | 

### Return type

[**list[PaymentDetails]**](#PaymentDetails)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_balances**
> list[PrepaymentBalance] get_prepayment_balances(customer_id)



Get PrepaymentBalances list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch

try: 
    api_response = api_instance.get_prepayment_balances(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_prepayment_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 

### Return type

[**list[PrepaymentBalance]**](#PrepaymentBalance)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_prepayment_operations**
> PrepaymentOperations get_prepayment_operations(customer_id, type, page=page, per_page=per_page)



Get PrepaymentOperations list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
type = 'type_example' # str | PrepaymentOperation type to fetch (currency or credit)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_prepayment_operations(customer_id, type, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_prepayment_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **type** | **str**| PrepaymentOperation type to fetch (currency or credit) | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**PrepaymentOperations**](#PrepaymentOperations)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **stop_subscription**
> stop_subscription(customer_id, product_access_id)



Unsubcribe an Access recurring payment

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to unsubscribe
product_access_id = 'product_access_id_example' # str | Product access ID to unsubscribe from

try: 
    api_instance.stop_subscription(customer_id, product_access_id)
except ApiException as e:
    print("Exception when calling CustomersApi->stop_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to unsubscribe | 
 **product_access_id** | **str**| Product access ID to unsubscribe from | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_customer**
> Customer update_customer(customer_id, body)



Update customer

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | Customer ID to fetch
body = kinow_client.Customer() # Customer | Body of the customer

try: 
    api_response = api_instance.update_customer(customer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **body** | [**Customer**](#Customer)| Body of the customer | 

### Return type

[**Customer**](#Customer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_payment_method**
> update_payment_method(customer_id, payment_name, payment_arguments)



Update payment method for a Customer on a payment gateway

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.CustomersApi()
customer_id = 789 # int | 
payment_name = 'payment_name_example' # str | 
payment_arguments = kinow_client.PaymentArguments() # PaymentArguments | Payment arguments

try: 
    api_instance.update_payment_method(customer_id, payment_name, payment_arguments)
except ApiException as e:
    print("Exception when calling CustomersApi->update_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **payment_name** | **str**|  | 
 **payment_arguments** | [**PaymentArguments**](#PaymentArguments)| Payment arguments | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

