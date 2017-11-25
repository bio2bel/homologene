# -*- coding: utf-8 -*-

from bio2bel.utils import get_connection, get_data_dir

MODULE_NAME = 'homologene'
DATA_DIR = get_data_dir(MODULE_NAME)
DEFAULT_CACHE_CONNECTION = get_connection(MODULE_NAME)

HOMOLOGENE_BUILD_URL = 'ftp://ftp.ncbi.nih.gov/pub/HomoloGene/current/RELEASE_NUMBER'
HOMOLOGENE_URL = 'ftp://ftp.ncbi.nih.gov/pub/HomoloGene/current/homologene.data'
