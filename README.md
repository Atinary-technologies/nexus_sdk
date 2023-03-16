# Nexus SDK
As part of Atinary™ Nexus, we offer a downloadable software development kit (SDK) client, which facilitates the access to the application programming interface (API) entry point. This API allows users to manage their project subscriptions and to share files among collaborators involved in the same project(s). The api usage requires an `API KEY`, associated to your Atinary™ Nexus account. You can generate your `API KEY` on your [account information page](https://home.atinary.com/user).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen


Check out the **tutorial** for a step by step guide: [tutorial/getting_started.ipynb](tutorial/getting_started.ipynb). 

For more information on the API, please visit [https://scientia.atinary.com/nexus](https://scientia.atinary.com/nexus)
.

### Getting started 

The Nexus SDK supports a variety of operating systems and only requires to have  Python 2.7 or 3.4+.

#### Installation
###### Option 1: pip install 

From GitHub, you can install directly using:

```sh
pip install git+https://github.com/atinary-technologies/nexus_sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/atinary-technologies/nexus_sdk.git`)

Then import the package:
```python
import nexus_sdk
```

###### Option 2: Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nexus_sdk
```

#### Running the Nexus SDK

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import nexus_sdk
from nexus_sdk.rest import ApiException


# Defining the host is optional and defaults to https://scientia.atinary.com/nexus/api
# Configure API key authorization: api_key
# See configuration.py for a list of all supported configuration parameters.
configuration = nexus_sdk.Configuration(
    host = "https://scientia.atinary.com/nexus/api",
    api_key = {
        'X-API-KEY': 'YOUR_API_KEY'
    }
)


# To start managing your projects, enter a context with an instance of the API client for Projects
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    projects = nexus_sdk.ProjectsApi(api_client)
    try:
        # List project subscriptions
        api_response = projects.list_projects()
        print("\nList of projects before project creation: \n", api_response.objects)

        # Create a new project
        project_create_req = nexus_sdk.ProjectCreateReq(
                                   project_name="project_1",
                                   project_description="My first project"
                              )
        api_response = projects.create_project(project_create_req=project_create_req)
        project_id = api_response.object.id # String with project id
        
        
        # List project subscriptions
        api_response = projects.list_projects()
        print("\nList of projects after project creation: \n", api_response.objects)

        # Subscribe users to a project (only available to project owner)
        project_subscribe_req = nexus_sdk.ProjectSubscribeReq(email_list=['email1@domain.com', 'email2@domain.com'])
        projects.subscribe_users(project_id, project_subscribe_req=project_subscribe_req)

        # Get project details
        api_response = projects.get_project(project_id)
        print("\nProject details: \n", api_response.object)

    except ApiException as e:
        print("Exception when calling an endpoint from ProjectsApi: %s\n" % e)


# To start managing your files, enter a context with an instance of the API client for Files
with nexus_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    files = nexus_sdk.FilesApi(api_client)
    try:
        # List files associated to project with project_id
        api_response = files.list_files(project_id=project_id)
        print("\nList of files before file upload: \n", api_response.objects)

        # Upload a file
        group_type = 'parameters'
        inline_object = nexus_sdk.InlineObject(file='data/wine_data.csv')
        api_response = files.upload_file(project_id, group_type, inline_object=inline_object)
        file_id = api_response.object.id # String with file id

        # List files associated to project with project_id
        api_response = files.list_files(project_id=project_id)
        print("\nList of files after file upload: \n", api_response.objects)

        # Download the file
        api_response = files.download_file(file_id)
        print("\nFile downloaded to:", api_response)

        # Delete the file
        files.delete_file(file_id)

    except ApiException as e:
        print("Exception when calling an endpoint from ManageFilesApi: %s\n" % e)


# To finalize the example, we delete the project by using an instance of the API client for Projects.
# Note that we can delete the project in this case because there are no subscriptions or files associated to it.
with nexus_sdk.ApiClient(configuration) as api_client:
    projects = nexus_sdk.ProjectsApi(api_client)
    try:

        # Delete project (only available to project owner)
        projects.delete_project(project_id)

    except ApiException as e:
        print("Exception when calling an endpoint from ProjectsApi: %s\n" % e)
```

### Documentation for API Endpoints

All URIs are relative to *https://scientia.atinary.com/nexus/api/latest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**health_check**](docs/AdminApi.md#health_check) | **GET** /Healthcheck | Health check
*AdminApi* | [**service_information**](docs/AdminApi.md#service_information) | **GET** /ServiceInfo | Service information.
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /Files/{file_id} | Delete a file
*FilesApi* | [**delete_files**](docs/FilesApi.md#delete_files) | **POST** /Files/delete | 
*FilesApi* | [**download_file**](docs/FilesApi.md#download_file) | **GET** /Files/{file_id} | Download a file
*FilesApi* | [**list_files**](docs/FilesApi.md#list_files) | **GET** /Files | List available files for a project
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /Files | Upload a file under a project
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /Projects | Create a new project
*ProjectsApi* | [**create_tutorial_project**](docs/ProjectsApi.md#create_tutorial_project) | **POST** /Tutorial | Create the tutorial project
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /Projects/{project_id} | Delete a project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /Projects/{project_id} | Get project information
*ProjectsApi* | [**list_projects**](docs/ProjectsApi.md#list_projects) | **GET** /Projects | List project subscriptions
*ProjectsApi* | [**subscribe_users**](docs/ProjectsApi.md#subscribe_users) | **POST** /Projects/{project_id}/Subscribe | Add users to a project
*ProjectsApi* | [**unsubscribe**](docs/ProjectsApi.md#unsubscribe) | **POST** /Projects/{project_id}/Unsubscribe | Unsubscribe from a project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /Projects/{project_id} | Update project name, description and owner


### Documentation For Models

 - [AvailableFile](docs/AvailableFile.md)
 - [AvailableFilesSummary](docs/AvailableFilesSummary.md)
 - [AvailableProject](docs/AvailableProject.md)
 - [CreateProjectResponse](docs/CreateProjectResponse.md)
 - [DeleteFilesReq](docs/DeleteFilesReq.md)
 - [GenericResponse](docs/GenericResponse.md)
 - [HealthCheckReport](docs/HealthCheckReport.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListProjectsResponse](docs/ListProjectsResponse.md)
 - [ProjectCreateReq](docs/ProjectCreateReq.md)
 - [ProjectDetail](docs/ProjectDetail.md)
 - [ProjectDetailResponse](docs/ProjectDetailResponse.md)
 - [ProjectSubscribeReq](docs/ProjectSubscribeReq.md)
 - [ProjectUnsubscribeReq](docs/ProjectUnsubscribeReq.md)
 - [ProjectUpdateReq](docs/ProjectUpdateReq.md)
 - [Result](docs/Result.md)
 - [ServiceInfo](docs/ServiceInfo.md)
 - [ServiceInfoResponse](docs/ServiceInfoResponse.md)
 - [UploadResponse](docs/UploadResponse.md)


### Documentation For Authorization


#### api_key

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


#### tokens

- **Type**: Bearer authentication (JWT)



### Experiencing problems?

Please create a [new issue](https://github.com/atinary-technologies/nexus_sdk/issues/new/choose) and describe your problem in detail so we can fix it.


### Contact 

support@atinary.com
support@atinary.com
support@atinary.com

