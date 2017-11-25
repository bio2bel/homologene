# -*- coding: utf-8 -*-

""" This module contains the flask application to visualize the db

when pip installing

.. source-code:: sh

    pip install bio2bel_homologene[web]

"""

import flask_admin
from flask import Blueprint, Flask, abort, current_app, jsonify
from flask_admin.contrib.sqla import ModelView

from bio2bel_homologene.manager import Manager
from bio2bel_homologene.models import *

ui = Blueprint('ui', __name__)


@ui.route('/api/species/<tax_id>')
def get_species_genes(tax_id):
    """Gets genes from this taxonomy id"""
    species = current_app.manager.session.query(Species).filter(Species.taxonomy_id == tax_id).one_or_none()
    if species is None:
        abort(404, 'Species {} not found'.format(tax_id))

    return jsonify([
        {
            'entrez_id': gene.gene_id,
            'symbol': gene.gene_symbol
        }
        for gene in species.genes
    ])


def add_admin(app, session, url=None):
    admin = flask_admin.Admin(app, url=(url or '/'))
    admin.add_view(ModelView(Homologene, session))
    admin.add_view(ModelView(Gene, session))
    admin.add_view(ModelView(Species, session))
    return admin


def create_application(connection=None, url=None):
    app = Flask(__name__)
    app.manager = Manager(connection=connection)
    add_admin(app, app.manager.session, url=url)
    return app


if __name__ == '__main__':
    app = create_application()
    app.run(debug=True, host='0.0.0.0', port=5000)
