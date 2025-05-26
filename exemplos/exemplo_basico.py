"""
Exemplo 1: Criptografia básica de mensagens
"""

import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rsa_basico import RSABasico
from rsa_avancado import RSAAvancado

def exemplo_rsa_basico():
    """Demonstra o uso do RSA básico"""
    print("=== EXEMPLO RSA BÁSICO ===")
    print("Este exemplo mostra como usar a implementação básica do RSA")
    print()
    
    # Criar instância
    rsa = RSABasico()
    
    # Gerar chaves pequenas para demonstração
    print("1. Gerando chaves RSA (implementação básica)...")
    chave_publica, chave_privada = rsa.gerar_chaves(bits=12)
    print()
    
    # Testar com diferentes tipos de mensagens
    mensagens_teste = [
        "OI",
        "RSA",
        "123",
        "HELLO"
    ]
    
    print("2. Testando criptografia com diferentes mensagens:")
    print("-" * 50)
    
    for mensagem in mensagens_teste:
        try:
            print(f"Mensagem original: '{mensagem}'")
            
            # Criptografar
            criptografada = rsa.criptografar(mensagem)
            print(f"Criptografada: {criptografada}")
            
            # Descriptografar
            descriptografada = rsa.descriptografar(criptografada)
            print(f"Descriptografada: '{descriptografada}'")
            
            # Verificar se funcionou
            sucesso = mensagem == descriptografada
            print(f"Sucesso: {sucesso}")
            print("-" * 30)
            
        except Exception as e:
            print(f"Erro com mensagem '{mensagem}': {e}")
            print("-" * 30)

def exemplo_rsa_avancado():
    """Demonstra o uso do RSA avançado"""
    print("\n=== EXEMPLO RSA AVANÇADO ===")
    print("Este exemplo mostra como usar a implementação avançada do RSA")
    print()
    
    # Criar instância
    rsa = RSAAvancado()
    
    # Gerar chaves
    print("1. Gerando chaves RSA (implementação avançada)...")
    rsa.gerar_chaves(1024)  # Usar 1024 para ser mais rápido no exemplo
    print()
    
    # Mensagens de teste
    mensagens_teste = [
        "Esta é uma mensagem secreta!",
        "RSA funciona muito bem 🔐",
        "Dados confidenciais: senha123",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    ]
    
    print("2. Testando criptografia avançada:")
    print("-" * 40)
    
    for i, mensagem in enumerate(mensagens_teste, 1):
        try:
            print(f"Teste {i}: '{mensagem[:30]}{'...' if len(mensagem) > 30 else ''}'")
            
            # Criptografar
            criptografada = rsa.criptografar(mensagem)
            print(f"Criptografada (primeiros 50 chars): {criptografada[:50]}...")
            
            # Descriptografar
            descriptografada = rsa.descriptografar(criptografada)
            print(f"Descriptografada: '{descriptografada}'")
            
            # Verificar
            sucesso = mensagem == descriptografada
            print(f"Sucesso: {sucesso}")
            print("-" * 30)
            
        except Exception as e:
            print(f"Erro: {e}")
            print("-" * 30)

def exemplo_assinatura_digital():
    """Demonstra assinatura digital"""
    print("\n=== EXEMPLO ASSINATURA DIGITAL ===")
    print("Este exemplo mostra como usar assinatura digital")
    print()
    
    # Criar instância
    rsa = RSAAvancado()
    rsa.gerar_chaves(1024)
    
    # Documento para assinar
    documento = """
    CONTRATO DE COMPRA E VENDA
    
    Vendedor: João Silva
    Comprador: Maria Santos
    Produto: Notebook Dell
    Valor: R$ 2.500,00
    Data: 25/05/2025
    """
    
    print("1. Documento original:")
    print(documento)
    
    # Assinar documento
    print("2. Gerando assinatura digital...")
    assinatura = rsa.assinar(documento)
    print(f"Assinatura (primeiros 50 chars): {assinatura[:50]}...")
    print()
    
    # Verificar assinatura válida
    print("3. Verificando assinatura do documento original:")
    valida = rsa.verificar_assinatura(documento, assinatura)
    print(f"Assinatura válida: {valida}")
    print()
    
    # Testar com documento alterado
    print("4. Verificando assinatura com documento alterado:")
    documento_alterado = documento.replace("R$ 2.500,00", "R$ 25.000,00")
    valida_alterado = rsa.verificar_assinatura(documento_alterado, assinatura)
    print(f"Assinatura válida para documento alterado: {valida_alterado}")
    print()
    
    print("Conclusão: A assinatura digital detecta alterações no documento!")

def main():
    """Executa todos os exemplos"""
    print("EXEMPLOS DE CRIPTOGRAFIA RSA")
    print("=" * 50)
    print()
    
    try:
        # Exemplo 1: RSA Básico
        exemplo_rsa_basico()
        
        # Exemplo 2: RSA Avançado
        exemplo_rsa_avancado()
        
        # Exemplo 3: Assinatura Digital
        exemplo_assinatura_digital()
        
    except ImportError as e:
        print(f"Erro de importação: {e}")
        print("Certifique-se de que as dependências estão instaladas:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    print("\n" + "=" * 50)
    print("FIM DOS EXEMPLOS")

if __name__ == "__main__":
    main()
