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
