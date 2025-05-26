# Projeto de Criptografia RSA

Este projeto implementa algoritmos de criptografia RSA em Python com diferentes níveis de complexidade.

## Estrutura do Projeto

- `rsa_basico.py` - Implementação básica do RSA
- `rsa_avancado.py` - Implementação avançada com mais recursos
- `rsa_gui.py` - Interface gráfica para usar o RSA
- `exemplos/` - Exemplos práticos de uso
- `utils/` - Utilitários auxiliares

## Como usar

### Instalação das dependências
```bash
pip install -r requirements.txt
```

### Executar a implementação básica
```bash
python rsa_basico.py
```

### Executar a interface gráfica
```bash
python rsa_gui.py
```

## Funcionalidades

- Geração de chaves RSA
- Criptografia e descriptografia de mensagens
- Assinatura digital
- Interface gráfica intuitiva
- Exemplos práticos

## Segurança

⚠️ **Atenção**: Este código é para fins educacionais. Para uso em produção, use bibliotecas criptográficas testadas e auditadas.





======================================
🔐 GUIA COMPLETO: SISTEMA DE CRIPTOGRAFIA RSA
=====================================
Data: 25 de maio de 2025
Autor: Sistema RSA Automático
===================================

📋 ÍNDICE
===================================
1. COMANDOS PARA EXECUTAR OS TESTES
2. COMO FUNCIONA O ALGORITMO RSA
3. ANÁLISE DE SEGURANÇA E TEMPO DE QUEBRA
4. EXEMPLOS PRÁTICOS DE USO
5. TROUBLESHOOTING E DICAS

===============================================================================
1. COMANDOS PARA EXECUTAR OS TESTES
===============================================================================

🔧 PREPARAÇÃO INICIAL:
----------------------
1. Abra o PowerShell ou Prompt de Comando
2. Navegue até o diretório do projeto:
   cd "c:\Users\FabLab Maker\CriptografiaRSA"

3. Instale as dependências (se ainda não instalou):
   python -m pip install -r requirements.txt

🚀 COMANDOS PARA EXECUTAR CADA TESTE:
-------------------------------------

A) MENU PRINCIPAL INTERATIVO (RECOMENDADO):
   python main.py
   - Execute este comando e siga o menu interativo
   - Oferece todas as opções organizadas

B) TESTES INDIVIDUAIS:

   1. RSA Básico (Implementação Educacional):
      python rsa_basico.py
      * Mostra como o RSA funciona matematicamente
      * Usa números pequenos para fins didáticos

   2. RSA Avançado (Implementação de Produção):
      python rsa_avancado.py
      * Usa bibliotecas criptográficas robustas
      * Chaves de 2048 bits (segurança real)

   3. Exemplos Práticos:
      python exemplos/exemplo_basico.py
      * Demonstrações completas
      * Testa diferentes tipos de mensagens

   4. Comunicação Segura:
      python exemplos/comunicacao_segura.py
      * Simula troca de mensagens entre duas pessoas
      * Mostra assinatura digital

   5. Interface Gráfica:
      python rsa_gui.py
      * Interface visual para usar RSA facilmente
      * Criptografar/descriptografar com cliques

C) TESTE COMPLETO AUTOMATIZADO:
   python main.py
   Depois digite "7" para executar todos os exemplos

🔍 VERIFICAÇÃO DE FUNCIONAMENTO:
-------------------------------
Se tudo está funcionando, você deve ver:
- Geração de chaves RSA
- Criptografia e descriptografia de mensagens
- Verificação de assinatura digital
- Tempos de execução dos processos

===============================================================================
2. COMO FUNCIONA O ALGORITMO RSA
===============================================================================

🧮 FUNDAMENTOS MATEMÁTICOS:
---------------------------
O RSA (Rivest-Shamir-Adleman) é baseado na dificuldade de fatorar números 
muito grandes. Aqui está como funciona:

PASSO 1: GERAÇÃO DAS CHAVES
---------------------------
1. Escolha dois números primos grandes: p e q
   Exemplo: p = 61, q = 53

2. Calcule n = p × q
   Exemplo: n = 61 × 53 = 3233

3. Calcule φ(n) = (p-1) × (q-1)
   Exemplo: φ(n) = 60 × 52 = 3120

4. Escolha e (expoente público):
   - Deve ser coprimo com φ(n)
   - Comumente usado: e = 65537
   Exemplo: e = 17 (para simplificar)

5. Calcule d (expoente privado):
   - d × e ≡ 1 (mod φ(n))
   - d é o inverso modular de e
   Exemplo: d = 2753

RESULTADO:
- Chave Pública: (e, n) = (17, 3233)
- Chave Privada: (d, n) = (2753, 3233)

PASSO 2: CRIPTOGRAFIA
---------------------
Para criptografar mensagem m:
C = m^e mod n

Exemplo: m = 123
C = 123^17 mod 3233 = 855

PASSO 3: DESCRIPTOGRAFIA
------------------------
Para descriptografar cifra C:
m = C^d mod n

Exemplo: C = 855
m = 855^2753 mod 3233 = 123

