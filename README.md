# CELO Transaction Decoder


This Python code provides a transaction decoder for Celo blockchain transactions. It allows you to decode raw transactions and extract relevant information from them, such as the transaction hash, sender address, recipient address, amount transferred, gas price, and more.

# Usage

## Requirements
To run this code, you need to have Python 3.6 or higher and the following Python packages installed:

web3.py (install using pip: pip install web3)
eth-utils (install using pip: pip install eth-utils)
eth-typing (install using pip: pip install eth-typing)
RLP (install using pip: pip install rlp)
Running the Code
To use this transaction decoder, you need to call the decode_raw_tx function and pass it a raw transaction string in hexadecimal format. The function will return a DecodedTx object with the decoded transaction information.

```python
def decode_raw_tx(raw_tx: str) -> DecodedTx:
    """
    Decodes a raw transaction string (in hexadecimal format) and returns a DecodedTx object.
    """
You can use the pprint function from the pprint library to print the decoded transaction information in a readable format. Here is an example usage:
```

```python
from pprint import pprint

raw_tx = "0xf8c4018504a817c800830285ec94874069fa1eb16d44d622f2e0ca25eea172369bc1808094874069fa1eb16d44d622f2e0ca25eea172369bc180b844a9059cbb000000000000000000000000485ef2673beabd920360536872c911661a56dc02000000000000000000000000000000000000000000000000002386f26fc1000083015e0aa074e7a1405442f380827b7f909b76ad80357ccb81081a1bb35e4526d7e6f6c10ca07be8cc184bc3d1d0ce418e47c6977243f0790502deaf79ef4de3174cdc6503d9"  # noqa

decoded_tx = decode_raw_tx(raw_tx)
pprint(decoded_tx)
```

Conclusion

This Python code provides a convenient way to decode Celo blockchain transactions and extract relevant information from them. You can use it to analyze transactions on the Celo blockchain and build tools to interact with the Celo network.
