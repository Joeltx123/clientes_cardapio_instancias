import pyotp
import os
import sys
import json

# Sua chave secreta do Google Authenticator já configurada
SEGREDO_TOTP = "JBSWY3DPEHPK3PXP"  # Substitua caso queira usar outra chave do seu app
ARQUIVO_ESTADO = ".status_cofre"

def verificar_2fa():
    print("🔒 [ÁREA RESTRITA] Protegido por Google Authenticator.")
    codigo = input("📱 Digite o código de 6 dígitos do seu Authenticator: ").strip()
    totp = pyotp.TOTP(SEGREDO_TOTP)
    return totp.verify(codigo)

def destravar():
    if verificar_2fa():
        with open(ARQUIVO_ESTADO, "w") as f:
            f.write("liberado")
        print("✅ Projeto DESTRAVADO com sucesso! Pode editar, ler e mexer à vontade.")
    else:
        print("❌ Código incorreto! Acesso negado.")
        sys.exit(1)

def trancar():
    if os.path.exists(ARQUIVO_ESTADO):
        os.remove(ARQUIVO_ESTADO)
    print("🔒 Projeto TRANCADO com segurança! Ninguém poderá mexer ou ler sem o Authenticator.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        if comando == "destravar":
            destravar()
        elif comando == "trancar":
            trancar()
    else:
        # Se tentar rodar sem comando, verifica se está trancado
        if not os.path.exists(ARQUIVO_ESTADO):
            print("🛑 BLOQUEADO! Este projeto está trancado.")
            destravar()
