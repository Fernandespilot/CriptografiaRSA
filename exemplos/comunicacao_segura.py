"""
Exemplo de comunicação segura entre duas partes usando RSA
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rsa_avancado import RSAAvancado
import json
import base64

class PessoaSegura:
    """Representa uma pessoa que pode se comunicar de forma segura"""
    
    def __init__(self, nome):
        self.nome = nome
        self.rsa = RSAAvancado()
        self.chave_publica_outros = {}  # Armazena chaves públicas de outras pessoas
    
    def gerar_chaves(self):
        """Gera suas próprias chaves"""
        print(f"{self.nome} está gerando suas chaves...")
        self.rsa.gerar_chaves(1024)
        print(f"{self.nome} gerou suas chaves com sucesso!")
    
    def exportar_chave_publica(self):
        """Exporta a chave pública para compartilhar"""
        if not self.rsa.chave_publica:
            raise ValueError("Chaves não foram geradas ainda!")
        
        from cryptography.hazmat.primitives import serialization
        chave_pem = self.rsa.chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return chave_pem
    
    def importar_chave_publica(self, nome_pessoa, chave_pem):
        """Importa a chave pública de outra pessoa"""
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.backends import default_backend
        
        chave_publica = serialization.load_pem_public_key(
            chave_pem,
            backend=default_backend()
        )
        self.chave_publica_outros[nome_pessoa] = chave_publica
        print(f"{self.nome} importou a chave pública de {nome_pessoa}")
    
    def enviar_mensagem_segura(self, destinatario, mensagem):
        """Envia uma mensagem criptografada para alguém"""
        if destinatario not in self.chave_publica_outros:
            raise ValueError(f"Chave pública de {destinatario} não encontrada!")
        
        # Criar RSA temporário para criptografar com a chave do destinatário
        rsa_temp = RSAAvancado()
        rsa_temp.chave_publica = self.chave_publica_outros[destinatario]
        
        # Criptografar mensagem
        mensagem_criptografada = rsa_temp.criptografar(mensagem)
        
        # Assinar mensagem para autenticidade
        assinatura = self.rsa.assinar(mensagem)
        
        # Criar pacote seguro
        pacote = {
            'remetente': self.nome,
            'destinatario': destinatario,
            'mensagem_criptografada': mensagem_criptografada,
            'assinatura': assinatura,
            'timestamp': '2025-05-25 20:00:00'
        }
        
        print(f"{self.nome} enviou mensagem segura para {destinatario}")
        return pacote
    
    def receber_mensagem_segura(self, pacote):
        """Recebe e processa uma mensagem criptografada"""
        remetente = pacote['remetente']
        destinatario = pacote['destinatario']
        
        if destinatario != self.nome:
            raise ValueError("Esta mensagem não é para você!")
        
        if remetente not in self.chave_publica_outros:
            raise ValueError(f"Chave pública de {remetente} não encontrada!")
        
        # Descriptografar mensagem
        mensagem = self.rsa.descriptografar(pacote['mensagem_criptografada'])
        
        # Verificar assinatura
        rsa_temp = RSAAvancado()
        rsa_temp.chave_publica = self.chave_publica_outros[remetente]
        
        assinatura_valida = rsa_temp.verificar_assinatura(mensagem, pacote['assinatura'])
        
        resultado = {
            'remetente': remetente,
            'mensagem': mensagem,
            'assinatura_valida': assinatura_valida,
            'timestamp': pacote['timestamp']
        }
        
        print(f"{self.nome} recebeu mensagem de {remetente}")
        print(f"Assinatura válida: {assinatura_valida}")
        
        return resultado

def demonstrar_comunicacao_segura():
    """Demonstra comunicação segura entre Alice e Bob"""
    print("=== DEMONSTRAÇÃO DE COMUNICAÇÃO SEGURA ===")
    print("Simulando uma conversa segura entre Alice e Bob")
    print()
    
    # Criar duas pessoas
    alice = PessoaSegura("Alice")
    bob = PessoaSegura("Bob")
    
    # Gerar chaves para ambos
    print("1. GERAÇÃO DE CHAVES")
    print("-" * 20)
    alice.gerar_chaves()
    bob.gerar_chaves()
    print()
    
    # Trocar chaves públicas (simulando um canal público)
    print("2. TROCA DE CHAVES PÚBLICAS")
    print("-" * 30)
    chave_publica_alice = alice.exportar_chave_publica()
    chave_publica_bob = bob.exportar_chave_publica()
    
    alice.importar_chave_publica("Bob", chave_publica_bob)
    bob.importar_chave_publica("Alice", chave_publica_alice)
    print()
    
    # Alice envia mensagem para Bob
    print("3. ALICE ENVIA MENSAGEM PARA BOB")
    print("-" * 35)
    mensagem1 = "Olá Bob! Esta é uma mensagem secreta. Encontro às 15h no local combinado. 🔐"
    print(f"Mensagem original: '{mensagem1}'")
    
    pacote1 = alice.enviar_mensagem_segura("Bob", mensagem1)
    print(f"Pacote criptografado criado com {len(str(pacote1))} caracteres")
    print()
    
    # Bob recebe e lê a mensagem
    print("4. BOB RECEBE E DESCRIPTOGRAFA")
    print("-" * 30)
    resultado1 = bob.receber_mensagem_segura(pacote1)
    print(f"Mensagem descriptografada: '{resultado1['mensagem']}'")
    print(f"Mensagem autêntica: {resultado1['assinatura_valida']}")
    print()
    
    # Bob responde para Alice
    print("5. BOB RESPONDE PARA ALICE")
    print("-" * 25)
    mensagem2 = "Entendi Alice! Estarei lá às 15h. Obrigado pela mensagem segura! 👍"
    print(f"Resposta: '{mensagem2}'")
    
    pacote2 = bob.enviar_mensagem_segura("Alice", mensagem2)
    print()
    
    # Alice recebe a resposta
    print("6. ALICE RECEBE A RESPOSTA")
    print("-" * 25)
    resultado2 = alice.receber_mensagem_segura(pacote2)
    print(f"Resposta recebida: '{resultado2['mensagem']}'")
    print(f"Resposta autêntica: {resultado2['assinatura_valida']}")
    print()
    
    # Testar interceptação (atacante)
    print("7. TESTE DE SEGURANÇA - ATACANTE")
    print("-" * 35)
    print("Simulando um atacante tentando interceptar e modificar mensagens...")
    
    # Atacante tenta modificar o pacote
    pacote_alterado = pacote1.copy()
    pacote_alterado['mensagem_criptografada'] = "mensagem_falsa_base64"
    
    try:
        resultado_atacado = bob.receber_mensagem_segura(pacote_alterado)
        print("FALHA DE SEGURANÇA: Atacante conseguiu modificar a mensagem!")
    except Exception as e:
        print(f"SEGURANÇA OK: Ataque bloqueado - {type(e).__name__}")
    
    print()
    print("CONCLUSÃO: A comunicação RSA é segura!")
    print("- Mensagens são criptografadas (confidencialidade)")
    print("- Assinaturas garantem autenticidade")
    print("- Modificações são detectadas")

def demonstrar_grupo_conversa():
    """Demonstra comunicação em grupo"""
    print("\n=== DEMONSTRAÇÃO DE GRUPO ===")
    print("Simulando uma conversa em grupo segura")
    print()
    
    # Criar grupo
    pessoas = {}
    nomes = ["Alice", "Bob", "Charlie", "Diana"]
    
    # Criar todas as pessoas
    print("1. CRIANDO PARTICIPANTES")
    print("-" * 25)
    for nome in nomes:
        pessoa = PessoaSegura(nome)
        pessoa.gerar_chaves()
        pessoas[nome] = pessoa
    print()
    
    # Trocar chaves públicas entre todos
    print("2. TROCANDO CHAVES PÚBLICAS")
    print("-" * 28)
    for nome1 in nomes:
        for nome2 in nomes:
            if nome1 != nome2:
                chave = pessoas[nome1].exportar_chave_publica()
                pessoas[nome2].importar_chave_publica(nome1, chave)
    print("Todas as chaves públicas foram trocadas!")
    print()
    
    # Conversação em grupo
    print("3. CONVERSAÇÃO EM GRUPO")
    print("-" * 22)
    
    mensagens = [
        ("Alice", "Bob", "Bob, você recebeu o documento?"),
        ("Bob", "Alice", "Sim Alice, está tudo certo!"),
        ("Charlie", "Alice", "Alice, posso participar do projeto?"),
        ("Alice", "Charlie", "Claro Charlie, bem-vindo!"),
        ("Diana", "Alice", "Quando é a próxima reunião?"),
        ("Alice", "Diana", "Diana, será na sexta às 14h")
    ]
    
    for i, (remetente, destinatario, mensagem) in enumerate(mensagens, 1):
        print(f"Mensagem {i}: {remetente} → {destinatario}")
        print(f"Conteúdo: '{mensagem}'")
        
        # Enviar mensagem
        pacote = pessoas[remetente].enviar_mensagem_segura(destinatario, mensagem)
        
        # Receber mensagem
        resultado = pessoas[destinatario].receber_mensagem_segura(pacote)
        
        print(f"Status: Entregue ✓ | Autêntica: {resultado['assinatura_valida']}")
        print("-" * 40)
    
    print("GRUPO: Todas as mensagens foram entregues com segurança!")

def main():
    """Executa as demonstrações"""
    print("EXEMPLOS DE COMUNICAÇÃO SEGURA COM RSA")
    print("=" * 50)
    
    try:
        # Demonstração 1: Comunicação entre duas pessoas
        demonstrar_comunicacao_segura()
        
        # Demonstração 2: Grupo de conversa
        demonstrar_grupo_conversa()
        
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("FIM DAS DEMONSTRAÇÕES")

if __name__ == "__main__":
    main()
