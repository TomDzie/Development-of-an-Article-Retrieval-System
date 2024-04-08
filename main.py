from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import new_prompt, context
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI

os.environ["OPENAI_API_KEY"] = 'API_KEY'
load_dotenv()

data_path = os.path.join("RAG system\\data", "medium.csv")
data_df = pd.read_csv(data_path)

population_query_engine = PandasQueryEngine(
    df=data_df, verbose=True,
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="info from Medium articles",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)