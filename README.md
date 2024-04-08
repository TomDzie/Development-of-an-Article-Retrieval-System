# Development-of-an-Article-Retrieval-System  
## Setup:  
1. Install dependencies:   
   ```
   pip install -r requirements.txt  
   ```
2. Set your OpenAI API Key:  
   ```
   os.environ["OPENAI_API_KEY"] = 'API_KEY'
   ```

## Usage  
1. Run main
   ```
   python main.py
   ```
2. Write a query
   example:  
   <img width="360" alt="image" src="https://github.com/TomDzie/Development-of-an-Article-Retrieval-System/assets/117634603/71a49107-2cf9-44c1-b459-4fc783fef7c1">  

3. Output:
   relative articles:  
   <img width="782" alt="image" src="https://github.com/TomDzie/Development-of-an-Article-Retrieval-System/assets/117634603/0ea1d2ff-9d58-4320-8d79-f5c2ae6d45e1">

   answer:
   <img width="1131" alt="image" src="https://github.com/TomDzie/Development-of-an-Article-Retrieval-System/assets/117634603/bb90f8fa-8f98-4dc4-9f0f-c255f5788b67">





## Configuration  

- main.py: Contains the main script to interact with the RAG System.  
- llama_index: Directory containing the LLAMA Index library.  
- RAG system/data: Directory for storing data used by the system.  
- prompts.py: File for defining prompts used by the system.  
- RAG system/tools: Directory for storing custom tools used by the system.  
- RAG system/agent.py: Contains the ReActAgent class for interacting with the LLAMA Index.  
- RAG system/llms.py: Contains the OpenAI class for interfacing with the GPT-3.5 model.  
