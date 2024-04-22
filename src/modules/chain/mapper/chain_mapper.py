from src.core.base_mapper import BaseMapper
from src.modules.chain.domain.chain import ChainModel, ChainDomain


class ChainMapper(BaseMapper):
    def __init__(self):
        super().__init__(ChainModel, ChainDomain)

    def to_public_domain(self):
        pass


chain_mapper = ChainMapper()
