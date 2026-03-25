from agents.proposal_generator import generate_proposal
from rich.console import Console

console = Console()

console.print("[bold magenta]=== Senpai-Ollama-Tools Demo ===[/bold magenta]\n")

# Example 1: Freelance Proposal
console.print("[bold cyan]1. Generating Freelance Proposal...[/bold cyan]")
generate_proposal(
    client_name="Rahul Sharma",
    project_desc="I need an intelligent AI agent that can automatically reply to client emails and manage my freelance inbox",
    budget="₹35,000"
)

console.print("\n" + "="*70)

# Example 2: Another Proposal
console.print("[bold cyan]2. Another Proposal Example...[/bold cyan]")
generate_proposal(
    client_name="Priya Patel",
    project_desc="Build a local AI tool for generating YouTube Shorts scripts and captions",
    budget="₹25,000"
)

console.print("\n[green]Demo completed! You can now create your own agents.[/green]")
