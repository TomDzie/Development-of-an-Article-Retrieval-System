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

## Configuration  

- main.py: Contains the main script to interact with the RAG System.  
- llama_index: Directory containing the LLAMA Index library.  
- RAG system/data: Directory for storing data used by the system.  
- prompts.py: File for defining prompts used by the system.  
- RAG system/tools: Directory for storing custom tools used by the system.  
- RAG system/agent.py: Contains the ReActAgent class for interacting with the LLAMA Index.  
- RAG system/llms.py: Contains the OpenAI class for interfacing with the GPT-3.5 model.  
