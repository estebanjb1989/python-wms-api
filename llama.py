import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"  # Change to your model name (e.g., mistral, codellama, etc.)

def ask_ollama(question):
    payload = {
        "model": MODEL,
        "prompt": question,
        "stream": False  # Set to True if you want streamed response
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    while True:
        question = input("You: ")
        if question.lower() in {"exit", "quit"}:
            break
        answer = ask_ollama(question)
        print("Ollama:", answer)