🔐 PROPRIEDADES IMPORTANTES:
---------------------------
1. UNIDIRECIONAL: É fácil calcular C a partir de m, mas difícil o contrário
   sem conhecer d

2. CHAVES ASSIMÉTRICAS: 
   - Chave pública: pode ser compartilhada
   - Chave privada: deve ser mantida em segredo

3. ASSINATURA DIGITAL:
   - Assinar: S = hash(m)^d mod n
   - Verificar: hash(m) = S^e mod n

🧠 POR QUE FUNCIONA:
-------------------
A segurança do RSA depende do "Problema da Fatoração de Inteiros":

- É FÁCIL: Multiplicar dois primos grandes (p × q = n)
- É DIFÍCIL: Encontrar p e q conhecendo apenas n

Se um atacante conseguir fatorar n em p e q, ele pode:
1. Calcular φ(n) = (p-1)(q-1)
2. Calcular d (chave privada)
3. Quebrar toda a criptografia

===============================================================================
3. ANÁLISE DE SEGURANÇA E TEMPO DE QUEBRA
===============================================================================

⏱️ TEMPO PARA QUEBRAR RSA COM COMPUTADORES COMUNS:
--------------------------------------------------

TAMANHOS DE CHAVE E SEGURANÇA:

512 bits (INSEGURO):
- Quebrado em 1999
- Computador comum: ~1 ano (com software otimizado)
- Status: NUNCA USE

1024 bits (VULNERÁVEL):
- Quebrado por organizações com recursos
- Computador comum: ~1.000-10.000 anos
- Cluster de computadores: ~1-10 anos
- Status: EVITE

2048 bits (SEGURO ATUALMENTE):
- Computador comum: ~300 bilhões de anos
- Supercomputador: ~300 milhões de anos
- Status: RECOMENDADO até 2030

3072 bits (MUITO SEGURO):
- Computador comum: Mais que a idade do universo
- Equivale a AES-128
- Status: RECOMENDADO para longo prazo

4096 bits (EXTREMAMENTE SEGURO):
- Praticamente impossível de quebrar
- Equivale a AES-192
- Status: MÁXIMA SEGURANÇA

📊 EXEMPLO PRÁTICO DE CÁLCULO:
-----------------------------
Para quebrar RSA-2048 com força bruta:

Operações necessárias: ~2^2048 ÷ 2 = ~10^616 operações
Computador moderno: ~10^12 operações/segundo
Tempo necessário: ~10^604 segundos

Para comparação:
- Idade do universo: ~4.3 × 10^17 segundos
- Número de átomos no universo: ~10^80

O tempo para quebrar RSA-2048 é incompreensivelmente maior que qualquer 
escala temporal conhecida!

🖥️ CENÁRIOS REALISTAS DE ATAQUE:
--------------------------------

COMPUTADOR DOMÉSTICO (Intel i7, 8 cores):
- RSA-512: ~2-5 anos (com software especializado)
- RSA-1024: ~50.000 anos
- RSA-2048: ~10^15 anos (1 quatrilhão de anos)

CLUSTER DE 1000 COMPUTADORES:
- RSA-1024: ~50 anos
- RSA-2048: ~10^12 anos (1 trilhão de anos)

SUPERCOMPUTADOR (como Fugaku - Japão):
- RSA-1024: ~1-5 anos
- RSA-2048: ~1 bilhão de anos

COMPUTADOR QUÂNTICO (FUTURO):
- Algoritmo de Shor pode quebrar RSA em tempo polinomial
- RSA-2048: Poucas horas com computador quântico suficientemente grande
- Por isso existe pesquisa em criptografia pós-quântica

🛡️ MÉTODOS DE ATAQUE CONHECIDOS:
-------------------------------

1. FORÇA BRUTA:
   - Testar todas as chaves possíveis
   - Impraticável para chaves grandes

2. FATORAÇÃO:
   - Método mais eficiente conhecido
   - Algoritmos como GNFS (General Number Field Sieve)
   - Ainda exponencial em complexidade

3. ATAQUES LATERAIS:
   - Timing attacks
   - Power analysis
   - Falhas na implementação

4. ATAQUES MATEMÁTICOS:
   - Exploram propriedades específicas de números escolhidos
   - Raros, mas possíveis com implementações ruins

⚡ CRESCIMENTO DA DIFICULDADE:
-----------------------------
O tempo para quebrar RSA cresce EXPONENCIALMENTE com o tamanho da chave:

- +1 bit na chave = dobra a dificuldade
- +10 bits na chave = 1024x mais difícil
- +100 bits na chave = 2^100 ≈ 10^30 vezes mais difícil

Por isso RSA-2048 é trilhões de trilhões de vezes mais seguro que RSA-1024!

===============================================================================
4. EXEMPLOS PRÁTICOS DE USO
===============================================================================

🌐 ONDE O RSA É USADO NO MUNDO REAL:
------------------------------------

1. HTTPS/TLS:
   - Navegadores web usam RSA para estabelecer conexões seguras
   - Certificados SSL/TLS

