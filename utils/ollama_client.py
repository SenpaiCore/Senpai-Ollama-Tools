import ollama
from rich.console import Console

console = Console()

def get_ollama_response(prompt: str, model: str = "llama3.2") -> str:
    """Simple function to get response from local Ollama"""
    try:
        console.print(f"[cyan]Thinking with {model}...[/cyan]")
        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return f"Error: {str(e)}"
