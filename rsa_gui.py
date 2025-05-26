import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import threading
from rsa_avancado import RSAAvancado
import os

class RSAInterface:
    """Interface gráfica para o sistema RSA"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Criptografia RSA - Interface Gráfica")
        self.root.geometry("800x600")
        
        # Instância do RSA
        self.rsa = RSAAvancado()
        
        # Configurar interface
        self.configurar_interface()
        
        # Status
        self.chaves_geradas = False
    
    def configurar_interface(self):
        """Configura todos os elementos da interface"""
        
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Aba 1: Geração de Chaves
        self.aba_chaves = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_chaves, text="Geração de Chaves")
        
        # Aba 2: Criptografia
        self.aba_criptografia = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_criptografia, text="Criptografia")
        
        # Aba 3: Assinatura Digital
        self.aba_assinatura = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_assinatura, text="Assinatura Digital")
        
        # Configurar cada aba
        self.configurar_aba_chaves()
        self.configurar_aba_criptografia()
        self.configurar_aba_assinatura()
    
    def configurar_aba_chaves(self):
        """Configura a aba de geração de chaves"""
        
        # Título
        titulo = ttk.Label(self.aba_chaves, text="Geração e Gerenciamento de Chaves RSA", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Frame para tamanho da chave
        frame_tamanho = ttk.Frame(self.aba_chaves)
        frame_tamanho.pack(pady=10)
        
        ttk.Label(frame_tamanho, text="Tamanho da chave:").pack(side=tk.LEFT, padx=5)
        
        self.var_tamanho = tk.StringVar(value="2048")
        combo_tamanho = ttk.Combobox(frame_tamanho, textvariable=self.var_tamanho,
                                   values=["1024", "2048", "3072", "4096"], state="readonly")
        combo_tamanho.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_tamanho, text="bits").pack(side=tk.LEFT, padx=5)
        
        # Botões
        frame_botoes = ttk.Frame(self.aba_chaves)
        frame_botoes.pack(pady=20)
        
        self.btn_gerar = ttk.Button(frame_botoes, text="Gerar Chaves", 
                                   command=self.gerar_chaves)
        self.btn_gerar.pack(side=tk.LEFT, padx=5)
        
        self.btn_salvar = ttk.Button(frame_botoes, text="Salvar Chaves", 
                                    command=self.salvar_chaves, state=tk.DISABLED)
        self.btn_salvar.pack(side=tk.LEFT, padx=5)
        
        self.btn_carregar = ttk.Button(frame_botoes, text="Carregar Chaves", 
                                      command=self.carregar_chaves)
        self.btn_carregar.pack(side=tk.LEFT, padx=5)
        
        # Status
        self.label_status = ttk.Label(self.aba_chaves, text="Status: Nenhuma chave carregada", 
                                     foreground="red")
        self.label_status.pack(pady=10)
        
        # Área para exibir chaves
        ttk.Label(self.aba_chaves, text="Chave Pública (PEM):").pack(anchor=tk.W, padx=20)
        self.text_chave_publica = scrolledtext.ScrolledText(self.aba_chaves, height=8, width=80)
        self.text_chave_publica.pack(padx=20, pady=5, fill=tk.X)
        
        ttk.Label(self.aba_chaves, text="Chave Privada (PEM):").pack(anchor=tk.W, padx=20)
        self.text_chave_privada = scrolledtext.ScrolledText(self.aba_chaves, height=8, width=80)
        self.text_chave_privada.pack(padx=20, pady=5, fill=tk.X)
    
    def configurar_aba_criptografia(self):
        """Configura a aba de criptografia"""
        
        # Título
        titulo = ttk.Label(self.aba_criptografia, text="Criptografia e Descriptografia", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Frame principal
        frame_principal = ttk.Frame(self.aba_criptografia)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Mensagem original
        ttk.Label(frame_principal, text="Mensagem Original:").pack(anchor=tk.W)
        self.text_mensagem_original = scrolledtext.ScrolledText(frame_principal, height=6)
        self.text_mensagem_original.pack(fill=tk.X, pady=5)
        
        # Botões de criptografia
        frame_botoes_cripto = ttk.Frame(frame_principal)
        frame_botoes_cripto.pack(pady=10)
        
        self.btn_criptografar = ttk.Button(frame_botoes_cripto, text="Criptografar", 
                                          command=self.criptografar_mensagem, state=tk.DISABLED)
        self.btn_criptografar.pack(side=tk.LEFT, padx=5)
        
        self.btn_descriptografar = ttk.Button(frame_botoes_cripto, text="Descriptografar", 
                                             command=self.descriptografar_mensagem, state=tk.DISABLED)
        self.btn_descriptografar.pack(side=tk.LEFT, padx=5)
        
        self.btn_limpar_cripto = ttk.Button(frame_botoes_cripto, text="Limpar", 
                                           command=self.limpar_criptografia)
        self.btn_limpar_cripto.pack(side=tk.LEFT, padx=5)
        
        # Mensagem criptografada
        ttk.Label(frame_principal, text="Mensagem Criptografada (Base64):").pack(anchor=tk.W)
        self.text_mensagem_criptografada = scrolledtext.ScrolledText(frame_principal, height=6)
        self.text_mensagem_criptografada.pack(fill=tk.X, pady=5)
        
        # Mensagem descriptografada
        ttk.Label(frame_principal, text="Mensagem Descriptografada:").pack(anchor=tk.W)
        self.text_mensagem_descriptografada = scrolledtext.ScrolledText(frame_principal, height=6)
        self.text_mensagem_descriptografada.pack(fill=tk.X, pady=5)
    
    def configurar_aba_assinatura(self):
        """Configura a aba de assinatura digital"""
        
        # Título
        titulo = ttk.Label(self.aba_assinatura, text="Assinatura Digital", 
                          font=("Arial", 14, "bold"))
        titulo.pack(pady=10)
        
        # Frame principal
        frame_principal = ttk.Frame(self.aba_assinatura)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Mensagem para assinar
        ttk.Label(frame_principal, text="Mensagem para Assinar:").pack(anchor=tk.W)
        self.text_mensagem_assinar = scrolledtext.ScrolledText(frame_principal, height=6)
        self.text_mensagem_assinar.pack(fill=tk.X, pady=5)
        
        # Botões de assinatura
        frame_botoes_assin = ttk.Frame(frame_principal)
        frame_botoes_assin.pack(pady=10)
        
        self.btn_assinar = ttk.Button(frame_botoes_assin, text="Assinar", 
                                     command=self.assinar_mensagem, state=tk.DISABLED)
        self.btn_assinar.pack(side=tk.LEFT, padx=5)
        
        self.btn_verificar = ttk.Button(frame_botoes_assin, text="Verificar Assinatura", 
                                       command=self.verificar_assinatura, state=tk.DISABLED)
        self.btn_verificar.pack(side=tk.LEFT, padx=5)
        
        self.btn_limpar_assin = ttk.Button(frame_botoes_assin, text="Limpar", 
                                          command=self.limpar_assinatura)
        self.btn_limpar_assin.pack(side=tk.LEFT, padx=5)
        
        # Assinatura
        ttk.Label(frame_principal, text="Assinatura (Base64):").pack(anchor=tk.W)
        self.text_assinatura = scrolledtext.ScrolledText(frame_principal, height=6)
        self.text_assinatura.pack(fill=tk.X, pady=5)
        
        # Resultado da verificação
        self.label_verificacao = ttk.Label(frame_principal, text="", font=("Arial", 12, "bold"))
        self.label_verificacao.pack(pady=10)
    
    def gerar_chaves(self):
        """Gera novas chaves RSA"""
        def gerar():
            try:
                self.btn_gerar.config(state=tk.DISABLED, text="Gerando...")
                tamanho = int(self.var_tamanho.get())
                
                chave_privada_pem, chave_publica_pem = self.rsa.gerar_chaves(tamanho)
                
                # Exibir chaves na interface
                self.text_chave_publica.delete(1.0, tk.END)
                self.text_chave_publica.insert(1.0, chave_publica_pem.decode('utf-8'))
                
                self.text_chave_privada.delete(1.0, tk.END)
                self.text_chave_privada.insert(1.0, chave_privada_pem.decode('utf-8'))
                
                # Atualizar status
                self.chaves_geradas = True
                self.label_status.config(text="Status: Chaves geradas com sucesso!", foreground="green")
                
                # Habilitar botões
                self.btn_salvar.config(state=tk.NORMAL)
                self.btn_criptografar.config(state=tk.NORMAL)
                self.btn_descriptografar.config(state=tk.NORMAL)
                self.btn_assinar.config(state=tk.NORMAL)
                self.btn_verificar.config(state=tk.NORMAL)
                
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao gerar chaves: {str(e)}")
            finally:
                self.btn_gerar.config(state=tk.NORMAL, text="Gerar Chaves")
        
        # Executar em thread separada para não travar a interface
        thread = threading.Thread(target=gerar)
        thread.start()
    
    def salvar_chaves(self):
        """Salva as chaves em arquivos"""
        try:
            nome_arquivo = filedialog.asksaveasfilename(
                title="Salvar chaves como...",
                defaultextension="",
                filetypes=[("Todos os arquivos", "*.*")]
            )
            
            if nome_arquivo:
                self.rsa.salvar_chaves(nome_arquivo)
                messagebox.showinfo("Sucesso", f"Chaves salvas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar chaves: {str(e)}")
    
    def carregar_chaves(self):
        """Carrega chaves de arquivos"""
        try:
            arquivo_privada = filedialog.askopenfilename(
                title="Selecionar chave privada",
                filetypes=[("Arquivos PEM", "*.pem"), ("Todos os arquivos", "*.*")]
            )
            
            if arquivo_privada:
                self.rsa.carregar_chave_privada(arquivo_privada)
                
                # Exibir chave carregada
                with open(arquivo_privada, 'r') as f:
                    self.text_chave_privada.delete(1.0, tk.END)
                    self.text_chave_privada.insert(1.0, f.read())
                
                # Tentar carregar chave pública correspondente
                arquivo_publica = arquivo_privada.replace('_private.pem', '_public.pem')
                if os.path.exists(arquivo_publica):
                    with open(arquivo_publica, 'r') as f:
                        self.text_chave_publica.delete(1.0, tk.END)
                        self.text_chave_publica.insert(1.0, f.read())
                
                # Atualizar status
                self.chaves_geradas = True
                self.label_status.config(text="Status: Chaves carregadas com sucesso!", foreground="green")
                
                # Habilitar botões
                self.btn_salvar.config(state=tk.NORMAL)
                self.btn_criptografar.config(state=tk.NORMAL)
                self.btn_descriptografar.config(state=tk.NORMAL)
                self.btn_assinar.config(state=tk.NORMAL)
                self.btn_verificar.config(state=tk.NORMAL)
                
                messagebox.showinfo("Sucesso", "Chaves carregadas com sucesso!")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar chaves: {str(e)}")
    
    def criptografar_mensagem(self):
        """Criptografa a mensagem"""
        try:
            mensagem = self.text_mensagem_original.get(1.0, tk.END).strip()
            if not mensagem:
                messagebox.showwarning("Aviso", "Digite uma mensagem para criptografar!")
                return
            
            mensagem_criptografada = self.rsa.criptografar(mensagem)
            
            self.text_mensagem_criptografada.delete(1.0, tk.END)
            self.text_mensagem_criptografada.insert(1.0, mensagem_criptografada)
            
            messagebox.showinfo("Sucesso", "Mensagem criptografada com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criptografar: {str(e)}")
    
    def descriptografar_mensagem(self):
        """Descriptografa a mensagem"""
        try:
            mensagem_criptografada = self.text_mensagem_criptografada.get(1.0, tk.END).strip()
            if not mensagem_criptografada:
                messagebox.showwarning("Aviso", "Não há mensagem criptografada para descriptografar!")
                return
            
            mensagem_descriptografada = self.rsa.descriptografar(mensagem_criptografada)
            
            self.text_mensagem_descriptografada.delete(1.0, tk.END)
            self.text_mensagem_descriptografada.insert(1.0, mensagem_descriptografada)
            
            messagebox.showinfo("Sucesso", "Mensagem descriptografada com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao descriptografar: {str(e)}")
    
    def limpar_criptografia(self):
        """Limpa os campos de criptografia"""
        self.text_mensagem_original.delete(1.0, tk.END)
        self.text_mensagem_criptografada.delete(1.0, tk.END)
        self.text_mensagem_descriptografada.delete(1.0, tk.END)
    
    def assinar_mensagem(self):
        """Assina uma mensagem"""
        try:
            mensagem = self.text_mensagem_assinar.get(1.0, tk.END).strip()
            if not mensagem:
                messagebox.showwarning("Aviso", "Digite uma mensagem para assinar!")
                return
            
            assinatura = self.rsa.assinar(mensagem)
            
            self.text_assinatura.delete(1.0, tk.END)
            self.text_assinatura.insert(1.0, assinatura)
            
            messagebox.showinfo("Sucesso", "Mensagem assinada com sucesso!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao assinar: {str(e)}")
    
    def verificar_assinatura(self):
        """Verifica uma assinatura"""
        try:
            mensagem = self.text_mensagem_assinar.get(1.0, tk.END).strip()
            assinatura = self.text_assinatura.get(1.0, tk.END).strip()
            
            if not mensagem or not assinatura:
                messagebox.showwarning("Aviso", "Digite a mensagem e a assinatura!")
                return
            
            valida = self.rsa.verificar_assinatura(mensagem, assinatura)
            
            if valida:
                self.label_verificacao.config(text="✓ Assinatura VÁLIDA", foreground="green")
                messagebox.showinfo("Verificação", "A assinatura é VÁLIDA!")
            else:
                self.label_verificacao.config(text="✗ Assinatura INVÁLIDA", foreground="red")
                messagebox.showwarning("Verificação", "A assinatura é INVÁLIDA!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao verificar assinatura: {str(e)}")
    
    def limpar_assinatura(self):
        """Limpa os campos de assinatura"""
        self.text_mensagem_assinar.delete(1.0, tk.END)
        self.text_assinatura.delete(1.0, tk.END)
        self.label_verificacao.config(text="")


def main():
    """Função principal"""
    root = tk.Tk()
    app = RSAInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
