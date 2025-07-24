import typer
import sys
import os
from cybersec.modules.shodan import search
#from cybersec.modules.shodan import ip_info
#from cybersec.modules.shodan import vuln
# Ensure the modules directory is in the Python path
# This allows us to import modules from the parent directory
# This is necessary if the script is run from a different directory



app = typer.Typer()


@app.command(name="search")
def shodan_search(
    country: str = typer.Option(
        None, "--country", "-c", help="Code of the country (ex: US, FR, BR.)"
    ),
    city: str = typer.Option(
        None, "--city", "-ci", help="City name (ex: Paris, London.)"
    ),
    port: int = typer.Option(
        None, "--port", "-p", help="Port number (ex: 22, 80, 443.)"
    ),
    keyword: str = typer.Option(
        None, "--keyword", "-k", help="Keyword to search (ex: Apache, Nginx.)"
    ),
    limit: int = typer.Option(
        10, "--limit", "-l", help="Number of results to return (default: 10)"
    ),
    file: bool = typer.Option(
        False, "--file", "-f", help="Save results to a CSV file."
    ),
):
    search.shodan_search(country, city, port, keyword, limit, file)


@app.command(name="ip-info")
def ip_info_command():
    ip_info.ip_info() # type: ignore


@app.command(name="vuln")
def vuln_check():
    vuln.vuln_check() # type: ignore


if __name__ == "__main__":
    app()
