import json_manag
import click


@click.group()
def cli():
    pass


@cli.command()
def user():
    data = json_manag.read_json()
    print(data)


if __name__ == '__main__':
    cli()