2. EMAIL SEGURO:
   - PGP/GPG usa RSA para criptografia de emails
   - Assinatura digital de mensagens

3. SSH:
   - Conexões seguras a servidores
   - Autenticação sem senha

4. BLOCKCHAIN:
   - Bitcoin e outras criptomoedas
   - Assinatura de transações

5. DOCUMENTOS DIGITAIS:
   - Assinatura de contratos
   - Certificados digitais

💼 EXEMPLO DE USO CORPORATIVO:
-----------------------------
Empresa A quer enviar dados confidenciais para Empresa B:

1. Empresa B gera par de chaves RSA
2. Empresa B envia chave pública para Empresa A
3. Empresa A criptografa dados com chave pública de B
4. Empresa A envia dados criptografados
5. Empresa B descriptografa com sua chave privada

🔒 EXEMPLO DE ASSINATURA DIGITAL:
--------------------------------
Advogado quer assinar contrato digitalmente:

1. Advogado gera hash do documento
2. Advogado "assina" o hash com sua chave privada
3. Qualquer pessoa pode verificar com a chave pública do advogado
4. Se documento for alterado, hash muda e assinatura fica inválida

===============================================================================
5. TROUBLESHOOTING E DICAS
===============================================================================

❌ PROBLEMAS COMUNS E SOLUÇÕES:
------------------------------

ERRO: "pip não reconhecido"
SOLUÇÃO: 
python -m pip install -r requirements.txt

ERRO: "No module named pip"
SOLUÇÃO:
python -m ensurepip --upgrade
python -m pip install -r requirements.txt

ERRO: "No module named tkinter"
SOLUÇÃO:
- Windows: tkinter já vem com Python
- Linux: sudo apt-get install python3-tk
- macOS: brew install python-tk

ERRO: Interface gráfica não abre
SOLUÇÃO:
- Verifique se está executando em ambiente gráfico
- Teste: python -c "import tkinter; print('OK')"

⚡ DICAS DE PERFORMANCE:
-----------------------

1. TAMANHO DA CHAVE:
   - 2048 bits: Bom equilíbrio segurança/performance
   - 4096 bits: Máxima segurança, mais lento

2. IMPLEMENTAÇÃO:
   - Use sempre bibliotecas criptográficas estabelecidas
   - Nunca implemente RSA do zero para produção

3. GERAÇÃO DE NÚMEROS ALEATÓRIOS:
   - Use geradores criptograficamente seguros
   - /dev/urandom no Linux, CryptGenRandom no Windows

📈 MONITORAMENTO DE PERFORMANCE:
-------------------------------
Execute o benchmark para medir performance no seu sistema:
python main.py
Opção 5: Benchmark de Performance

🔧 CONFIGURAÇÕES RECOMENDADAS:
-----------------------------

DESENVOLVIMENTO/TESTE:
- RSA-1024: Rápido para testes
- RSA-2048: Recomendado

PRODUÇÃO:
- RSA-2048: Mínimo recomendado
- RSA-3072: Para dados muito sensíveis
- RSA-4096: Máxima segurança

EMBARCADO/IoT:
- RSA-1024: Se performance for crítica
- Considere usar ECC como alternativa

⚠️ AVISOS IMPORTANTES DE SEGURANÇA:
----------------------------------

1. NUNCA compartilhe sua chave privada
2. SEMPRE use bibliotecas criptográficas testadas
3. MANTENHA suas chaves em local seguro
4. USE senhas fortes para proteger chaves privadas
5. ATUALIZE regularmente suas bibliotecas criptográficas
6. CONSIDERE migração para criptografia pós-quântica

===============================================================================
📚 RECURSOS ADICIONAIS
===============================================================================

LIVROS RECOMENDADOS:
- "Applied Cryptography" - Bruce Schneier
- "Handbook of Applied Cryptography" - Menezes, Oorschot, Vanstone

ARTIGOS CIENTÍFICOS:
- Rivest, R.L., Shamir, A., Adleman, L. (1978). "A Method for Obtaining 
  Digital Signatures and Public-Key Cryptosystems"

FERRAMENTAS ONLINE:
- OpenSSL: Geração de chaves RSA
- GnuPG: Criptografia prática com RSA

CURSOS:
- Coursera: Cryptography (Stanford University)
- edX: Introduction to Cryptography

=================
🎯 CONCLUSÃO
=================

O RSA continua sendo um dos algoritmos de criptografia mais importantes e 
amplamente utilizados. Sua segurança baseia-se em um problema matemático 
extremamente difícil de resolver, tornando-o praticamente impossível de 
quebrar com computadores clássicos quando usado com chaves de tamanho adequado.

Com este guia, você tem:
✅ Comandos para executar todos os testes
✅ Compreensão completa de como o RSA funciona
✅ Análise detalhada de segurança e tempos de quebra
✅ Exemplos práticos de uso
✅ Soluções para problemas comuns

Execute os testes, experimente com diferentes tamanhos de chave, e explore 
como este algoritmo fundamental protege a maior parte da comunicação digital 
moderna!

=============
FIM DO GUIA
============
