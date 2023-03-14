from dataclasses import asdict, dataclass
from pprint import pprint
from typing import Optional

import rlp
from eth_typing import HexStr
from eth_utils import keccak, to_bytes
from rlp.sedes import Binary, big_endian_int, binary
from web3 import Web3
from web3.auto import w3


class Transaction(rlp.Serializable):
    fields = [
        ("nonce", big_endian_int),
        ("gasPrice", big_endian_int),
        ("gatewayFee", big_endian_int),
        ("gas", big_endian_int),
        ("to", Binary.fixed_length(20, allow_empty=True)),
        ("gatewayFeeRecipient", Binary.fixed_length(20, allow_empty=True)),
        ("feeCurrency", Binary.fixed_length(20, allow_empty=True)),
        ("value", big_endian_int),
        ("data", binary),
        ("v", big_endian_int),
        ("r", big_endian_int),
        ("s", big_endian_int),
    ]


@dataclass
class DecodedTx:
    hash_tx: str
    gatewayFee: int
    gatewayFeeRecipient: str
    feeCurrency: str
    from_: str
    to: Optional[str]
    nonce: int
    gas: int
    gasPrice: int
    value: int
    data: str
    chainId: int
    r: str
    s: str
    v: int


def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))


def decode_raw_tx(raw_tx: str):
    tx = rlp.decode(hex_to_bytes(raw_tx), Transaction)
    hash_tx = Web3.toHex(keccak(hex_to_bytes(raw_tx)))
    from_ = w3.eth.account.recover_transaction(raw_tx)
    to = w3.toChecksumAddress(tx.to) if tx.to else None
    data = w3.toHex(tx.data)
    r = hex(tx.r)
    s = hex(tx.s)
    chain_id = (tx.v - 35) // 2 if tx.v % 2 else (tx.v - 36) // 2
    return DecodedTx(hash_tx, tx.gatewayFee, tx.gatewayFeeRecipient, tx.feeCurrency.hex(), from_, to, tx.nonce, tx.gas, tx.gasPrice, tx.value, data, chain_id, r, s, tx.v)


def main():
    raw_tx = "0xf8c4018504a817c800830285ec94874069fa1eb16d44d622f2e0ca25eea172369bc1808094874069fa1eb16d44d622f2e0ca25eea172369bc180b844a9059cbb000000000000000000000000485ef2673beabd920360536872c911661a56dc02000000000000000000000000000000000000000000000000002386f26fc1000083015e0aa074e7a1405442f380827b7f909b76ad80357ccb81081a1bb35e4526d7e6f6c10ca07be8cc184bc3d1d0ce418e47c6977243f0790502deaf79ef4de3174cdc6503d9"  # noqa
    res = decode_raw_tx(raw_tx)
    pprint(asdict(res))


if __name__ == "__main__":
    main()
