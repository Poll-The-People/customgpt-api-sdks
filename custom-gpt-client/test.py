from custom_gpt_client import CustomGPT
from custom_gpt_client.models import CreateProjectJsonBody
from custom_gpt_client.api.projects import list_projects

client = CustomGPT(
    base_url="https://dev.customgpt.ai", token="13|0tozJdzYhUrQ7HojFRSFzwtMAPNJXwAbYRhaNFMB", timeout=10000
)
request_body = CreateProjectJsonBody(
    project_name="my_project2", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
)
response = client.create_project(json_body=request_body)
print("Project: ", response.content)
response_list = list_projects.sync_detailed(client=client)
print(response_list)