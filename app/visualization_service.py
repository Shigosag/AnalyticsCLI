import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
from rich import print

class VisualizationService:

    @staticmethod
    def safe_chart(df: pd.DataFrame, max_categories: int = 10):
        numeric_cols = df.select_dtypes(include='number').columns
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns

        total_cols = len(numeric_cols) + len(categorical_cols)
        if total_cols == 0:
            print("[bold yellow]No numeric or categorical columns found[/bold yellow]")
            return

        # Terminal output for categorical columns
        for col in categorical_cols:
            counts = df[col].value_counts().head(max_categories)
            print(f"\n[bold blue]Categorical Column: {col}[/bold blue]")
            print(counts.to_string())

        # Matplotlib for pop-up charts
        n_cols = 2
        n_rows = (total_cols + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6*n_cols, 4*n_rows))
        axes = axes.flatten() if total_cols > 1 else [axes]

        i = 0
        # Numeric plots
        for col in numeric_cols:
            sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
            axes[i].set_title(f"{col} distribution")
            i += 1

        # Categorical plots
        for col in categorical_cols:
            counts = df[col].value_counts().head(max_categories)
            sns.barplot(x=counts.index.astype(str), y=counts.values, ax=axes[i])
            axes[i].set_title(f"{col} count")
            axes[i].tick_params(axis='x', rotation=45)
            i += 1

        # Hide extra subplots
        for j in range(i, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def generate_correlation_heatmap(df: pd.DataFrame):
        """Generate a correlation heatmap using seaborn/matplotlib."""
        numeric_df = df.select_dtypes(include='number')
        if numeric_df.empty:
            print("[bold yellow]No numeric columns for correlation heatmap[/bold yellow]")
            return
        corr = numeric_df.corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def terminal_bar_chart(df: pd.DataFrame, x_col: str, y_col: str):
        """Show a simple bar chart in terminal using plotext."""
        # Convert y_col to numeric, ignore errors
        try:
            y_values = pd.to_numeric(df[y_col], errors='coerce')
        except Exception:
            print(f"[bold yellow]Cannot convert column {y_col} to numeric for terminal bar chart[/bold yellow]")
            return

        # Drop rows where y_values is NaN
        valid_rows = df[y_values.notna()]
        x_values = valid_rows[x_col].astype(str).tolist()
        y_values = valid_rows[y_col].tolist()

        if not x_values or not y_values:
            print("[bold yellow]No valid data for terminal bar chart[/bold yellow]")
            return

        pltxt.clear_data()
        pltxt.bar(x_values, y_values)
        pltxt.title("Terminal Bar Chart")
        pltxt.show()

    @staticmethod
    def interactive_chart(df: pd.DataFrame, x_col: str, y_col: str):
        """Generate an interactive Plotly chart (HTML)."""
        # Convert y_col to numeric, skip invalid
        df_copy = df.copy()
        df_copy[y_col] = pd.to_numeric(df_copy[y_col], errors='coerce')
        df_copy = df_copy.dropna(subset=[y_col])

        if df_copy.empty:
            print("[bold yellow]No valid numeric data for interactive chart[/bold yellow]")
            return

        fig = px.bar(df_copy, x=x_col, y=y_col, title="Interactive Plotly Chart")
        fig.show()
