# Python API Client for Flexify.IO Management Console

With [Flexify.IO](https://flexify.io/), storing your data in a cloud does not imply dependency on a single provider anymore!

By unlocking your application from the specific cloud vendor or protocol, you finally gain the freedom to decide when and where to store your data.

And we took care about data migration too!


+ Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.6
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://flexify.io/](https://flexify.io/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install directly from Github

```sh
pip install git+https://github.com/flexifyio/flexify-manage-api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/flexifyio/flexify-manage-api-client-python.git`)

Then import the package:
```python
import flexify_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flexify_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import flexify_api
from flexify_api.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = flexify_api.AuthenticationControllerApi()
authentication_request = flexify_api.AuthenticationRequest() # AuthenticationRequest | authenticationRequest

try:
    # Generate access token for user
    api_response = api_instance.authentication_request(authentication_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationControllerApi->authentication_request: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationControllerApi* | [**authenticate**](docs/AuthenticationControllerApi.md#authenticate) | **POST** /rest/auth | Generate new access token for the user
*AuthenticationControllerApi* | [**get_config**](docs/AuthenticationControllerApi.md#get_config) | **GET** /rest/auth/config | Logout
*AuthenticationControllerApi* | [**logout**](docs/AuthenticationControllerApi.md#logout) | **POST** /rest/auth/logout | Logout
*BillingAccountControllerApi* | [**get_costs_for_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_costs_for_current_user_billing_account) | **GET** /rest/account/costs | Get costs for current user
*BillingAccountControllerApi* | [**get_current_user_billing_account**](docs/BillingAccountControllerApi.md#get_current_user_billing_account) | **GET** /rest/account | Get billing account for current user
*BillingAccountControllerApi* | [**get_payments_for_current_user**](docs/BillingAccountControllerApi.md#get_payments_for_current_user) | **GET** /rest/account/payments | Get payments for current user
*CloudLocationsControllerApi* | [**get_available_locations_for_current_user**](docs/CloudLocationsControllerApi.md#get_available_locations_for_current_user) | **GET** /rest/cloud-locations | getAvailableLocationsForCurrentUser
*DistributorBillingAccountsControllerApi* | [**activate_account**](docs/DistributorBillingAccountsControllerApi.md#activate_account) | **PUT** /rest/distributor/accounts/{account-id}/actions/activate | activateAccount
*DistributorBillingAccountsControllerApi* | [**add_payment**](docs/DistributorBillingAccountsControllerApi.md#add_payment) | **POST** /rest/distributor/accounts/{account-id}/payments | addPayment
*DistributorBillingAccountsControllerApi* | [**get_costs**](docs/DistributorBillingAccountsControllerApi.md#get_costs) | **GET** /rest/distributor/accounts/{account-id}/costs | getCosts
*DistributorBillingAccountsControllerApi* | [**get_details**](docs/DistributorBillingAccountsControllerApi.md#get_details) | **GET** /rest/distributor/accounts/{account-id} | getDetails
*DistributorBillingAccountsControllerApi* | [**get_payments**](docs/DistributorBillingAccountsControllerApi.md#get_payments) | **GET** /rest/distributor/accounts/{account-id}/payments | getPayments
*DistributorBillingAccountsControllerApi* | [**suspend_account**](docs/DistributorBillingAccountsControllerApi.md#suspend_account) | **PUT** /rest/distributor/accounts/{account-id}/actions/suspend | suspendAccount
*EndpointsControllerApi* | [**attach_storages_to_endpoint**](docs/EndpointsControllerApi.md#attach_storages_to_endpoint) | **POST** /rest/endpoints/{endpoint-id}/storages | Attach the storage to the endpoint
*EndpointsControllerApi* | [**detach_storage_from_endpoint**](docs/EndpointsControllerApi.md#detach_storage_from_endpoint) | **DELETE** /rest/endpoints/{endpoint-id}/storages/{storage-id} | Detach the storage from the endpoint
*EndpointsControllerApi* | [**disable**](docs/EndpointsControllerApi.md#disable) | **PUT** /rest/endpoints/{endpoint-id}/actions/disable | Disable the endpoint
*EndpointsControllerApi* | [**enable**](docs/EndpointsControllerApi.md#enable) | **PUT** /rest/endpoints/{endpoint-id}/actions/enable | Enable the endpoint
*EndpointsControllerApi* | [**get_endpoint_details**](docs/EndpointsControllerApi.md#get_endpoint_details) | **GET** /rest/endpoints/{endpoint-id} | Get endpoint details
*EndpointsControllerApi* | [**get_endpoints_for_current_user**](docs/EndpointsControllerApi.md#get_endpoints_for_current_user) | **GET** /rest/endpoints | Get endpoint for current user. This method will create new endpoint if no endpoints exist for user
*EndpointsControllerApi* | [**set_storage_put_objects**](docs/EndpointsControllerApi.md#set_storage_put_objects) | **PUT** /rest/endpoints/{endpoint-id}/storages/{storage-id}/put-objects | Set given storage as default for the endpoint
*EndpointsControllerApi* | [**update_endpoint**](docs/EndpointsControllerApi.md#update_endpoint) | **PUT** /rest/endpoints/{endpoint-id} | Update attributes of the endpoint
*LogControllerApi* | [**get_log_for_current_user**](docs/LogControllerApi.md#get_log_for_current_user) | **GET** /rest/log | getLogForCurrentUser
*MigrationsControllerApi* | [**add_migration**](docs/MigrationsControllerApi.md#add_migration) | **POST** /rest/migrations | Add new migration
*MigrationsControllerApi* | [**get_migration**](docs/MigrationsControllerApi.md#get_migration) | **GET** /rest/migrations/{migration-id} | Get migration by id. Only migration owner or administrator have access to the migration
*MigrationsControllerApi* | [**get_migrations**](docs/MigrationsControllerApi.md#get_migrations) | **GET** /rest/migrations | Get all migrations for logged in user in pagged mode
*MigrationsControllerApi* | [**hide_migration**](docs/MigrationsControllerApi.md#hide_migration) | **POST** /rest/migrations/{migration-id}/hide | Hide migration from UI
*MigrationsControllerApi* | [**stop_migration**](docs/MigrationsControllerApi.md#stop_migration) | **POST** /rest/migrations/{migration-id}/stop | Stop (cancel) the migration
*PaymentControllerApi* | [**get_payment_options**](docs/PaymentControllerApi.md#get_payment_options) | **GET** /rest/pay/paddle/options | getPaymentOptions
*PaymentControllerApi* | [**payment_fulfilled**](docs/PaymentControllerApi.md#payment_fulfilled) | **GET** /rest/pay/paddle/webhook | paymentFulfilled
*StoragesControllerApi* | [**add_buckets**](docs/StoragesControllerApi.md#add_buckets) | **POST** /rest/storage-accounts/{storage-account-id}/buckets | Add buckets to the storage account
*StoragesControllerApi* | [**add_storage_account**](docs/StoragesControllerApi.md#add_storage_account) | **POST** /rest/storage-accounts | Add Storage Account with an optional list of buckets
*StoragesControllerApi* | [**delete_bucket**](docs/StoragesControllerApi.md#delete_bucket) | **DELETE** /rest/storage-accounts/{storage-account-id}/buckets/{bucket-id} | Deletes (hides) a bucket/container
*StoragesControllerApi* | [**delete_buckets**](docs/StoragesControllerApi.md#delete_buckets) | **POST** /rest/storage-accounts/actions/delete-buckets | Deletes (hides) multiple buckets/containers
*StoragesControllerApi* | [**generate_access_keys**](docs/StoragesControllerApi.md#generate_access_keys) | **GET** /rest/generate-access-keys | Generate new access keys pair
*StoragesControllerApi* | [**get_buckets**](docs/StoragesControllerApi.md#get_buckets) | **GET** /rest/storage-accounts/{storage-account-id}/buckets | Get registered non-hidden bukects/containers of the storage account
*StoragesControllerApi* | [**get_providers**](docs/StoragesControllerApi.md#get_providers) | **GET** /rest/providers | Get all storage providers
*StoragesControllerApi* | [**get_storage_accounts**](docs/StoragesControllerApi.md#get_storage_accounts) | **GET** /rest/storage-accounts | Get all storage accounts for current user
*StoragesControllerApi* | [**refresh_bucket**](docs/StoragesControllerApi.md#refresh_bucket) | **POST** /rest/storage-accounts/{storage-account-id}/buckets/{bucket-id}/actions/refresh | Refresh statistics of a single bucket
*StoragesControllerApi* | [**refresh_buckets**](docs/StoragesControllerApi.md#refresh_buckets) | **POST** /rest/storage-accounts/actions/refresh-buckets | Refresh statistics of multiple buckets
*StoragesControllerApi* | [**request_buckets**](docs/StoragesControllerApi.md#request_buckets) | **GET** /rest/buckets | Lists buckets of the external storage account
*StoragesControllerApi* | [**request_cloud_buckets**](docs/StoragesControllerApi.md#request_cloud_buckets) | **GET** /rest/storage-accounts/{storage-account-id}/cloud/buckets | Retrieve buckets/containers list from underlying cloud
*StoragesControllerApi* | [**set_buckets**](docs/StoragesControllerApi.md#set_buckets) | **PUT** /rest/storage-accounts/{storage-account-id}/buckets | Sets a list of bucket for a storage account (hides existing buckets not in a list and adds buckets not in a list)
*UserControllerApi* | [**get_current_user**](docs/UserControllerApi.md#get_current_user) | **GET** /rest/user/current | Get details of user correponsing to provided auth token
*UserControllerApi* | [**request_reset_password**](docs/UserControllerApi.md#request_reset_password) | **POST** /rest/user/request-reset-password | requestResetPassword


## Documentation For Models

 - [AccessKeysPair](docs/AccessKeysPair.md)
 - [AddMigrationRequest](docs/AddMigrationRequest.md)
 - [AddMigrationRequestMapping](docs/AddMigrationRequestMapping.md)
 - [AddStorageAccountRequest](docs/AddStorageAccountRequest.md)
 - [AttachStoragesToEndpointRequest](docs/AttachStoragesToEndpointRequest.md)
 - [AuthenticationRequest](docs/AuthenticationRequest.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [BillingAccount](docs/BillingAccount.md)
 - [BillingAccountWithMoney](docs/BillingAccountWithMoney.md)
 - [Bucket](docs/Bucket.md)
 - [BucketStat](docs/BucketStat.md)
 - [BucketsRequest](docs/BucketsRequest.md)
 - [ChangePasswordRequest](docs/ChangePasswordRequest.md)
 - [CleanupStat](docs/CleanupStat.md)
 - [CloudLocation](docs/CloudLocation.md)
 - [CostDetails](docs/CostDetails.md)
 - [Distributor](docs/Distributor.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointDetails](docs/EndpointDetails.md)
 - [EndpointStat](docs/EndpointStat.md)
 - [EndpointStorage](docs/EndpointStorage.md)
 - [EndpointStorageSettings](docs/EndpointStorageSettings.md)
 - [IdResponse](docs/IdResponse.md)
 - [IdsList](docs/IdsList.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogEvent](docs/LogEvent.md)
 - [Mapping](docs/Mapping.md)
 - [MappingStat](docs/MappingStat.md)
 - [Migration](docs/Migration.md)
 - [MigrationSettings](docs/MigrationSettings.md)
 - [MigrationStat](docs/MigrationStat.md)
 - [Money](docs/Money.md)
 - [NewEndpointStorage](docs/NewEndpointStorage.md)
 - [NewStorageAccount](docs/NewStorageAccount.md)
 - [Organization](docs/Organization.md)
 - [PageLogEntry](docs/PageLogEntry.md)
 - [PageMigration](docs/PageMigration.md)
 - [Pageable](docs/Pageable.md)
 - [Payment](docs/Payment.md)
 - [PaymentAddRequest](docs/PaymentAddRequest.md)
 - [PaymentOptions](docs/PaymentOptions.md)
 - [PriceListEntry](docs/PriceListEntry.md)
 - [PublicAuthenticationConfiguration](docs/PublicAuthenticationConfiguration.md)
 - [RequestResetPasswordReqeust](docs/RequestResetPasswordReqeust.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [SignUpRequest](docs/SignUpRequest.md)
 - [SignupResult](docs/SignupResult.md)
 - [Slot](docs/Slot.md)
 - [SlotStat](docs/SlotStat.md)
 - [Sort](docs/Sort.md)
 - [StorageAccount](docs/StorageAccount.md)
 - [StorageAccountSettings](docs/StorageAccountSettings.md)
 - [StorageProvider](docs/StorageProvider.md)
 - [User](docs/User.md)
 - [UserProfile](docs/UserProfile.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Contact us:

+ Information: [info@flexify.io](mailto:info@flexify.io)
+ Sales: [sales@flexify.io](mailto:sales@flexify.io)
+ Support: [support@flexify.io](mailto:support@flexify.io)

