import random
import math

class RSABasico:
    """
    Implementação básica do algoritmo RSA para fins educacionais.
    """
    
    def __init__(self):
        self.chave_publica = None
        self.chave_privada = None
        self.n = None
    
    def eh_primo(self, num):
        """Verifica se um número é primo"""
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    def gerar_primo(self, bits=8):
        """Gera um número primo com o número especificado de bits"""
        while True:
            num = random.getrandbits(bits)
            if self.eh_primo(num):
                return num
    
    def mdc(self, a, b):
        """Calcula o Máximo Divisor Comum usando algoritmo de Euclides"""
        while b:
            a, b = b, a % b
        return a
    
    def inverso_modular(self, a, m):
        """Calcula o inverso modular usando algoritmo euclidiano estendido"""
        if self.mdc(a, m) != 1:
            return None
        
        # Algoritmo euclidiano estendido
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        
        return x1 + m0 if x1 < 0 else x1
    
    def gerar_chaves(self, bits=8):
        """
        Gera um par de chaves RSA
        
        Args:
            bits: Número de bits para os números primos (padrão: 8)
        
        Returns:
            tuple: (chave_publica, chave_privada)
        """
        print("Gerando chaves RSA...")
        
        # Passo 1: Gerar dois números primos distintos
        p = self.gerar_primo(bits)
        q = self.gerar_primo(bits)
        
        while p == q:  # Garantir que p e q são diferentes
            q = self.gerar_primo(bits)
        
        print(f"p = {p}")
        print(f"q = {q}")
        
        # Passo 2: Calcular n = p * q
        self.n = p * q
        print(f"n = p * q = {self.n}")
        
        # Passo 3: Calcular φ(n) = (p-1) * (q-1)
        phi_n = (p - 1) * (q - 1)
        print(f"φ(n) = (p-1) * (q-1) = {phi_n}")
        
        # Passo 4: Escolher e tal que 1 < e < φ(n) e mdc(e, φ(n)) = 1
        e = 65537  # Número comumente usado
        if e >= phi_n:
            e = 3  # Fallback para números pequenos
            
        while self.mdc(e, phi_n) != 1:
            e += 2
        
        print(f"e = {e}")
        
        # Passo 5: Calcular d tal que (d * e) mod φ(n) = 1
        d = self.inverso_modular(e, phi_n)
        print(f"d = {d}")
        
        # Chave pública: (e, n)
        self.chave_publica = (e, self.n)
        
        # Chave privada: (d, n)
        self.chave_privada = (d, self.n)
        
        print(f"Chave pública: {self.chave_publica}")
        print(f"Chave privada: {self.chave_privada}")
        
        return self.chave_publica, self.chave_privada
    
    def exponenciacao_modular(self, base, expoente, modulo):
        """Calcula (base^expoente) mod modulo de forma eficiente"""
        resultado = 1
        base = base % modulo
        
        while expoente > 0:
            if expoente % 2 == 1:
                resultado = (resultado * base) % modulo
            expoente = expoente >> 1
            base = (base * base) % modulo
        
        return resultado
    
    def criptografar(self, mensagem, chave_publica=None):
        """
        Criptografa uma mensagem usando a chave pública
        
        Args:
            mensagem: String ou número a ser criptografado
            chave_publica: Tupla (e, n) da chave pública
        
        Returns:
            list: Lista de números criptografados
        """
        if chave_publica is None:
            chave_publica = self.chave_publica
        
        if chave_publica is None:
            raise ValueError("Chave pública não foi gerada ainda!")
        
        e, n = chave_publica
        
        # Converter string para lista de números (ASCII)
        if isinstance(mensagem, str):
            numeros = [ord(char) for char in mensagem]
        else:
            numeros = [mensagem] if isinstance(mensagem, int) else mensagem
        
        # Criptografar cada número
        criptografado = []
        for num in numeros:
            if num >= n:
                raise ValueError(f"Número {num} é maior que n={n}. Use chaves maiores!")
            
            # c = m^e mod n
            c = self.exponenciacao_modular(num, e, n)
            criptografado.append(c)
        
        return criptografado
    
    def descriptografar(self, mensagem_criptografada, chave_privada=None):
        """
        Descriptografa uma mensagem usando a chave privada
        
        Args:
            mensagem_criptografada: Lista de números criptografados
            chave_privada: Tupla (d, n) da chave privada
        
        Returns:
            str: Mensagem descriptografada
        """
        if chave_privada is None:
            chave_privada = self.chave_privada
        
        if chave_privada is None:
            raise ValueError("Chave privada não foi gerada ainda!")
        
        d, n = chave_privada
        
        # Descriptografar cada número
        descriptografado = []
        for c in mensagem_criptografada:
            # m = c^d mod n
            m = self.exponenciacao_modular(c, d, n)
            descriptografado.append(m)
        
        # Converter números de volta para string
        try:
            mensagem = ''.join([chr(num) for num in descriptografado])
            return mensagem
        except ValueError:
            return descriptografado  # Retornar números se não puder converter para string


def main():
    """Exemplo de uso da implementação RSA básica"""
    print("=== DEMONSTRAÇÃO RSA BÁSICO ===\n")
    
    # Criar instância do RSA
    rsa = RSABasico()
    
    # Gerar chaves
    print("1. GERAÇÃO DE CHAVES")
    print("-" * 30)
    chave_publica, chave_privada = rsa.gerar_chaves(bits=10)
    print()
    
    # Exemplo com string
    print("2. CRIPTOGRAFIA DE STRING")
    print("-" * 30)
    mensagem_original = "OLA"
    print(f"Mensagem original: '{mensagem_original}'")
    
    try:
        mensagem_criptografada = rsa.criptografar(mensagem_original)
        print(f"Mensagem criptografada: {mensagem_criptografada}")
        
        mensagem_descriptografada = rsa.descriptografar(mensagem_criptografada)
        print(f"Mensagem descriptografada: '{mensagem_descriptografada}'")
        
        print(f"Sucesso: {mensagem_original == mensagem_descriptografada}")
    except ValueError as e:
        print(f"Erro: {e}")
        print("Tentando com chaves maiores...")
        rsa.gerar_chaves(bits=12)
        mensagem_criptografada = rsa.criptografar(mensagem_original)
        mensagem_descriptografada = rsa.descriptografar(mensagem_criptografada)
        print(f"Mensagem descriptografada: '{mensagem_descriptografada}'")
    
    print()
    
    # Exemplo com número
    print("3. CRIPTOGRAFIA DE NÚMERO")
    print("-" * 30)
    numero_original = 42
    print(f"Número original: {numero_original}")
    
    try:
        numero_criptografado = rsa.criptografar(numero_original)
        print(f"Número criptografado: {numero_criptografado}")
        
        numero_descriptografado = rsa.descriptografar(numero_criptografado)
        print(f"Número descriptografado: {numero_descriptografado}")
        
        # Converter de volta para int se retornado como lista
        if isinstance(numero_descriptografado, list):
            numero_descriptografado = numero_descriptografado[0]
        else:
            numero_descriptografado = ord(numero_descriptografado)
        
        print(f"Sucesso: {numero_original == numero_descriptografado}")
    except ValueError as e:
        print(f"Erro: {e}")
    
    print()
    print("=== FIM DA DEMONSTRAÇÃO ===")


if __name__ == "__main__":
    main()
