# -*- coding: utf-8 -*-

import click


@click.group()
def main():
    """Bio2BEL HomoloGene Utilities"""


@main.command()
@click.option('-c', '--connection', help="Custom OLS base url")
def populate(connection):
    """Creates and populates the database"""
    from .manager import Manager
    m = Manager(connection=connection)
    m.populate()


@main.command()
@click.option('-c', '--connection', help="Custom OLS base url")
def drop(connection):
    """Drops all tables"""
    from .manager import Manager
    m = Manager(connection=connection)
    m.drop_all()


@main.command()
def web():
    """Run the web app"""
    from .web import app
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
