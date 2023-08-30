debug = False

import requests
from mnemonic import Mnemonic
from bip32utils import BIP32Key
from eth_keys import keys
from eth_utils import to_checksum_address

# Warunkowy import var_dump
if debug:
    from var_dump import var_dump

# Podziel mnemonic na dwie części, pamiętaj o spacji na końcu prefixu bądź początku sufixu
prefix_mnemonic = "liberty river current obey box soldier now gather dismiss penalty subway "
suffix_mnemonic = ""

# Lista 2048 słów BIP-39
wordlist = Mnemonic("english").wordlist

# Stała dla kluczy utwardzonych
HARDENED = 0x80000000

# Klucz API dla polygonscan.com; get free one at https://polygonscan.com/myapikey
API_KEY = ""

# Znajdź brakujące słowo mnemonika
for word in wordlist:
    try:
        mnemonic = prefix_mnemonic + word + suffix_mnemonic
        if debug:
            var_dump(mnemonic)
        if Mnemonic("english").check(mnemonic):
            print(f"Znaleziono pasujące 12. słowo: {word}")
            
            # Generuj klucz prywatny i adres Ethereum zgodnie z BIP-44
            seed = Mnemonic.to_seed(mnemonic)
            root_key = BIP32Key.fromEntropy(seed)
            child_key = root_key.ChildKey(44 + HARDENED).ChildKey(60 + HARDENED).ChildKey(0 + HARDENED).ChildKey(0).ChildKey(0)
            private_key_bytes = child_key.PrivateKey()
            private_key = keys.PrivateKey(private_key_bytes)
            address = to_checksum_address(private_key.public_key.to_address())

            print(f"Adres Ethereum: {address}")
            
            # Sprawdź stan konta na polygonscan.com
            response = requests.get(f"https://api.polygonscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey={API_KEY}")
            balance = response.json().get("result", "0")
            print(f"Stan konta: {int(balance) / 10**18} MATIC")
            
            # Sprawdź tokeny ERC-20
            response = requests.get(f"https://api.polygonscan.com/api?module=account&action=tokentx&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}")
            erc20_tokens = response.json().get("result", [])
            if erc20_tokens:
                print("Tokeny ERC-20:")
                for token in erc20_tokens:
                    print(f"Token: {token['tokenName']}, Symbol: {token['tokenSymbol']}, Ilość: {int(token['value']) / 10**int(token['tokenDecimal'])}")
            else:
                print("Brak tokenów ERC-20.")
            
            # Sprawdź tokeny ERC-721
            response = requests.get(f"https://api.polygonscan.com/api?module=account&action=tokennfttx&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}")
            erc721_tokens = response.json().get("result", [])
            if erc721_tokens:
                print("Tokeny ERC-721:")
                for token in erc721_tokens:
                    print(f"Token: {token['tokenName']}, Symbol: {token['tokenSymbol']}, Token ID: {token['tokenID']}")
            else:
                print("Brak tokenów ERC-721.")

            # Sprawdź tokeny ERC-1155
            response = requests.get(f"https://api.polygonscan.com/api?module=account&action=token1155tx&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={API_KEY}")
            erc1155_tokens = response.json().get("result", [])
            if erc1155_tokens:
                print("Tokeny ERC-1155:")
                for token in erc1155_tokens:
                    token_value = token.get('value', 'Nieznana ilość')  # Używamy metody get() z wartością domyślną
                    print(f"Token: {token['tokenName']}, Symbol: {token['tokenSymbol']}, Token ID: {token['tokenID']}, Ilość: {token_value}")
            else:
                print("Brak tokenów ERC-1155.")
    except requests.RequestException as e:
        print(f"Błąd podczas łączenia się z API: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
