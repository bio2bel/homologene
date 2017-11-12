# -*- coding: utf-8 -*-

""" This module contains the flask application to visualize the db

when pip installing

.. source-code:: sh

    pip install bio2bel_chebi[web]

"""

import flask_admin
from flask import Flask, abort, jsonify
from flask_admin.contrib.sqla import ModelView

from bio2bel_homologene.manager import Manager
from bio2bel_homologene.models import *

app = Flask(__name__)
admin = flask_admin.Admin(app, url='/')

manager = Manager()

admin.add_view(ModelView(Homologene, manager.session))
admin.add_view(ModelView(Gene, manager.session))
admin.add_view(ModelView(Species, manager.session))


@app.route('/api/species/<tax_id>')
def get_species_genes(tax_id):
    """Gets genes from this taxonomy id"""
    species = manager.session.query(Species).filter(Species.taxonomy_id == tax_id).one_or_none()
    if species is None:
        abort(404, 'Species {} not found'.format(tax_id))

    return jsonify([
        {
            'entrez_id': gene.gene_id,
            'symbol': gene.gene_symbol
        }
        for gene in species.genes
    ])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
