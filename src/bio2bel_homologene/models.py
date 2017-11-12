# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

TABLE_PREFIX = 'homologene'
GROUP_TABLE_NAME = '{}_homologene'.format(TABLE_PREFIX)
GENE_TABLE_NAME = '{}_gene'.format(TABLE_PREFIX)
SPECIES_TABLE_NAME = '{}_species'.format(TABLE_PREFIX)

Base = declarative_base()


class Homologene(Base):
    """Represents a HomoloGene Group"""
    __tablename__ = GROUP_TABLE_NAME

    id = Column(Integer, primary_key=True)

    homologene_id = Column(String(255), index=True, unique=True, nullable=False)

    def __str__(self):
        return self.homologene_id


class Gene(Base):
    """Represents a Gene"""
    __tablename__ = GENE_TABLE_NAME

    id = Column(Integer, primary_key=True)

    gene_id = Column(String(255), index=True, unique=True, nullable=False, doc='Entrez Gene Identifier')
    gene_symbol = Column(String(255), doc='Entrez Gene Symbol')

    species_id = Column(Integer, ForeignKey('{}.id'.format(SPECIES_TABLE_NAME)))
    species = relationship('Species', backref=backref('genes'))

    homologene_id = Column(Integer, ForeignKey('{}.id'.format(GROUP_TABLE_NAME)))
    homologene = relationship('Homologene', backref=backref('genes'))

    def __str__(self):
        return self.gene_id


class Species(Base):
    """Representes a Species"""
    __tablename__ = SPECIES_TABLE_NAME

    id = Column(Integer, primary_key=True)

    taxonomy_id = Column(String(255), index=True, unique=True, nullable=False, doc='NCBI Taxonomy Identifier')

    def __str__(self):
        return self.taxonomy_id
