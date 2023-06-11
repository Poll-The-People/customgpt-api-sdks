from custom_gpt_client import CustomGPT
from custom_gpt_client.models import CreateProjectJsonBody, UpdateProjectJsonBody
import json
import time
import os


def test_projects():
    client = CustomGPT(base_url="https://dev.customgpt.ai", token="", timeout=10000)
    # Create a Project
    json_body = CreateProjectJsonBody(project_name='test', sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response = client.create_project(json_body=json_body)
    response_create = json.loads(response.content.decode('utf-8'))
    assert response_create['data']['project_name'] == 'test'
    assert response.status_code == 201

    # Update The Project Name
    json_body = UpdateProjectJsonBody(project_name='test2', sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response = client.update_project(project_id=response_create['data']['id'], json_body=json_body)
    response_update = json.loads(response.content.decode('utf-8'))
    assert response_update['data']['project_name'] == 'test2'
    assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    response = client.get_project(project_id=response_create['data']['id'])
    response_project = json.loads(response.content.decode('utf-8'))
    assert response_project['data']['project_name'] == response_update['data']['project_name']
    assert response.status_code == 200

    # Fetch Created project Stat
    response = client.get_project_stats(project_id=response_create['data']['id'])
    response_stats = json.loads(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert list(response_stats['data'].keys()) == ['pages_found', 'pages_crawled', 'pages_indexed', 'crawl_credits_used', 'query_credits_used', 'total_queries', 'total_words_indexed']
    
    # Delete the project
    response = client.delete_project(project_id=response_create['data']['id'])
    assert response.status_code == 200


from custom_gpt_client.models import CreateProjectConversationJsonBody, UpdateProjectConversationJsonBody, SendMessageToConversationJsonBody

def test_conversations():
    client = CustomGPT(base_url="https://dev.customgpt.ai", token="", timeout=10000)
    json_body = CreateProjectJsonBody(project_name='test', sitemap_path="https://adorosario.github.io/small-sitemap.xml")
    response = client.create_project(json_body=json_body)
    response_create = json.loads(response.content.decode('utf-8'))
    project_id = response_create['data']['id']
    conversation_body = CreateProjectConversationJsonBody(name='test_converation')
    response = client.create_project_conversation(project_id=project_id, json_body=conversation_body)
    response_create = json.loads(response.content.decode('utf-8'))
    session_id = response_create['data']['session_id']
    assert response_create['data']['name'] == 'test_converation'
    assert response.status_code == 201

    # wait for chat active
    is_chat_active = 0
    json_project = {}
    while not is_chat_active:
        response_project = client.get_project(project_id=project_id)
        json_project = json.loads(response_project.content.decode('utf-8'))
        is_chat_active = json_project['data']['is_chat_active']
        time.sleep(5)

    assert json_project['data']['is_chat_active'] == 1
    # Update The Project Conversation Name
    # json_body = UpdateProjectConversationJsonBody(name='test_conversation2')
    # response = client.update_project_conversation(project_id=project_id, session_id=session_id, json_body=json_body)
    # response_update = json.loads(response.content.decode('utf-8'))
    # # assert response_update['data']['name'] == 'test_conversation2'
    # assert response.status_code == 200

    # Get Project By created project Id and assert updated name
    # response = client.get_project_conversations(project_id=project_id)
    # response_project = json.loads(response.content.decode('utf-8'))
    # assert response_project['data']['session_id'] == session_id
    # assert response_project['data']['name'] == 'test_conversation2'
    # assert response.status_code == 200

    # Fetch Created project messages
    response = client.get_project_conversation_messages(project_id=project_id, session_id=session_id)
    response_stats = json.loads(response.content.decode('utf-8'))
    assert response.status_code == 200
    # assert list(response_stats['data'].keys()) == ['pages_found', 'pages_crawled', 'pages_indexed', 'crawl_credits_used', 'query_credits_used', 'total_queries', 'total_words_indexed']
    
    # send message to conversation stream false
    json_body = SendMessageToConversationJsonBody(prompt='Who is Tom? I need a short answer in 10 words.')
    response = client.send_message_to_conversation(project_id=project_id, session_id=session_id, json_body=json_body)
    message_json = json.loads(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert list(message_json['data'].keys()) == ['id', 'created_at', 'updated_at', 'user_id', 'user_query', 'openai_response', 'citations']


    # send message to conversation stream true
    json_body = SendMessageToConversationJsonBody(prompt='Who is Tom? I need a short answer in 10 words.')
    response = client.send_message_to_conversation(project_id=project_id, session_id=session_id, json_body=json_body, stream=True)
    message_json = response.content.decode('utf-8')
    assert response.status_code == 200
    assert message_json.count('data') > 1

    # Delete the project
    response = client.delete_project_conversation(project_id=project_id, session_id=session_id)
    assert response.status_code == 200
