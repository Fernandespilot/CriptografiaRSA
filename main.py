"""
Script para executar todos os exemplos e testes
"""

import sys
import os

# Adicionar diretórios ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils'))

def menu_principal():
    """Exibe o menu principal"""
    print("=" * 60)
    print("🔐 SISTEMA DE CRIPTOGRAFIA RSA 🔐")
    print("=" * 60)
    print("Escolha uma opção:")
    print()
    print("1. 📚 Executar RSA Básico (Implementação Educacional)")
    print("2. 🔒 Executar RSA Avançado (Produção)")
    print("3. 💬 Exemplo de Comunicação Segura")
    print("4. 🖥️  Interface Gráfica (GUI)")
    print("5. 📊 Benchmark de Performance")
    print("6. 📋 Relatório de Chaves")
    print("7. 🧪 Executar Todos os Exemplos")
    print("8. 🧹 Limpar Arquivos Temporários")
    print("9. 📖 Como Funciona o RSA (Explicação)")
    print("10. 🛡️ Análise de Segurança e Tempo de Quebra")
    print("0. ❌ Sair")
    print()
    print("=" * 60)

def executar_rsa_basico():
    """Executa o exemplo RSA básico"""
    print("\n🔍 Executando RSA Básico...")
    try:
        from rsa_basico import main
        main()
    except Exception as e:
        print(f"Erro: {e}")

def executar_rsa_avancado():
    """Executa o exemplo RSA avançado"""
    print("\n🔒 Executando RSA Avançado...")
    try:
        from rsa_avancado import main
        main()
    except Exception as e:
        print(f"Erro: {e}")

def executar_comunicacao():
    """Executa exemplo de comunicação segura"""
    print("\n💬 Executando Comunicação Segura...")
    try:
        from exemplos.comunicacao_segura import main
        main()
    except Exception as e:
        print(f"Erro: {e}")

def executar_gui():
    """Executa a interface gráfica"""
    print("\n🖥️ Abrindo Interface Gráfica...")
    try:
        from rsa_gui import main
        main()
    except Exception as e:
        print(f"Erro: {e}")
        print("Certifique-se de que o tkinter está instalado!")

def executar_benchmark():
    """Executa benchmark de performance"""
    print("\n📊 Executando Benchmark...")
    try:
        from utils.rsa_utils import benchmark_rsa
        resultados = benchmark_rsa([1024, 2048])
        
        print("\n📈 RESUMO DO BENCHMARK:")
        print("-" * 40)
        for tamanho, tempos in resultados.items():
            print(f"Chave {tamanho} bits:")
            print(f"  Mais rápido: Verificação ({tempos['verificacao']:.4f}s)")
            print(f"  Mais lento: Geração ({tempos['geracao_chaves']:.3f}s)")
            print()
    except Exception as e:
        print(f"Erro: {e}")

def gerar_relatorio_chaves():
    """Gera relatório das chaves"""
    print("\n📋 Gerando Relatório de Chaves...")
    try:
        from rsa_avancado import RSAAvancado
        from utils.rsa_utils import gerar_relatorio_chaves
        
        rsa = RSAAvancado()
        print("Gerando chaves para o relatório...")
        rsa.gerar_chaves(2048)
        
        relatorio = gerar_relatorio_chaves(rsa)
        print("\n" + relatorio)
        
        # Salvar relatório
        with open("relatorio_chaves.txt", "w", encoding='utf-8') as f:
            f.write(relatorio)
        print("\n💾 Relatório salvo em 'relatorio_chaves.txt'")
        
    except Exception as e:
        print(f"Erro: {e}")

