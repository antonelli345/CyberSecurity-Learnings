import typer
import os
from datetime import date
import modules.dns_methods as dns_methods 
import modules.who_is as who_is
import modules.geo_loc as geo_loc

app = typer.Typer()

@app.command()
def main(
    domain: str = typer.Argument(..., help="The domain to analyze (e.g., example.com)"), 
    file: bool = False, 
    W: bool = typer.Option(False, "--whois", "-W", help="WHOIS lookup"),
    R: bool = typer.Option(False, "--resolve", "-R", help="Resolve subdomains"),
    Q: bool = typer.Option(False, "--query", "-Q", help="Query specific DNS records"),
    G: bool = typer.Option(False, "--geolocate", "-G", help="Geolocation"),
):    
    if not any([W, R, Q, G]):
        print("No action specified. Use --help for more information.")
        raise typer.Exit(code=1)
    
    output = []
    
    if W: # Whois lookup      
        typer.echo(f"Performing WHOIS lookup for {domain}")
        whois_result = who_is.whois_resolver(domain)
        output.append("\n".join(whois_result))    
    if R: # Resolve subdomains
        typer.echo(f"Resolving subdomains for {domain}")
        subdomains_result = dns_methods.resolve_subdomains(domain)
        output.append("\n" .join(subdomains_result))
    if Q: # Query specific DNS records
        typer.echo(f"Querying specific DNS records for {domain}")
        dns_results = dns_methods.query_dns_records(domain)   
        output.append("\n" .join(dns_results))
    if G: # Geolocation
        typer.echo(f"Performing geolocation for {domain}")
        geo_loc_result = geo_loc.get_geo_loc(domain)
        output.append("\n".join(geo_loc_result))
        
    if file:
        # Relative path to the output directory
        output_dir = "./tools/out"
        output_path = os.path.join(output_dir, f"{domain}_output.txt")
        # Validating the output directory
        os.makedirs(output_dir, exist_ok=True)
        try:
            # Open the file in write mode
            with open(output_path, "w", encoding = "utf-8") as f:
                f.write("\n\n".join(output))
            typer.echo(f"Output saved to {output_path}")
        except Exception as e:
            typer.echo(f"Error while saving the file: {e}")    
        
# Verify if the script is being executed
if __name__ == "__main__":
    app()
