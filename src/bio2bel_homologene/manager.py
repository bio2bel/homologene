# -*- coding: utf-8 -*-

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from bio2bel.utils import get_connection
from bio2bel_homologene.models import Base, Gene, Homologene, Species
from bio2bel_homologene.parser import download_homologene
from .constants import MODULE_NAME

log = logging.getLogger(__name__)


class Manager(object):
    """Manages the HomoloGene database"""

    def __init__(self, connection=None):
        """
        :param Optional[str] connection: The connection string
        """
        self.connection = get_connection(MODULE_NAME, connection=connection)
        log.info('connected to %s', self.connection)
        self.engine = create_engine(self.connection)
        self.session_maker = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.session = self.session_maker()
        self.create_all()

        #: a cache from group id to its model
        self.group_cache = {}
        #: a cache from (tax id, gene id) to its model
        self.gene_cache = {}

        #: a cache from NCBI tax id to its model
        self.species_cache = {}

    def create_all(self, check_first=True):
        """Create tables"""
        Base.metadata.create_all(self.engine, checkfirst=check_first)

    def drop_all(self, check_first=True):
        """Create tables"""
        log.info('dropping tables')
        Base.metadata.drop_all(self.engine, checkfirst=check_first)

    def populate(self, url=None):
        """Populates the database

        :param Optional[str] url:
        """
        log.info('downloading data')
        df = download_homologene(url=url)

        log.info('preparing models')
        for _, (hid, tax_id, gene_id, gene_symbol, _, _) in tqdm(df.iterrows(), total=len(df.index)):
            if hid in self.group_cache:
                group = self.group_cache[hid]
            else:
                group = Homologene(homologene_id=hid)
                self.group_cache[hid] = group
                self.session.add(group)

            if tax_id in self.species_cache:
                species = self.species_cache[tax_id]
            else:
                species = Species(taxonomy_id=tax_id)
                self.species_cache[tax_id] = species
                self.session.add(species)

            if gene_id in self.gene_cache:
                gene = self.gene_cache[tax_id, gene_id]
                log.warning('second group for %s (%s)', gene_symbol, gene_id)
            else:
                gene = Gene(species=species, gene_id=gene_id, gene_symbol=gene_symbol)
                self.gene_cache[tax_id, gene_id] = gene
                self.session.add(gene)

            gene.homologene = group

        log.info('committing models')
        self.session.commit()


if __name__ == '__main__':
    logging.basicConfig(level=20, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
    log.setLevel(20)
    m = Manager()
    m.drop_all()
    m.create_all()
    m.populate(url='/Users/cthoyt/Downloads/homologene.data.txt')
