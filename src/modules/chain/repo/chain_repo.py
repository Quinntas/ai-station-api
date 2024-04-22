from src.core.base_repo import BaseRepo
from src.modules.chain.domain.chain import ChainModel
from src.modules.chain.mapper.chain_mapper import chain_mapper


class ChainRepo(BaseRepo):
    def __init__(self):
        super().__init__(ChainModel, chain_mapper)


chain_repo = ChainRepo()
