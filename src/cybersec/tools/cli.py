import typer
from cybersec.tools import shodan_sentinel, hash_checker_tool, net_recon
app = typer.Typer()

# This is the main entry point for the CLI application
# It allows users to run different tools from the command line.
# Each tool is registered as a subcommand of the main app

app.add_typer(net_recon.app, name="net-recon")
app.add_typer(hash_checker_tool.app, name="hash-checker")
app.add_typer(shodan_sentinel.app, name="shodan-scanner")

if __name__ == "__main__":
    app()
