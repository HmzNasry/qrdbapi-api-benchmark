import typer
import webbrowser
import os
from pathlib import Path
from typing import Optional
from benchmark.core import BenchmarkRunner
from benchmark.visualizer import generate_chart
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def start(
    config: str = "inputs/benchmarks.json",
    system: str = typer.Option(None, help="Specific system to test (e.g., 'fastapi')"),
):
    """
    Run the API Benchmark based on the configuration file.
    """
    runner = BenchmarkRunner(config)
    runner.run(target_system=system)


@app.command()
def visualize(
    file: Optional[str] = typer.Argument(None, help="Path to the results JSON file. If empty, uses the latest run.")
):
    """
    Generate an interactive HTML chart from a results JSON file and open it.
    """
    target_file = file

    if target_file is None:
        output_dir = Path("outputs")
        if not output_dir.exists():
            console.print("[bold red]No 'outputs' directory found. Run a benchmark first![/bold red]")
            raise typer.Exit(1)
        
        json_files = list(output_dir.glob("**/*.json"))
        
        if not json_files:
            console.print("[bold red]No JSON result files found in 'outputs/' or its subdirectories.[/bold red]")
            raise typer.Exit(1)
        
        latest_file = max(json_files, key=os.path.getmtime)
        target_file = str(latest_file)
        console.print(f"[dim]Auto-detected latest file: {target_file}[/dim]")

    if not Path(target_file).exists():
        console.print(f"[bold red]File not found: {target_file}[/bold red]")
        raise typer.Exit(1)
    
    console.print(f"[cyan]Generating interactive chart for {target_file}...[/cyan]")
    html_path = generate_chart(target_file)
    
    console.print(f"[bold green]Interactive chart saved to: {html_path}[/bold green]")
    
    # Open in browser
    abs_path = Path(html_path).resolve()
    console.print(f"[dim]Opening in browser...[/dim]")
    webbrowser.open(f"file://{abs_path}")


if __name__ == "__main__":
    app()
