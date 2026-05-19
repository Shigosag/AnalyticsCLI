from rich.console import Console

console = Console()

def show_menu(analyze, clean, visualize, run_all, default_file_path=None):
    # Use default path if provided, else ask user
    if default_file_path:
        file_path = default_file_path
        console.print(f"[bold green]Using provided file path:[/bold green] {file_path}")
    else:
        file_path = console.input("[bold yellow]Enter file path (CSV/Excel/JSON): [/bold yellow] ")

    while True:
        console.print("\n[bold cyan]Choose an option:[/bold cyan]")
        console.print("[1] Analyze Data")
        console.print("[2] Clean Data")
        console.print("[3] Visualize Data")
        console.print("[4] Run All (Analyze + Clean + Visualize)")
        console.print("[5] Exit")

        choice = console.input("[bold yellow]Enter choice:[/bold yellow] ")

        if choice == "1":
            analyze(file_path)
        elif choice == "2":
            clean(file_path)
        elif choice == "3":
            visualize(file_path)
        elif choice == "4":
            run_all(file_path)
        elif choice == "5":
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
