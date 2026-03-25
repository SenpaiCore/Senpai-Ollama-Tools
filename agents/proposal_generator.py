from utils.ollama_client import get_ollama_response
from rich.console import Console
import sys

console = Console()

def generate_proposal(client_name: str, project_desc: str, budget: str = None):
    prompt = f"""
You are a professional freelance developer specializing in AI and web development.

Write a highly professional, personalized proposal for the following client:

Client: {client_name}
Project: {project_desc}
{f"Budget: {budget}" if budget else ""}

Requirements:
- Keep it concise (150-250 words)
- Sound confident but friendly
- Highlight relevant skills (AI Agents, Automation, Web Dev)
- Mention that you use local AI tools for faster delivery
- End with clear next steps and call to action

Write in natural, professional English. Use Hinglish only if needed.
"""

    console.print(f"[bold green]Generating proposal for {client_name}...[/bold green]")
    proposal = get_ollama_response(prompt, model="llama3.2")
    
    console.print("\n[bold]=== YOUR PROPOSAL ===[/bold]\n")
    console.print(proposal)
    console.print("\n" + "="*60)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        client = sys.argv[1]
        desc = sys.argv[2] if len(sys.argv) > 2 else "AI automation project"
        budget = sys.argv[3] if len(sys.argv) > 3 else None
        generate_proposal(client, desc, budget)
    else:
        console.print("[yellow]Usage: python proposal_generator.py \"Client Name\" \"Project Description\" \"Optional Budget\"[/yellow]")
        # Example
        generate_proposal("Rahul Sharma", "I need an AI agent that can automatically reply to client emails and manage my freelance inbox", "₹35,000")
