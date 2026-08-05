import pyotp
import os

# Chave secreta exclusiva do seu autenticador (você pode gerar uma nova ou guardar esta)
# Para gerar o qrcode no terminal para ler no app do celular, execute: python3 -c "import pyotp; print(pyotp.random_base32())"
SEGREDO_TOTP = os.getenv("CHAVE_AUTENTICADOR", "JBSWY3DPEHPK3PXP") # Substitua pela sua chave secreta gerada

def verificar_codigo(codigo_digitado):
    totp = pyotp.TOTP(SEGREDO_TOTP)
    return totp.verify(codigo_digitado)
