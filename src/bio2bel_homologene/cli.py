# -*- coding: utf-8 -*-

import click

from .constants import DEFAULT_CACHE_CONNECTION


@click.group()
def main():
    """Bio2BEL HomoloGene Utilities"""


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def populate(connection):
    """Creates and populates the database"""
    from .manager import Manager
    m = Manager(connection=connection)
    m.populate()


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def drop(connection):
    """Drops all tables"""
    from .manager import Manager
    m = Manager(connection=connection)
    m.drop_all()


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def web(connection):
    """Run the web app"""
    from .web import create_application
    app = create_application(connection=connection)
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
