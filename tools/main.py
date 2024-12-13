import typer
import modules.dns_methods as dns_methods 
import modules.who_is as who_is 

app = typer.Typer()

@app.command()
def main(
    domain: str = typer.Argument(..., help="The domain to analyze (e.g., example.com)"), 
    file: bool = False, 
    W: bool = typer.Option(False, "--whois", "-W", help="Perform WHOIS lookup"),
    R: bool = typer.Option(False, "--resolve", "-R", help="Resolve subdomains"),
    Q: bool = typer.Option(False, "--query", "-Q", help="Query specific DNS records"),

):    
    if not any([W, R, Q]):
        print("No action specified. Use --help for more information.")
        raise typer.Exit(code=1)
    if W:
        typer.echo(f"Performing WHOIS lookup for {domain}")
        who_is.whois_resolver(domain, file)
    if R:
        typer.echo(f"Resolving subdomains for {domain}")
        dns_methods.resolve_subdomains(domain, file)
    if Q:
        typer.echo(f"Querying specific DNS records for {domain}")
        dns_methods.query_dns_records(domain, file)   

# Verify if the script is being executed
if __name__ == "__main__":
    app()
