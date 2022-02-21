from ast import Store
from click import prompt
from dotenv import load_dotenv, load_env
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
open.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nSanti:"
restart_sequence = "\n\nPerson:"
sesion_prompt = "Hi, I've reached my usage limit."

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt=prompt_text
    temperature=0.5,
    max_tokens=94,
    top_p=0.5,
    frequency_penalty=0.15,
    presence_penalty=0
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = sesion_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'