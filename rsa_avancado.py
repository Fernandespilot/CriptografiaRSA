from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64
import os

class RSAAvancado:
    """
    Implementação avançada do RSA usando a biblioteca cryptography
    para uso em produção com recursos de segurança aprimorados.
    """
    
    def __init__(self):
        self.chave_privada = None
        self.chave_publica = None
    
    def gerar_chaves(self, tamanho_chave=2048):
        """
        Gera um par de chaves RSA usando biblioteca criptográfica segura
        
        Args:
            tamanho_chave: Tamanho da chave em bits (padrão: 2048)
        
        Returns:
            tuple: (chave_privada_pem, chave_publica_pem)
        """
        print(f"Gerando chaves RSA de {tamanho_chave} bits...")
        
        # Gerar chave privada
        self.chave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=tamanho_chave,
            backend=default_backend()
        )
        
        # Extrair chave pública
        self.chave_publica = self.chave_privada.public_key()
        
        # Serializar chaves para formato PEM
        chave_privada_pem = self.chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        chave_publica_pem = self.chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        print("Chaves geradas com sucesso!")
        return chave_privada_pem, chave_publica_pem
    
    def salvar_chaves(self, nome_arquivo="rsa_key"):
        """
        Salva as chaves em arquivos
        
        Args:
            nome_arquivo: Nome base dos arquivos (sem extensão)
        """
        if not self.chave_privada or not self.chave_publica:
            raise ValueError("Chaves não foram geradas ainda!")
        
        # Salvar chave privada
        chave_privada_pem = self.chave_privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        with open(f"{nome_arquivo}_private.pem", "wb") as f:
            f.write(chave_privada_pem)
        
        # Salvar chave pública
        chave_publica_pem = self.chave_publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        with open(f"{nome_arquivo}_public.pem", "wb") as f:
            f.write(chave_publica_pem)
        
        print(f"Chaves salvas como {nome_arquivo}_private.pem e {nome_arquivo}_public.pem")
    
    def carregar_chave_privada(self, caminho_arquivo):
        """Carrega chave privada de um arquivo"""
        with open(caminho_arquivo, "rb") as f:
            self.chave_privada = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        self.chave_publica = self.chave_privada.public_key()
        print(f"Chave privada carregada de {caminho_arquivo}")
    
    def carregar_chave_publica(self, caminho_arquivo):
        """Carrega chave pública de um arquivo"""
        with open(caminho_arquivo, "rb") as f:
            self.chave_publica = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )
        print(f"Chave pública carregada de {caminho_arquivo}")
    
    def criptografar(self, mensagem, usar_base64=True):
        """
        Criptografa uma mensagem usando OAEP padding
        
        Args:
            mensagem: String a ser criptografada
            usar_base64: Se True, retorna resultado em base64
        
        Returns:
            bytes ou str: Mensagem criptografada
        """
        if not self.chave_publica:
            raise ValueError("Chave pública não foi carregada!")
        
        if isinstance(mensagem, str):
            mensagem = mensagem.encode('utf-8')
        
        # Criptografar usando OAEP padding
        mensagem_criptografada = self.chave_publica.encrypt(
            mensagem,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        if usar_base64:
            return base64.b64encode(mensagem_criptografada).decode('utf-8')
        else:
            return mensagem_criptografada
    
    def descriptografar(self, mensagem_criptografada, eh_base64=True):
        """
        Descriptografa uma mensagem
        
        Args:
            mensagem_criptografada: Mensagem criptografada
            eh_base64: Se True, espera entrada em base64
        
        Returns:
            str: Mensagem descriptografada
        """
        if not self.chave_privada:
            raise ValueError("Chave privada não foi carregada!")
        
        if eh_base64:
            if isinstance(mensagem_criptografada, str):
                mensagem_criptografada = base64.b64decode(mensagem_criptografada)
        
        # Descriptografar
        mensagem_original = self.chave_privada.decrypt(
            mensagem_criptografada,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return mensagem_original.decode('utf-8')
    
    def assinar(self, mensagem):
        """
        Cria uma assinatura digital da mensagem
        
        Args:
            mensagem: String a ser assinada
        
        Returns:
            str: Assinatura em base64
        """
        if not self.chave_privada:
            raise ValueError("Chave privada não foi carregada!")
        
        if isinstance(mensagem, str):
            mensagem = mensagem.encode('utf-8')
        
        assinatura = self.chave_privada.sign(
            mensagem,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return base64.b64encode(assinatura).decode('utf-8')
    
    def verificar_assinatura(self, mensagem, assinatura):
        """
        Verifica se uma assinatura é válida
        
        Args:
            mensagem: Mensagem original
            assinatura: Assinatura em base64
        
        Returns:
            bool: True se a assinatura é válida
        """
        if not self.chave_publica:
            raise ValueError("Chave pública não foi carregada!")
        
        try:
            if isinstance(mensagem, str):
                mensagem = mensagem.encode('utf-8')
            
            assinatura_bytes = base64.b64decode(assinatura)
            
            self.chave_publica.verify(
                assinatura_bytes,
                mensagem,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False
    
    def criptografar_arquivo(self, caminho_entrada, caminho_saida):
        """
        Criptografa um arquivo pequeno
        
        Args:
            caminho_entrada: Caminho do arquivo original
            caminho_saida: Caminho do arquivo criptografado
        """
        with open(caminho_entrada, 'rb') as f:
            dados = f.read()
        
        # Para arquivos grandes, seria necessário usar criptografia híbrida
        if len(dados) > 190:  # Limite aproximado para RSA-2048 com OAEP
            raise ValueError("Arquivo muito grande para RSA puro. Use criptografia híbrida.")
        
        dados_criptografados = self.criptografar(dados, usar_base64=False)
        
        with open(caminho_saida, 'wb') as f:
            f.write(dados_criptografados)
        
        print(f"Arquivo criptografado salvo em {caminho_saida}")
    
    def descriptografar_arquivo(self, caminho_entrada, caminho_saida):
        """
        Descriptografa um arquivo
        
        Args:
            caminho_entrada: Caminho do arquivo criptografado
            caminho_saida: Caminho do arquivo descriptografado
        """
        with open(caminho_entrada, 'rb') as f:
            dados_criptografados = f.read()
        
        dados_originais = self.descriptografar(dados_criptografados, eh_base64=False)
        
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(dados_originais)
        
        print(f"Arquivo descriptografado salvo em {caminho_saida}")


def main():
    """Demonstração da implementação RSA avançada"""
    print("=== DEMONSTRAÇÃO RSA AVANÇADO ===\n")
    
    # Criar instância
    rsa_avancado = RSAAvancado()
    
    print("1. GERAÇÃO E SALVAMENTO DE CHAVES")
    print("-" * 40)
    
    # Gerar chaves
    chave_privada_pem, chave_publica_pem = rsa_avancado.gerar_chaves(2048)
    
    # Salvar chaves
    rsa_avancado.salvar_chaves("exemplo")
    print()
    
    print("2. CRIPTOGRAFIA DE MENSAGEM")
    print("-" * 30)
    
    mensagem = "Esta é uma mensagem secreta!"
    print(f"Mensagem original: {mensagem}")
    
    # Criptografar
    mensagem_criptografada = rsa_avancado.criptografar(mensagem)
    print(f"Mensagem criptografada (base64): {mensagem_criptografada[:50]}...")
    
    # Descriptografar
    mensagem_descriptografada = rsa_avancado.descriptografar(mensagem_criptografada)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")
    
    print(f"Sucesso: {mensagem == mensagem_descriptografada}")
    print()
    
    print("3. ASSINATURA DIGITAL")
    print("-" * 20)
    
    # Assinar mensagem
    assinatura = rsa_avancado.assinar(mensagem)
    print(f"Assinatura (base64): {assinatura[:50]}...")
    
    # Verificar assinatura
    valida = rsa_avancado.verificar_assinatura(mensagem, assinatura)
    print(f"Assinatura válida: {valida}")
    
    # Testar com mensagem alterada
    mensagem_alterada = "Esta é uma mensagem secreta alterada!"
    valida_alterada = rsa_avancado.verificar_assinatura(mensagem_alterada, assinatura)
    print(f"Assinatura válida para mensagem alterada: {valida_alterada}")
    print()
    
    print("4. TESTE DE CARREGAMENTO DE CHAVES")
    print("-" * 35)
    
    # Criar nova instância e carregar chaves
    rsa_teste = RSAAvancado()
    rsa_teste.carregar_chave_privada("exemplo_private.pem")
    
    # Testar descriptografia com chaves carregadas
    mensagem_teste = rsa_teste.descriptografar(mensagem_criptografada)
    print(f"Descriptografia com chaves carregadas: {mensagem_teste}")
    print(f"Sucesso: {mensagem == mensagem_teste}")
    
    print()
    print("=== FIM DA DEMONSTRAÇÃO ===")


if __name__ == "__main__":
    main()
