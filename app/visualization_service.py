import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotext as pltxt
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

        for col in categorical_cols:
            counts = df[col].value_counts().head(max_categories)
            print(f"\n[bold blue]Categorical Column: {col}[/bold blue]")
            print(counts.to_string())

        n_cols = 2
        n_rows = (total_cols + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6*n_cols, 4*n_rows))
        axes = axes.flatten() if total_cols > 1 else [axes]

        i = 0
        for col in numeric_cols:
            sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
            axes[i].set_title(f"{col} distribution")
            i += 1
        for col in categorical_cols:
            counts = df[col].value_counts().head(max_categories)
            sns.barplot(x=counts.index.astype(str), y=counts.values, ax=axes[i])
            axes[i].set_title(f"{col} count")
            axes[i].tick_params(axis='x', rotation=45)
            i += 1
        for j in range(i, len(axes)):
            axes[j].axis('off')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def interactive_chart(df: pd.DataFrame, x_col: str, y_col: str, output_html="exports/interactive_chart.html"):
        df_copy = df.copy()
        df_copy[y_col] = pd
