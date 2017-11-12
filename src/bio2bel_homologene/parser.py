# -*- coding: utf-8 -*-

"""
1) HID (HomoloGene group id)
2) Taxonomy ID
3) Gene ID
4) Gene Symbol
5) Protein gi
6) Protein accession
"""

import pandas as pd

from bio2bel_homologene.constants import HOMOLOGENE_URL

header = [
    'homologene_id',
    'tax_id',
    'gene_id',
    'gene_symbol',
    'protein_gi',
    'protein_accession'
]


def download_homologene(url=None):
    """

    :param Optional[str] url: A custom URL to download
    :rtype: pandas.Datarame
    """
    df = pd.read_csv(
        url or HOMOLOGENE_URL,
        sep='\t',
        names=header
    )
    return df
