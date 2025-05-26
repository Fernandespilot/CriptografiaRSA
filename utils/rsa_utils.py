"""
Utilitários para trabalhar com RSA
"""

import os
import json
import base64
from datetime import datetime

def salvar_chaves_json(chave_publica_pem, chave_privada_pem, nome_arquivo="chaves_rsa.json"):
    """
    Salva as chaves RSA em formato JSON
    
    Args:
        chave_publica_pem: Chave pública em formato PEM (bytes)
        chave_privada_pem: Chave privada em formato PEM (bytes)
        nome_arquivo: Nome do arquivo para salvar
    
    Returns:
        str: Caminho do arquivo salvo
    """
    dados = {
        "timestamp": datetime.now().isoformat(),
        "chave_publica": base64.b64encode(chave_publica_pem).decode('utf-8'),
        "chave_privada": base64.b64encode(chave_privada_pem).decode('utf-8'),
        "formato": "PEM_BASE64"
    }
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    
    return os.path.abspath(nome_arquivo)

def carregar_chaves_json(nome_arquivo):
    """
    Carrega chaves RSA de um arquivo JSON
    
    Args:
        nome_arquivo: Nome do arquivo para carregar
    
    Returns:
        tuple: (chave_publica_pem, chave_privada_pem)
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    chave_publica_pem = base64.b64decode(dados['chave_publica'])
    chave_privada_pem = base64.b64decode(dados['chave_privada'])
    
    return chave_publica_pem, chave_privada_pem

def texto_para_numeros(texto):
    """Converte texto para lista de números (códigos ASCII/Unicode)"""
    return [ord(char) for char in texto]

def numeros_para_texto(numeros):
    """Converte lista de números para texto"""
    return ''.join([chr(num) for num in numeros])

def formatar_chave_para_exibicao(chave_pem, titulo="Chave"):
    """
    Formata uma chave PEM para exibição bonita
    
    Args:
        chave_pem: Chave em formato PEM (str ou bytes)
        titulo: Título para exibir
    
    Returns:
        str: Chave formatada para exibição
    """
    if isinstance(chave_pem, bytes):
        chave_pem = chave_pem.decode('utf-8')
    
    linhas = chave_pem.strip().split('\n')
    
    resultado = []
    resultado.append(f"{'='*50}")
    resultado.append(f"{titulo:^50}")
    resultado.append(f"{'='*50}")
    
    for linha in linhas:
        if linha.startswith('-----'):
            resultado.append(f"{linha:^50}")
        else:
            # Quebrar linhas longas
            while len(linha) > 50:
                resultado.append(linha[:50])
                linha = linha[50:]
            if linha:
                resultado.append(linha)
    
    resultado.append(f"{'='*50}")
    
    return '\n'.join(resultado)

def verificar_tamanho_chave(chave_publica):
    """
    Verifica o tamanho de uma chave RSA
    
    Args:
        chave_publica: Objeto de chave pública
    
    Returns:
        int: Tamanho da chave em bits
    """
    try:
        return chave_publica.key_size
    except:
        return None

def gerar_relatorio_chaves(rsa_instance):
    """
    Gera um relatório detalhado sobre as chaves
    
    Args:
        rsa_instance: Instância de RSAAvancado
    
    Returns:
        str: Relatório formatado
    """
    if not rsa_instance.chave_publica or not rsa_instance.chave_privada:
        return "Nenhuma chave carregada."
    
    from cryptography.hazmat.primitives import serialization
    
    # Informações da chave
    tamanho = rsa_instance.chave_publica.key_size
    numeros_publicos = rsa_instance.chave_publica.public_numbers()
    
    relatorio = []
    relatorio.append("RELATÓRIO DE CHAVES RSA")
    relatorio.append("=" * 40)
    relatorio.append(f"Tamanho da chave: {tamanho} bits")
    relatorio.append(f"Expoente público (e): {numeros_publicos.e}")
    relatorio.append(f"Módulo (n): {str(numeros_publicos.n)[:50]}... (truncado)")
    relatorio.append(f"Timestamp: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    relatorio.append("")
    
    # Capacidades
    relatorio.append("CAPACIDADES:")
    relatorio.append(f"- Tamanho máximo de mensagem: ~{(tamanho // 8) - 42} bytes")
    relatorio.append("- Criptografia: Sim")
    relatorio.append("- Assinatura digital: Sim")
    relatorio.append("- Padding: OAEP (criptografia), PSS (assinatura)")
    relatorio.append("")
    
    # Segurança
    if tamanho >= 2048:
        nivel_seguranca = "Alto"
    elif tamanho >= 1024:
        nivel_seguranca = "Médio"
    else:
        nivel_seguranca = "Baixo"
    
    relatorio.append(f"NÍVEL DE SEGURANÇA: {nivel_seguranca}")
    relatorio.append("=" * 40)
    
    return '\n'.join(relatorio)

def benchmark_rsa(tamanhos_chave=[1024, 2048, 3072]):
    """
    Faz benchmark de diferentes tamanhos de chave RSA
    
    Args:
        tamanhos_chave: Lista de tamanhos para testar
    
    Returns:
        dict: Resultados do benchmark
    """
    import time
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    from rsa_avancado import RSAAvancado
    
    resultados = {}
    mensagem_teste = "Esta é uma mensagem de teste para benchmark do RSA!"
    
    print("Executando benchmark RSA...")
    print("=" * 50)
    
    for tamanho in tamanhos_chave:
        print(f"Testando chave de {tamanho} bits...")
        
        rsa = RSAAvancado()
        
        # Medir tempo de geração de chaves
        inicio = time.time()
        rsa.gerar_chaves(tamanho)
        tempo_geracao = time.time() - inicio
        
        # Medir tempo de criptografia
        inicio = time.time()
        for _ in range(10):  # 10 iterações
            mensagem_criptografada = rsa.criptografar(mensagem_teste)
        tempo_criptografia = (time.time() - inicio) / 10
        
        # Medir tempo de descriptografia
        inicio = time.time()
        for _ in range(10):  # 10 iterações
            rsa.descriptografar(mensagem_criptografada)
        tempo_descriptografia = (time.time() - inicio) / 10
        
        # Medir tempo de assinatura
        inicio = time.time()
        for _ in range(10):  # 10 iterações
            assinatura = rsa.assinar(mensagem_teste)
        tempo_assinatura = (time.time() - inicio) / 10
        
        # Medir tempo de verificação
        inicio = time.time()
        for _ in range(10):  # 10 iterações
            rsa.verificar_assinatura(mensagem_teste, assinatura)
        tempo_verificacao = (time.time() - inicio) / 10
        
        resultados[tamanho] = {
            'geracao_chaves': tempo_geracao,
            'criptografia': tempo_criptografia,
            'descriptografia': tempo_descriptografia,
            'assinatura': tempo_assinatura,
            'verificacao': tempo_verificacao
        }
        
        print(f"  Geração: {tempo_geracao:.3f}s")
        print(f"  Criptografia: {tempo_criptografia:.4f}s")
        print(f"  Descriptografia: {tempo_descriptografia:.4f}s")
        print(f"  Assinatura: {tempo_assinatura:.4f}s")
        print(f"  Verificação: {tempo_verificacao:.4f}s")
        print("-" * 30)
    
    return resultados

def criar_certificado_simples(nome, email, rsa_instance):
    """
    Cria um 'certificado' simples (não é um certificado X.509 real)
    
    Args:
        nome: Nome do proprietário
        email: Email do proprietário
        rsa_instance: Instância RSA com chaves
    
    Returns:
        dict: Certificado simples
    """
    from cryptography.hazmat.primitives import serialization
    
    if not rsa_instance.chave_publica:
        raise ValueError("Chave pública não encontrada!")
    
    # Dados do certificado
    dados_certificado = {
        'versao': '1.0',
        'proprietario': {
            'nome': nome,
            'email': email
        },
        'chave_publica': base64.b64encode(
            rsa_instance.chave_publica.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        ).decode('utf-8'),
        'valido_de': datetime.now().isoformat(),
        'valido_ate': datetime(2026, 5, 25).isoformat(),
        'numero_serie': f"RSA-{hash(nome + email) % 1000000:06d}"
    }
    
    # "Assinar" o certificado (auto-assinado)
    certificado_str = json.dumps(dados_certificado, sort_keys=True)
    assinatura = rsa_instance.assinar(certificado_str)
    
    certificado_completo = {
        'dados': dados_certificado,
        'assinatura': assinatura,
        'algoritmo_assinatura': 'RSA-PSS-SHA256'
    }
    
    return certificado_completo

def validar_certificado_simples(certificado, chave_publica_rsa):
    """
    Valida um certificado simples
    
    Args:
        certificado: Certificado a validar
        chave_publica_rsa: Instância RSA com chave pública
    
    Returns:
        dict: Resultado da validação
    """
    try:
        # Verificar estrutura
        if 'dados' not in certificado or 'assinatura' not in certificado:
            return {'valido': False, 'erro': 'Estrutura inválida'}
        
        # Verificar datas
        valido_de = datetime.fromisoformat(certificado['dados']['valido_de'])
        valido_ate = datetime.fromisoformat(certificado['dados']['valido_ate'])
        agora = datetime.now()
        
        if agora < valido_de or agora > valido_ate:
            return {'valido': False, 'erro': 'Certificado fora do período de validade'}
        
        # Verificar assinatura
        certificado_str = json.dumps(certificado['dados'], sort_keys=True)
        assinatura_valida = chave_publica_rsa.verificar_assinatura(
            certificado_str, 
            certificado['assinatura']
        )
        
        if not assinatura_valida:
            return {'valido': False, 'erro': 'Assinatura inválida'}
        
        return {
            'valido': True,
            'proprietario': certificado['dados']['proprietario'],
            'numero_serie': certificado['dados']['numero_serie'],
            'valido_ate': valido_ate.strftime('%d/%m/%Y')
        }
        
    except Exception as e:
        return {'valido': False, 'erro': f'Erro na validação: {str(e)}'}

def limpar_arquivos_temporarios(diretorio="."):
    """Remove arquivos temporários de chaves"""
    import glob
    
    padroes = [
        "*.pem",
        "exemplo_private.pem",
        "exemplo_public.pem", 
        "chaves_rsa.json"
    ]
    
    removidos = []
    for padrao in padroes:
        for arquivo in glob.glob(os.path.join(diretorio, padrao)):
            try:
                os.remove(arquivo)
                removidos.append(arquivo)
            except:
                pass
    
    return removidos