def executar_todos():
    """Executa todos os exemplos"""
    print("\n🧪 Executando Todos os Exemplos...")
    print("=" * 50)
    
    exemplos = [
        ("RSA Básico", executar_rsa_basico),
        ("RSA Avançado", executar_rsa_avancado),
        ("Comunicação Segura", executar_comunicacao),
        ("Benchmark", executar_benchmark),
        ("Relatório", gerar_relatorio_chaves)
    ]
    
    for nome, funcao in exemplos:
        print(f"\n▶️ Executando {nome}...")
        try:
            funcao()
            print(f"✅ {nome} concluído!")
        except Exception as e:
            print(f"❌ Erro em {nome}: {e}")
        
        print("-" * 30)
    
    print("\n🎉 Todos os exemplos foram executados!")

def limpar_temporarios():
    """Limpa arquivos temporários"""
    print("\n🧹 Limpando Arquivos Temporários...")
    try:
        from utils.rsa_utils import limpar_arquivos_temporarios
        removidos = limpar_arquivos_temporarios()
        
        if removidos:
            print("Arquivos removidos:")
            for arquivo in removidos:
                print(f"  - {arquivo}")
        else:
            print("Nenhum arquivo temporário encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

def explicar_rsa():
    """Explica como funciona o algoritmo RSA"""
    print("\n📖 COMO FUNCIONA O ALGORITMO RSA")
    print("=" * 60)
    
    print("\n🧮 FUNDAMENTOS MATEMÁTICOS:")
    print("-" * 30)
    print("O RSA baseia-se na dificuldade de fatorar números muito grandes.")
    print("É fácil multiplicar dois primos, mas difícil encontrá-los conhecendo apenas o produto.")
    
    print("\n🔑 GERAÇÃO DAS CHAVES:")
    print("-" * 25)
    print("1. Escolha dois números primos grandes: p e q")
    print("2. Calcule n = p × q (módulo público)")
    print("3. Calcule φ(n) = (p-1) × (q-1)")
    print("4. Escolha e (expoente público, geralmente 65537)")
    print("5. Calcule d (expoente privado): d × e ≡ 1 (mod φ(n))")
    print("\nResultado:")
    print("• Chave Pública: (e, n)")
    print("• Chave Privada: (d, n)")
    
    print("\n🔐 PROCESSO DE CRIPTOGRAFIA:")
    print("-" * 32)
    print("• Para criptografar mensagem m: C = m^e mod n")
    print("• Para descriptografar cifra C: m = C^d mod n")
    
    print("\n✍️ ASSINATURA DIGITAL:")
    print("-" * 24)
    print("• Assinar: S = hash(mensagem)^d mod n")
    print("• Verificar: hash(mensagem) = S^e mod n")
    
    print("\n🛡️ POR QUE É SEGURO:")
    print("-" * 20)
    print("• A segurança depende da dificuldade de fatorar n")
    print("• Conhecendo n, é preciso encontrar p e q")
    print("• Com p e q, pode-se calcular d (chave privada)")
    print("• Para números grandes, isso é computacionalmente inviável")

def mostrar_analise_seguranca():
    """Mostra análise detalhada de segurança"""
    print("\n🛡️ ANÁLISE DE SEGURANÇA E TEMPO DE QUEBRA")
    print("=" * 60)
    
    print("\n⏱️ TEMPO PARA QUEBRAR RSA (COMPUTADOR COMUM):")
    print("-" * 48)
    
    tamanhos = [
        ("512 bits", "INSEGURO", "~1 ano", "Quebrado em 1999"),
        ("1024 bits", "VULNERÁVEL", "~10.000 anos", "Evite usar"),
        ("2048 bits", "SEGURO", "~300 bilhões de anos", "Recomendado"),
        ("3072 bits", "MUITO SEGURO", "Mais que idade do universo", "Longo prazo"),
        ("4096 bits", "EXTREMAMENTE SEGURO", "Praticamente impossível", "Máxima segurança")
    ]
    
    for tamanho, status, tempo, observacao in tamanhos:
        print(f"• {tamanho:12} | {status:18} | {tempo:25} | {observacao}")
    
    print("\n🖥️ CENÁRIOS DE ATAQUE:")
    print("-" * 25)
    print("• Computador doméstico (Intel i7):")
    print("  - RSA-2048: ~10^15 anos (1 quatrilhão de anos)")
    print("• Cluster de 1000 computadores:")
    print("  - RSA-2048: ~10^12 anos (1 trilhão de anos)")
    print("• Supercomputador (ex: Fugaku):")
    print("  - RSA-2048: ~1 bilhão de anos")
    
    print("\n⚡ CRESCIMENTO DA DIFICULDADE:")
    print("-" * 32)
    print("• +1 bit na chave = dobra a dificuldade")
    print("• +10 bits = 1024x mais difícil")
    print("• +100 bits = 2^100 ≈ 10^30 vezes mais difícil")
    
    print("\n🤖 AMEAÇAS FUTURAS:")
    print("-" * 18)
    print("• Computadores quânticos com Algoritmo de Shor")
    print("• RSA-2048 seria quebrado em poucas horas")
    print("• Por isso existe pesquisa em criptografia pós-quântica")
    
    print("\n📊 PARA COMPARAÇÃO:")
    print("-" * 18)
    print("• Idade do universo: ~4.3 × 10^17 segundos")
    print("• Átomos no universo: ~10^80")
    print("• Tempo para quebrar RSA-2048: ~10^604 segundos")
    print("  (Incompreensivelmente maior que qualquer escala temporal!)")

def verificar_dependencias():
    """Verifica se as dependências estão instaladas"""
    print("🔍 Verificando dependências...")
    
    dependencias = {
        'cryptography': 'Biblioteca principal de criptografia',
        'tkinter': 'Interface gráfica (geralmente incluído no Python)',
    }
    
    faltando = []
    
    for dep, desc in dependencias.items():
        try:
            if dep == 'tkinter':
                import tkinter
            else:
                __import__(dep)
            print(f"✅ {dep}: OK")
        except ImportError:
            print(f"❌ {dep}: FALTANDO ({desc})")
            faltando.append(dep)
    
    if faltando:
        print(f"\n⚠️ Instale as dependências faltando:")
        print("pip install cryptography")
        return False
    
    print("\n✅ Todas as dependências estão instaladas!")
    return True

def explicar_rsa():
    """Explica como funciona o algoritmo RSA"""
    print("\n📖 COMO FUNCIONA O ALGORITMO RSA")
    print("=" * 60)
    
    print("\n🧮 FUNDAMENTOS MATEMÁTICOS:")
    print("-" * 30)
    print("O RSA baseia-se na dificuldade de fatorar números muito grandes.")
    print("É fácil multiplicar dois primos, mas difícil encontrá-los conhecendo apenas o produto.")
    
    print("\n🔑 GERAÇÃO DAS CHAVES:")
    print("-" * 25)
    print("1. Escolha dois números primos grandes: p e q")
    print("2. Calcule n = p × q (módulo público)")
    print("3. Calcule φ(n) = (p-1) × (q-1)")
    print("4. Escolha e (expoente público, geralmente 65537)")
    print("5. Calcule d (expoente privado): d × e ≡ 1 (mod φ(n))")
    print("\nResultado:")
    print("• Chave Pública: (e, n)")
    print("• Chave Privada: (d, n)")
    
    print("\n🔐 PROCESSO DE CRIPTOGRAFIA:")
    print("-" * 32)
    print("• Para criptografar mensagem m: C = m^e mod n")
    print("• Para descriptografar cifra C: m = C^d mod n")
    
    print("\n✍️ ASSINATURA DIGITAL:")
    print("-" * 24)
    print("• Assinar: S = hash(mensagem)^d mod n")
    print("• Verificar: hash(mensagem) = S^e mod n")
    
    print("\n🛡️ POR QUE É SEGURO:")
    print("-" * 20)
    print("• A segurança depende da dificuldade de fatorar n")
    print("• Conhecendo n, é preciso encontrar p e q")
    print("• Com p e q, pode-se calcular d (chave privada)")
    print("• Para números grandes, isso é computacionalmente inviável")

def mostrar_analise_seguranca():
    """Mostra análise detalhada de segurança"""
    print("\n🛡️ ANÁLISE DE SEGURANÇA E TEMPO DE QUEBRA")
    print("=" * 60)
    
    print("\n⏱️ TEMPO PARA QUEBRAR RSA (COMPUTADOR COMUM):")
    print("-" * 48)
    
    tamanhos = [
        ("512 bits", "INSEGURO", "~1 ano", "Quebrado em 1999"),
        ("1024 bits", "VULNERÁVEL", "~10.000 anos", "Evite usar"),
        ("2048 bits", "SEGURO", "~300 bilhões de anos", "Recomendado"),
        ("3072 bits", "MUITO SEGURO", "Mais que idade do universo", "Longo prazo"),
        ("4096 bits", "EXTREMAMENTE SEGURO", "Praticamente impossível", "Máxima segurança")
    ]
    
    for tamanho, status, tempo, observacao in tamanhos:
        print(f"• {tamanho:12} | {status:18} | {tempo:25} | {observacao}")
    
    print("\n🖥️ CENÁRIOS DE ATAQUE:")
    print("-" * 25)
    print("• Computador doméstico (Intel i7):")
    print("  - RSA-2048: ~10^15 anos (1 quatrilhão de anos)")
    print("• Cluster de 1000 computadores:")
    print("  - RSA-2048: ~10^12 anos (1 trilhão de anos)")
    print("• Supercomputador (ex: Fugaku):")
    print("  - RSA-2048: ~1 bilhão de anos")
    
    print("\n⚡ CRESCIMENTO DA DIFICULDADE:")
    print("-" * 32)
    print("• +1 bit na chave = dobra a dificuldade")
    print("• +10 bits = 1024x mais difícil")
    print("• +100 bits = 2^100 ≈ 10^30 vezes mais difícil")
    
    print("\n🤖 AMEAÇAS FUTURAS:")
    print("-" * 18)
    print("• Computadores quânticos com Algoritmo de Shor")
    print("• RSA-2048 seria quebrado em poucas horas")
    print("• Por isso existe pesquisa em criptografia pós-quântica")
    
    print("\n📊 PARA COMPARAÇÃO:")
    print("-" * 18)
    print("• Idade do universo: ~4.3 × 10^17 segundos")
    print("• Átomos no universo: ~10^80")
    print("• Tempo para quebrar RSA-2048: ~10^604 segundos")
    print("  (Incompreensivelmente maior que qualquer escala temporal!)")

def main():
    """Função principal"""
    # Verificar dependências primeiro
    if not verificar_dependencias():
        print("\n❌ Algumas dependências estão faltando.")
        print("Execute: pip install -r requirements.txt")
        return
    
    while True:
        menu_principal()
        
        try:
            opcao = input("Digite sua opção: ").strip()
            
            if opcao == "0":
                print("\n👋 Obrigado por usar o Sistema RSA!")
                break
            elif opcao == "1":
                executar_rsa_basico()
            elif opcao == "2":
                executar_rsa_avancado()
            elif opcao == "3":
                executar_comunicacao()
            elif opcao == "4":
                executar_gui()
            elif opcao == "5":
                executar_benchmark()
            elif opcao == "6":
                gerar_relatorio_chaves()
            elif opcao == "7":
                executar_todos()
            elif opcao == "8":
                limpar_temporarios()
                
            elif opcao == "9":
                explicar_rsa()            
            elif opcao == "10":
                mostrar_analise_seguranca()
            else:
                print("\n❌ Opção inválida! Tente novamente.")
            
            if opcao != "0":
                input("\n⏸️ Pressione Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("\n⏸️ Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
