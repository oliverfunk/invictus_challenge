from typing import List
from nameko.rpc import rpc

class InvictusTestService:
    name = "invt_service"

    @rpc
    def square_odds(self, in_list: List) -> List:
        return list(map(lambda n: n if n%2 == 0 else n**2, in_list))