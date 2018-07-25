# StatsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_stats_by_customers**](#get_video_stats_by_customers) | **GET** /video-stats/customers | 
[**get_video_stats_by_video**](#get_video_stats_by_video) | **GET** /video-stats/videos | 
[**get_video_stats_sessions**](#get_video_stats_sessions) | **GET** /video-stats/sessions | 


## **get_video_stats_by_customers**
> CustomerVideoStat get_video_stats_by_customers(customer_id=customer_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)



Get video stats by customer

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.StatsApi()
customer_id = 789 # int | ID of the customer to fetch (optional)
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_stats_by_customers(customer_id=customer_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_video_stats_by_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | [optional] 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CustomerVideoStat**](#CustomerVideoStat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_stats_by_video**
> VideoStat get_video_stats_by_video(customer_id=customer_id, date_from=date_from, date_to=date_to, page=page)



Get video stats by video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.StatsApi()
customer_id = 789 # int | ID of the customer to fetch (optional)
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_stats_by_video(customer_id=customer_id, date_from=date_from, date_to=date_to, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_video_stats_by_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | [optional] 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**VideoStat**](#VideoStat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_stats_sessions**
> SessionVideoStat get_video_stats_sessions(customer_id=customer_id, video_id=video_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)



Get video stats sessions

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.StatsApi()
customer_id = 789 # int | ID of the customer to fetch (optional)
video_id = 789 # int | ID of the video to fetch (optional)
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_stats_sessions(customer_id=customer_id, video_id=video_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_video_stats_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | [optional] 
 **video_id** | **int**| ID of the video to fetch | [optional] 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SessionVideoStat**](#SessionVideoStat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

