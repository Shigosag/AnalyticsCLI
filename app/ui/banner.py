from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]Analytics CLI[/bold cyan]\n[bright_red]by Shigosag[/bright_red]\nModern Data Analyst Tool",
            border_style="green"
        )
    )
