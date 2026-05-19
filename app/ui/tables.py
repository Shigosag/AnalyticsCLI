from rich.console import Console
from rich.table import Table

console = Console()

def show_summary_table(df):
    table = Table(title="Dataset Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Rows", str(df.shape[0]))
    table.add_row("Columns", str(df.shape[1]))
    console.print(table)
