import pandas as pd
import os

def ler_excel(caminho_arquivo):
    """
    Lê o arquivo Excel e retorna um DataFrame.
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    return pd.read_excel(caminho_arquivo)

def identificar_novos_modulos(df, modulos_processados):
    """
    Identifica novos módulos na coluna 'group1' que ainda não foram processados.
    """
    # Extrai todos os módulos únicos da coluna 'group1'
    todos_modulos = df['group1'].dropna().unique()
    
    # Filtra apenas os módulos que ainda não foram processados
    novos_modulos = [modulo for modulo in todos_modulos if modulo not in modulos_processados]
    return novos_modulos

def extrair_materias_e_cidades(df, novo_modulo):
    """
    Para um novo módulo, extrai as matérias (course1) e cidades (profile_field_descnre) associadas.
    Garante que não haja duplicatas de combinações "Módulo + Matéria".
    """
    # Filtra o DataFrame para o módulo específico
    df_filtrado = df[df['group1'] == novo_modulo]
    
    # Cria uma lista de tuplas (modulo, materia, cidade)
    materias_cidades = [
        (novo_modulo, row['course1'], row['profile_field_descnre'])
        for _, row in df_filtrado.iterrows()
        if pd.notna(row['course1']) and pd.notna(row['profile_field_descnre'])
    ]
    
    # Remove duplicatas mantendo a ordem original
    materias_cidades_unicas = []
    seen = set()
    for item in materias_cidades:
        if item not in seen:
            materias_cidades_unicas.append(item)
            seen.add(item)
    
    return materias_cidades_unicas

def salvar_resultados(resultados, caminho_saida):
    """
    Salva os resultados em um novo arquivo Excel com as colunas TURMA, MATÉRIA e CIDADE.
    """
    # Converte os resultados para um DataFrame
    df_resultados = pd.DataFrame(resultados, columns=["TURMA", "MATÉRIA", "CIDADE"])
    
    # Salva o DataFrame em um arquivo Excel
    df_resultados.to_excel(caminho_saida, index=False)
    print(f"Resultados salvos em: {caminho_saida}")

def main():
    # Configurações
    caminho_arquivo_original = "C:\\Users\\"  # Substitua pelo caminho real
    caminho_arquivo_saida = "C:\\Users\\"          # Substitua pelo caminho real
    
    # Lista de módulos já processados (pode ser carregada de um arquivo ou banco de dados)
    modulos_processados = []  # Exemplo: ["Módulo 1 - 2373891"]
    
    try:
        # Passo 1: Ler o arquivo Excel original
        print("Lendo o arquivo Excel original...")
        df = ler_excel(caminho_arquivo_original)
        
        # Passo 2: Identificar novos módulos
        print("Identificando novos módulos...")
        novos_modulos = identificar_novos_modulos(df, modulos_processados)
        
        if not novos_modulos:
            print("Nenhum novo módulo encontrado.")
            return
        
        print(f"Novos módulos encontrados: {novos_modulos}")
        
        # Passo 3: Extrair matérias e cidades para cada novo módulo
        print("Extraindo matérias e cidades...")
        resultados = []
        for modulo in novos_modulos:
            materias_cidades = extrair_materias_e_cidades(df, modulo)
            resultados.extend(materias_cidades)
            
            # Atualiza a lista de módulos processados
            modulos_processados.append(modulo)
        
        # Passo 4: Salvar os resultados em um novo arquivo Excel
        print("Salvando os resultados...")
        salvar_resultados(resultados, caminho_arquivo_saida)
        
        print("Processamento concluído com sucesso!")
    
    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    main()