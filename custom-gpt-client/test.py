from custom_gpt_client import CustomGPT
from custom_gpt_client.models import CreateProjectJsonBody, CreateProjectConversationJsonBody, SendMessageToConversationJsonBody
from custom_gpt_client.api.projects import create_project, get_project
from custom_gpt_client.api.conversations import create_project_conversation, send_message_to_conversation
from custom_gpt_client.types import Response
import json
import time


client = CustomGPT(base_url="https://dev.customgpt.ai", token="", timeout=10000)
request_body = CreateProjectJsonBody(project_name='my_project2', sitemap_path='https://adorosario.github.io/small-sitemap.xml')
response = create_project.sync_detailed(client=client, json_body=request_body)
print('Project: ', response.content)
print("\n")

json_project = json.loads(response.content.decode('utf-8'))
project_id = json_project['data']['id']

is_chat_active = 0
while not is_chat_active:
    response_project = get_project.sync_detailed(client=client, project_id=project_id)
    json_project = json.loads(response_project.content.decode('utf-8'))
    print(json_project)
    print("\n")
    is_chat_active = json_project['data']['is_chat_active']
    time.sleep(5)

print(response_project)
print("\n")

conversation_body = CreateProjectConversationJsonBody(name='hamza_sdk_test_converation')
response_conversation = create_project_conversation.sync_detailed(client=client, project_id=project_id, json_body=conversation_body)
print('Conversation: ',response_conversation.content)
print("\n")


json_conversation = json.loads(response_conversation.content)
session_id = json_conversation['data']['session_id']
message_body = SendMessageToConversationJsonBody(prompt='who is tom? in 10 words')
print(session_id)
print(project_id)
print(message_body)
response_message = send_message_to_conversation.sync_detailed(client=client, project_id=project_id, session_id=session_id, json_body=message_body, stream=True)
print('Message: ', response_message)
print("\n")