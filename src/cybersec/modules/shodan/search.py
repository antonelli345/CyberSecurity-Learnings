import shodan
import typer
import os
import sys
from dotenv import load_dotenv
from cybersec.modules.utils.export import save_to_csv
from pathlib import Path


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
    if country and (len(country) != 2 or not country.isalpha()):
        print("Invalid country code. Country code must be 2 letters.")
        sys.exit(1)
    query_parts = []
    if keyword:
        query_parts.append(keyword)
    if country:
        query_parts.append(f"country:{country.lower()}")
    if city:
        query_parts.append(f"city:{city.lower()}")
    if port:
        query_parts.append(f"port:{port}")
    if not query_parts:
        print("No search criteria provided. Use --help for more information.")
        sys.exit(1)
    final_query = " ".join(query_parts)
    env_path = Path("./modules/shodan/.env")
    load_dotenv(dotenv_path=env_path)
    api_token = os.getenv('SHODAN_API_KEY')
    if not api_token:
        print("API key not found. Please set the API_KEY in .env file.")
        sys.exit(1)
    api = shodan.Shodan(api_token)
    try:
        results = api.search(final_query, limit=limit)
        output = []
        for i, result in enumerate(results['matches'], start=1):
            ip = result.get('ip_str', 'N/A')
            port = result.get('port', 'N/A')
            org = result.get('org', 'N/A')
            info = f"{i}. IP: {ip}, Port: {port}, Organization: {org}"
            output.append(info)
        typer.echo("\n\n".join(output))
        typer.echo(f"\n[✔] {len(results['matches'])} results found.")
        if file:
            save_to_csv(results, country, city, port, keyword)
    except shodan.APIError as e:
        print(f"[!] Shodan API error: {e}")
        sys.exit(1)
