import typer
import os
from datetime import date
from modules.scanner import (resolve_subdomains, query_dns_records, get_geo_loc, whois_resolver, scan_ports)
app = typer.Typer()

@app.command()
def main(
    domain: str = typer.Argument(..., help="The domain to analyze (e.g., example.com)"), 
    file: bool = False, 
    W: bool = typer.Option(False, "--whois", "-W", help="WHOIS lookup"),
    R: bool = typer.Option(False, "--resolve", "-R", help="Resolve subdomains"),
    Q: bool = typer.Option(False, "--query", "-Q", help="Query specific DNS records"),
    G: bool = typer.Option(False, "--geolocate", "-G", help="Geolocation"),
    S: bool = typer.Option(False, "--scan", "-S", help="Port scan"),
    max_port: int = typer.Option(1000, "--max-port", "-M", help="Maximum port to scan (default: 1000)")

):    
    if not any([W, R, Q, G, S]):
        print("No action specified. Use --help for more information.")
        raise typer.Exit(code=1)
    
    output = []
    
    if W: # Whois lookup      
        typer.echo(f"Performing WHOIS lookup for {domain}")
        whois_result = whois_resolver(domain)
        output.append("\n".join(whois_result))    
    if R: # Resolve subdomains
        typer.echo(f"Resolving subdomains for {domain}")
        subdomain_results = resolve_subdomains(domain)
        output.append("\n".join(subdomain_results))
    if Q: # Query specific DNS records
        typer.echo(f"Querying specific DNS records for {domain}")
        dns_results = query_dns_records(domain)
        output.append("\n".join(dns_results))
    if G: # Geolocation
        typer.echo(f"Performing geolocation for {domain}")
        geo_loc_result = get_geo_loc(domain)
        output.append("\n".join(geo_loc_result))
    if S: # Port scan
        typer.echo(f"Performing port scan for {domain}")
        port_scan_result = scan_ports(domain, max_port)
        scan_output = ["\nDNS                 Port   Protocol", "-" * 40]
        for dns, port, proto in port_scan_result:
            scan_output.append(f"{dns:<20} {port:<6} {proto.upper()}")
        output.append("\n".join(scan_output))
   
    typer.echo("\n\n".join(output))

    if file:
        output_dir = "./out"
        output_path = os.path.join(output_dir, f"{domain}_output.txt")
        os.makedirs(output_dir, exist_ok=True)
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n\n".join(output))
            typer.echo(f"\n[✔] Output saved to {output_path}")
        except Exception as e:
            typer.echo(f"\n[!] Error while saving the file: {e}")
    
        
# Verify if the script is being executed
if __name__ == "__main__":
    app()
