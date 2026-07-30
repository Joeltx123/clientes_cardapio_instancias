import os
import base64

OUTPUT_FILE = "projeto_completo_para_ia.md"

def generate_tree(startpath='.'):
    tree_str = "## 🌳 Mapeamento Completo da Estrutura de Pastas e Arquivos\n\n```text\n"
    for root, dirs, files in os.walk(startpath):
        # Remove o próprio arquivo de saída da listagem se já existir
        if OUTPUT_FILE in files:
            files.remove(OUTPUT_FILE)
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * level + ('├── ' if level > 0 else '')
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        sub_indent = '│   ' * (level + 1) + '├── '
        for f in sorted(files):
            tree_str += f"{sub_indent}{f}\n"
    tree_str += "```\n\n---\n\n"
    return tree_str

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except Exception:
        return True
    return False

def bundle_project():
    print("🚀 Iniciando a varredura total do projeto (sem exclusões)...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write("# 📂 Projeto Completo - Cardápio Pro (Varredura Total sem Filtros)\n\n")
        outfile.write("Este documento contém **absolutamente tudo** do projeto: código-fonte, configurações, banco de dados e dependências do ambiente virtual.\n\n---\n\n")
        
        print("Mapeando a estrutura de diretórios...")
        outfile.write(generate_tree('.'))
        
        for root, dirs, files in os.walk('.'):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                
                if os.path.abspath(file_path) == os.path.abspath(OUTPUT_FILE):
                    continue
                
                print(f"Processando: {file_path}")
                outfile.write(f"## Arquivo: `{file_path}`\n\n")
                
                if is_binary(file_path):
                    outfile.write("*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*\n\n")
                    try:
                        with open(file_path, 'rb') as bin_file:
                            encoded = base64.b64encode(bin_file.read()).decode('utf-8')
                            outfile.write(f"```base64\n{encoded}\n```\n\n---\n\n")
                    except Exception as e:
                        outfile.write(f"Erro ao processar arquivo binário: {e}\n\n---\n\n")
                else:
                    outfile.write("```text\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"Erro ao ler arquivo: {e}\n")
                    outfile.write("\n```\n\n---\n\n")
                    
    print(f"\n✨ Sucesso absoluto! O arquivo `{OUTPUT_FILE}` foi gerado na raiz do projeto.")

if __name__ == "__main__":
    bundle_project()
