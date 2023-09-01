import secrets


class Valid_Data:
    TourInputSecretTokenHex16 = secrets.token_hex(16)  # Генерирует 32 символа (16 байт в шестнадцатеричном формате)
    TourInputSecretTokenHex32 = secrets.token_hex(32)

    TourInputSecretTokenHex12 = secrets.token_hex(12)
    TourInputSecretTokenHex4 = secrets.token_hex(4)


class MassHex:
    HEX = [
        secrets.token_hex(16),
        secrets.token_hex(32)
    ]
