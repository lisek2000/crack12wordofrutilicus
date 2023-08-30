# Ethereum Mnemonic Recovery Tool

## Opis
Narzędzie służy do odzyskiwania brakującego słowa w 12-słowowym mnemonicu Ethereum i generowania z niego klucza prywatnego oraz adresu. Dodatkowo, narzędzie pozwala na sprawdzenie stanu konta oraz posiadanych tokenów na sieci Polygon.

## Wymagania
- Python 3.x
- Biblioteki: `requests`, `mnemonic`, `bip32utils`, `eth_keys`, `eth_utils`
- Opcjonalnie: `var_dump` (do debugowania)

## Instalacja
1. Sklonuj repozytorium:
git clone git@github.com/crack12wordofrutilicus.git


2. Zainstaluj wymagane biblioteki:
```python
pip install requests mnemonic bip32utils eth_keys eth_utils
```

## Użycie
1. Ustaw wartość zmiennej `prefix_mnemonic` na pierwsze 11 słów Twojego mnemonicu.
2. Uruchom skrypt:
```bash
python main.py
```

## Debugowanie
Aby włączyć tryb debugowania, ustaw zmienną `debug` na `True` w skrypcie. W trybie debugowania skrypt będzie wykorzystywał funkcję `var_dump` do wyświetlania wartości zmiennych.

## Licencja
Ten projekt jest udostępniany na licencji MIT. Me it you, amć, amć, amć, delicious you.

## Autor
k0lo2077 at Discord
Discord User ID: 491543734006185988
