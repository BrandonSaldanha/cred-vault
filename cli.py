import os
import click
from vault import Vault

API_URL = "https://ecu18zixz9.execute-api.us-east-1.amazonaws.com/dev/passwords"  # ← check my URL

@click.group()
def cli():
    """Password Manager CLI"""
    pass

@click.command()
@click.argument('site')
@click.argument('username')
@click.argument('password')
@click.argument('user_id')
def add(site, username, password, user_id):
    """Add a new password entry to the cloud vault."""
    try:
        vault = Vault(owner=user_id, api_url=API_URL)
        vault.upload_entry(site, username, password)
        click.echo(f" Added entry for {site}")
    except ValueError as e:
        raise click.ClickException(str(e))
    except Exception as e:
        raise click.ClickException(f"Upload failed: {str(e)}")

@click.command()
@click.argument('user_id')
def list_entries(user_id):
    """List all password entries from the cloud vault."""
    try:
        vault = Vault(owner=user_id, api_url=API_URL)
        vault.fetch_entries_from_cloud()
        vault.list_entries()
    except Exception as e:
        raise click.ClickException(f"Fetch failed: {str(e)}")
    
# add the command to the CLI group
cli.add_command(add)
cli.add_command(list_entries)

if __name__ == '__main__':
    cli()
    # Run the CLI