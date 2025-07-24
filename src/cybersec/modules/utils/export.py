import os
import typer


def save_to_txt(domain, output):
    output_dir = "./out"
    output_path = os.path.join(output_dir, f"{domain}_output.txt")
    os.makedirs(output_dir, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(output))
        typer.echo(f"\n[✔] Output saved to {output_path}")
    except Exception as e:
        typer.echo(f"\n[!] Error while saving the file: {e}")


def save_to_csv(results, country, city, port, keyword):
    output_dir = "./out"
    output_path = os.path.join(output_dir, "shodan_results.csv")
    os.makedirs(output_dir, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("IP,Port,Organization\n")
            # Assuming results is a list of dictionaries with keys 'ip',
            # 'port', and 'org'
            for result in results['matches']:
                ip = result.get('ip_str', 'N/A')
                port = result.get('port', 'N/A')
                org = result.get('org', 'N/A')
                f.write(f"{ip},{port},{org}\n")
        typer.echo(f"\n[✔] Output saved to {output_path}")
    except Exception as e:
        typer.echo(f"\n[!] Error while saving the file: {e}")
