# CustomGPT Python API SDK

### Welcome to CustomGPT's Official Python SDK!

The CustomGPT Python API SDK offers users access to the number one RAG system's REST API from any Python application.
The library offers both synchronous and asynchronous clients, as well as definitions for all request params and response fields.

## Documentation

The full documentation can be found online at [https://docs.customgpt.ai/reference/i-api-homepage](https://docs.customgpt.ai/reference/i-api-homepage)

## Usage
### First, create a client:

```python
from customgpt_client import CustomGPT

CustomGPT.api_key="SuperSecretToken"
```

Now you can access all of our models.
An example request will look like this:

### Creating a Project Synchronously:

```python
response = CustomGPT.Project.create(project_name='Test', sitemap_path='https://example.com/test.xml', file_data_retension=False, file=file)
project_id = response.data.id
```

### Or do the same thing with an async version:

```python
response = await CustomGPT.Project.acreate(project_name='Test', sitemap_path='https://example.com/test.xml', file_data_retension=False, file=file)
project_id = response.data.id
```

## Tests
Fill your credentials in customgpt_client/tests/credentials.py in base_url and api_key
```python
def credentials():
    return (base_url, api_key)
```
