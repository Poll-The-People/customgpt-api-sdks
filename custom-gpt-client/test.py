from custom_gpt_client import CustomGPT
from custom_gpt_client.models import CreateProjectJsonBody, CreateProjectConversationJsonBody, SendMessageToConversationJsonBody
import json
import time

client = CustomGPT(
    base_url="https://dev.customgpt.ai", token="", timeout=10000
)
request_body = CreateProjectJsonBody(
    project_name="my_project2", sitemap_path="https://adorosario.github.io/small-sitemap.xml"
)
# response = client.create_project(json_body=request_body)
# project_json = json.loads(response.content.decode('utf-8'))
# project_id = project_json['data']['id']
# is_chat_active = 0
# while not is_chat_active:
#     response_project = client.get_project(project_id=project_id)
#     json_project = json.loads(response_project.content.decode('utf-8'))
#     print(json_project)
#     is_chat_active = json_project['data']['is_chat_active']
#     time.sleep(5)
project_id = 187
conversation_body = CreateProjectConversationJsonBody(name='test_converation')
response = client.create_project_conversation(project_id=project_id, json_body=conversation_body)
response_create = json.loads(response.content.decode('utf-8'))
session_id = 'f5755e0f-3007-47bf-9b93-de2cd0b2765b'

# response_create['data']['session_id']
# print(session_id)
json_body = SendMessageToConversationJsonBody(prompt='Who is Tom? I need a short answer in 10 words.')
response = client.send_message_to_conversation(project_id=project_id, session_id=session_id, json_body=json_body, stream=True)
print(response)
