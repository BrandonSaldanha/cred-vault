import click
from vault import Vault

@click.group()
def cli():
    """Password Manager CLI"""
    pass

@click.command()
@click.argument('site')
@click.argument('username')
@click.argument('password')
def add(site, username, password):
    """Add a new password entry to the vault."""
    vault = Vault(owner="User")
    vault.add_entry(site, username, password)
    vault.save("vault.dat")
    click.echo(f"Added entry for {site}")

@click.command()
def list_entries():
    """List all password entries in the vault."""
    vault = Vault(owner="User")
    vault.load("vault.dat")
    vault.list_entries()
    
@click.command()
@click.argument('filepath')
@click.argument('key')
def save(filepath):
    """Save the vault to a file."""
    vault = Vault(owner="User")
    vault.save(filepath)
    click.echo(f"Vault saved to {filepath}")

# add the command to the CLI group
cli.add_command(add)
cli.add_command(list_entries)
cli.add_command(save)

if __name__ == '__main__':
    cli()
    # Run the CLI