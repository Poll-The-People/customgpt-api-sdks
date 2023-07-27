# CustomGPT SDK

## Usage
First, create a client:

```python
from customgpt_client import CustomGPT

CustomGPT.api_key="SuperSecretToken"
```

Now you can access to all of our Models:
Example Request will be like this:

Creating a Project synchronously:

```python
response = CustomGPT.Project.create(project_name='Test', sitemap_path='https://example.com/test.xml', file_data_retension=False, file=file)
project_id = response.data.id
```

Or do the same thing with an async version:

```python
response = await CustomGPT.Project.acreate(project_name='Test', sitemap_path='https://example.com/test.xml', file_data_retension=False, file=file)
project_id = response.data.id
```
