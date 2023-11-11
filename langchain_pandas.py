import numpy as np
import pandas as pd
from langchain.llms import OpenAI
from langchain.llms import VertexAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
# from langchain.agents import create_pandas_dataframe_agent
import os
import yaml

try:
    df = pd.read_csv('./langchain_pandas/Sample-Spreadsheet-5000-rows.csv')
except UnicodeDecodeError:
    df = pd.read_csv(
        './langchain_pandas/Sample-Spreadsheet-5000-rows.csv', encoding='latin1')

print("df.shape[0] \n", df.shape[0])
rows, columns = df.shape
print('rows', rows, 'columns', columns)

# define LLM objects
llm = VertexAI()
agent = create_pandas_dataframe_agent(llm, df, verbose=True)

# # use LLM to answer the questions
# for question in config['questions']:
while (True):
    question = input('\033[32m:>')
    if (question == 'close'):
        print('\033[32mbye')
        break

    print(question)
    print(agent.run(question))

print(':-:-:')
