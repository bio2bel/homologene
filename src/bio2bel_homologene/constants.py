# -*- coding: utf-8 -*-

import os

MODULE_NAME = 'homologene'
BIO2BEL_DIR = os.environ.get('BIO2BEL_DIRECTORY', os.path.join(os.path.expanduser('~'), '.pybel', 'bio2bel'))
DATA_DIR = os.path.join(BIO2BEL_DIR, MODULE_NAME)
os.makedirs(DATA_DIR, exist_ok=True)

DEFAULT_CACHE_NAME = '{}.db'.format(MODULE_NAME)
DEFAULT_CACHE_PATH = os.path.join(DATA_DIR, DEFAULT_CACHE_NAME)
DEFAULT_CACHE_CONNECTION = os.environ.get('BIO2BEL_CONNECTION', 'sqlite:///' + DEFAULT_CACHE_PATH)

HOMOLOGENE_BUILD_URL = 'ftp://ftp.ncbi.nih.gov/pub/HomoloGene/current/RELEASE_NUMBER'
HOMOLOGENE_URL = 'ftp://ftp.ncbi.nih.gov/pub/HomoloGene/current/homologene.data'