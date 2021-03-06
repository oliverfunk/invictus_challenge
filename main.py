from typing import Dict, List
import zlib
from nameko.rpc import rpc


class InvictusNamekoService:
    name = "inv_nameko_service"

    '''
    Compress a given string using zlib and return the result in a hex format.
    Encoding it as hex makes it easeier to display or transmit.
    '''
    def compress_string(self, str_to_comp: str) -> str:
        return zlib.compress(str_to_comp.encode('utf-8'), level=-1).hex()

    '''
    Decompress a previously compressed string in its hex format using zlib.
    '''
    def decompress_data(self, compressed_hex_data: str) -> str:
        return zlib.decompress(bytearray.fromhex(compressed_hex_data)).decode('utf-8')

    @rpc
    def square_odds(self, in_list: List[int]) -> List[int]:
        return list(map(lambda n: n if n % 2 == 0 else n**2, in_list))

    @rpc
    def compress_list_map(self, in_list: List[str]) -> Dict[str, str]:
        return dict(zip(in_list, map(self.compress_string, in_list)))

    @rpc
    def decompress_string(self, in_hex_str: str) -> str:
        return self.decompress_data(in_hex_str)
