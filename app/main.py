# +------------------------------------------------------------------+
# |            AnalyticsCLI – Production-Ready Data Analyst CLI Tool |
# |                                        Copyright 2026, Shigosag. |
# |                             GitHub: https://github.com/Shigosag  |
# +------------------------------------------------------------------+
# property copyright "Copyright 2026, Shigosag"

# --- Author: Shigosag         

#            \\|//             +-+-+-+-+-+-+-+-+             \\|// 
#           ( o o )            |S|h|i|g|o|s|a|g|            ( o o )
#    ~~~~oOOo~(_)~oOOo~~~~     +-+-+-+-+-+-+-+-+     ~~~~oOOo~(_)~oOOo~~~~

import sys
import typer
from datetime import datetime
from rich import print
from app.logger import logger
from app.loader_service import LoaderService
from app.profiling_service import ProfilingService
from app.cleaning_service import CleaningService
from app.visualization_service import VisualizationService
from app.export_service import ExportService
from app.database.duckdb_manager import DuckDBManager
from app.ui.banner import show_banner
from app.ui.menu import show_menu
from app.ui.progress import show_progress

app = typer.Typer()


@app.command()
def analyze(file_path: str):
    """Analyze dataset."""
    try:
        show_banner()
        show_progress(description="Loading data...")

        df = LoaderService.load_data(file_path)
        cleaned_df = CleaningService.remove_duplicates(df)
        cleaned_df = CleaningService.fill_missing_values(cleaned_df)

        # Profile
        profile = ProfilingService.generate_profile(cleaned_df)
        print("\n[bold green]Dataset Profile[/bold green]")
        print(profile)

        # Exports (CSV, Excel)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ExportService.export_csv(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.csv")
        ExportService.export_excel(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.xlsx")

        # DuckDB
        db = DuckDBManager()
        db.register_dataframe("dataset", cleaned_df)
        result = db.query("SELECT COUNT(*) AS total_rows FROM dataset")
        print("\n[bold blue]SQL Query Result[/bold blue]")
        print(result)

        # Exports PDF
        import pandas as pd
        result_df = cleaned_df if hasattr(cleaned_df, "to_string") else pd.DataFrame(cleaned_df)
        ExportService.export_pdf_report(result_df, path=f"exports/dataset_report_{timestamp}.pdf")

        # Visualization
        VisualizationService.safe_chart(cleaned_df)

        print("[bold green]Analyze completed successfully[/bold green]")
        logger.info("Analyze completed successfully")

    except Exception as error:
        logger.exception(error)
        print(f"[bold red]Error:[/bold red] {error}")


def clean(file_path: str):
    """Clean dataset."""
    try:
        show_banner()
        show_progress(description="Loading data for cleaning...")

        df = LoaderService.load_data(file_path)
        cleaned_df = CleaningService.remove_duplicates(df)
        cleaned_df = CleaningService.fill_missing_values(cleaned_df)

        # Exports
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ExportService.export_csv(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.csv")
        ExportService.export_excel(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.xlsx")

        # Exports PDF
        import pandas as pd
        result_df = cleaned_df if hasattr(cleaned_df, "to_string") else pd.DataFrame(cleaned_df)
        ExportService.export_pdf_report(result_df, path=f"exports/dataset_report_{timestamp}.pdf")

        print("[bold green]Data cleaned successfully[/bold green]")
        logger.info("Clean completed successfully")

    except Exception as error:
        logger.exception(error)
        print(f"[bold red]Error:[/bold red] {error}")


def visualize(file_path: str):
    """Visualize dataset."""
    try:
        show_banner()
        show_progress(description="Loading data for visualization...")

        df = LoaderService.load_data(file_path)
        cleaned_df = CleaningService.remove_duplicates(df)
        cleaned_df = CleaningService.fill_missing_values(cleaned_df)

        VisualizationService.safe_chart(cleaned_df)
        print("[bold green]Visualization completed[/bold green]")
        logger.info("Visualization completed successfully")

    except Exception as error:
        logger.exception(error)
        print(f"[bold red]Error:[/bold red] {error}")


def run_all(file_path: str):
    try:
        show_banner()
        show_progress(description="Loading data...")

        # Load & clean
        df = LoaderService.load_data(file_path)
        cleaned_df = CleaningService.remove_duplicates(df)
        cleaned_df = CleaningService.fill_missing_values(cleaned_df)

        # Profile
        profile = ProfilingService.generate_profile(cleaned_df)
        print("\n[bold green]Dataset Profile[/bold green]")
        print(profile)

        # Exports (CSV, Excel)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ExportService.export_csv(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.csv")
        ExportService.export_excel(cleaned_df, path=f"exports/dataset_cleaned_{timestamp}.xlsx")

        # DuckDB SQL
        db = DuckDBManager()
        db.register_dataframe("dataset", cleaned_df)
        result = db.query("SELECT COUNT(*) AS total_rows FROM dataset")
        print("\n[bold blue]SQL Query Result[/bold blue]")
        print(result)

        # Exports PDF
        import pandas as pd
        result_df = cleaned_df if hasattr(cleaned_df, "to_string") else pd.DataFrame(cleaned_df)
        ExportService.export_pdf_report(result_df, path=f"exports/dataset_report_{timestamp}.pdf")

        # Visualization
        VisualizationService.safe_chart(cleaned_df)

        print("[bold green]Run All completed successfully[/bold green]")
        logger.info("Run All completed successfully")

    except Exception as error:
        logger.exception(error)
        print(f"[bold red]Error in run_all:[/bold red] {error}")


def main():
    typer_args = sys.argv[1:]
    if typer_args:
        # CLI path provided → show menu with path pre-filled
        file_path = typer_args[0]
        show_menu(
            analyze=analyze,
            clean=clean,
            visualize=visualize,
            run_all=run_all,
            default_file_path=file_path
        )
    else:
        # No CLI arg → ask user to enter file path in menu
        show_menu(
            analyze=analyze,
            clean=clean,
            visualize=visualize,
            run_all=run_all
        )


if __name__ == "__main__":
    main()
