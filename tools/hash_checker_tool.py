import hashlib
import typer

app = typer.Typer()
@app.command(
    help="Analyze a file for specific hash types (MD5, SHA1, SHA256)."
)

def main(
    src_file: str = typer.Argument(
        ..., help="The file to analyze (e.g., hashes.txt)"
    ),
    md5: bool = False,
    sha1: bool = False,
    sha256: bool = False,

    file: bool = typer.Option(
        False, "--file", "-f", help="save output to a file"
    )
): 


    def md5_hasher(file_path: str) -> str:
        with open(file_path, "rb") as f:
            file_content = f.read()
        md5_hash = hashlib.md5(file_content).hexdigest()
        return md5_hash

    def sha1_hasher(file_path: str) -> str:
        with open(file_path, "rb") as f:
            file_content = f.read()
        sha1_hash = hashlib.sha1(file_content).hexdigest()
        return sha1_hash

    def sha256_hasher(file_path: str) -> str:
        with open(file_path, "rb") as f:
            file_content = f.read()
        sha256_hash = hashlib.sha256(file_content).hexdigest()
        return sha256_hash


    if not (md5 or sha1 or sha256):
        raise typer.BadParameter("At least one hash type must be specified.")

    if md5:
        print(f"Analyzing file: {src_file} with hashtype: MD5")
        md5_hash = md5_hasher(src_file)
        print(f"MD5 Hash: {md5_hash}")

    elif sha1:
        print(f"Analyzing file: {src_file} with hashtype: SHA1")
        sha1_hash = sha1_hasher(src_file)
        print(f"SHA1 Hash: {sha1_hash}")

    elif sha256:
        print(f"Analyzing file: {src_file} with hashtype: SHA256")
        sha256_hash = sha256_hasher(src_file)
        print(f"SHA256 Hash: {sha256_hash}")

if __name__ == "__main__":
    app()


