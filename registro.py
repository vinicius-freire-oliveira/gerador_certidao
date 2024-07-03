"""Requisitos:
- Matrícula com número de 32 dígitos, 
- O primeiro grupo com seis dígitos identifica cartório
- O segundo grupo com dois dígitos identifica acervo (01 - Código de acervo próprio)
- O terceiro grupo com dois dígitos identifica nº do serviço de registro civil (55 - Código do Registro Civil de Pessoas Naturais)
- O quarto grupo com quatro dígitos identifica o ano
- O quinto grupo com um dígito para tipo de certidão:
 * 1 para nascimento 
 * 2 para casamento
 * 3 para casamento religioso com efeito civil)
 * 4 para óbito
- O sexto grupo com cinco dígitos para número do livro
- O sétimo grupo com três dígitos para número da folha
- O oitavo grupo com 7 dígitos para número do termo
- O nono grupo com 2 dígitos para dígito verificador"""

import random
import string

# Classe para geração de registros civis
class RegistroCivil:
    # Método estático para gerar registro de nascimento
    @staticmethod
    def gerar_registro_nascimento():
        # Geração dos dígitos aleatórios para cada grupo da matrícula
        codigo_cartorio = ''.join(random.choices(string.digits, k=6))  # Código do cartório (6 dígitos)
        codigo_acervo = "01"  # Código de acervo próprio (fixo em 01)
        ano_registro = random.randint(1900, 2023)  # Ano do registro (4 dígitos)
        tipo_certidao = "1"  # Tipo de certidão (1 para nascimento)
        numero_livro = ''.join(random.choices(string.digits, k=5))  # Número do livro (5 dígitos)
        numero_folha = ''.join(random.choices(string.digits, k=3))  # Número da folha (3 dígitos)
        numero_termo = ''.join(random.choices(string.digits, k=7))  # Número do termo (7 dígitos)
        
        # Cálculo do dígito verificador
        matricula = f"{codigo_cartorio}{codigo_acervo}55{ano_registro}{tipo_certidao}{numero_livro}{numero_folha}{numero_termo}"
        soma = sum(int(digito) for digito in matricula)
        digito_verificador = soma % 100

        # Retorna a matrícula formatada
        return f"{codigo_cartorio} {codigo_acervo} 55 {ano_registro} {tipo_certidao} {numero_livro} {numero_folha} {numero_termo} {str(digito_verificador).zfill(2)}"

    # Método estático para gerar registro de casamento
    @staticmethod
    def gerar_registro_casamento():
        # Geração dos dígitos aleatórios para cada grupo da matrícula
        codigo_cartorio = ''.join(random.choices(string.digits, k=6))  # Código do cartório (6 dígitos)
        codigo_acervo = "01"  # Código de acervo próprio (fixo em 01)
        ano_registro = random.randint(1900, 2023)  # Ano do registro (4 dígitos)
        tipo_certidao = "2"  # Tipo de certidão (2 para casamento)
        numero_livro = ''.join(random.choices(string.digits, k=5))  # Número do livro (5 dígitos)
        numero_folha = ''.join(random.choices(string.digits, k=3))  # Número da folha (3 dígitos)
        numero_termo = ''.join(random.choices(string.digits, k=7))  # Número do termo (7 dígitos)
        
        # Cálculo do dígito verificador
        matricula = f"{codigo_cartorio}{codigo_acervo}55{ano_registro}{tipo_certidao}{numero_livro}{numero_folha}{numero_termo}"
        soma = sum(int(digito) for digito in matricula)
        digito_verificador = soma % 100

        # Retorna a matrícula formatada
        return f"{codigo_cartorio} {codigo_acervo} 55 {ano_registro} {tipo_certidao} {numero_livro} {numero_folha} {numero_termo} {str(digito_verificador).zfill(2)}"

    # Método estático para gerar registro de casamento religioso com efeito civil
    @staticmethod
    def gerar_registro_casamento_religioso():
        # Geração dos dígitos aleatórios para cada grupo da matrícula
        codigo_cartorio = ''.join(random.choices(string.digits, k=6))  # Código do cartório (6 dígitos)
        codigo_acervo = "01"  # Código de acervo próprio (fixo em 01)
        ano_registro = random.randint(1900, 2023)  # Ano do registro (4 dígitos)
        tipo_certidao = "3"  # Tipo de certidão (3 para casamento religioso com efeito civil)
        numero_livro = ''.join(random.choices(string.digits, k=5))  # Número do livro (5 dígitos)
        numero_folha = ''.join(random.choices(string.digits, k=3))  # Número da folha (3 dígitos)
        numero_termo = ''.join(random.choices(string.digits, k=7))  # Número do termo (7 dígitos)
        
        # Cálculo do dígito verificador
        matricula = f"{codigo_cartorio}{codigo_acervo}55{ano_registro}{tipo_certidao}{numero_livro}{numero_folha}{numero_termo}"
        soma = sum(int(digito) for digito in matricula)
        digito_verificador = soma % 100

        # Retorna a matrícula formatada
        return f"{codigo_cartorio} {codigo_acervo} 55 {ano_registro} {tipo_certidao} {numero_livro} {numero_folha} {numero_termo} {str(digito_verificador).zfill(2)}"

    # Método estático para gerar registro de óbito
    @staticmethod
    def gerar_registro_obito():
        # Geração dos dígitos aleatórios para cada grupo da matrícula
        codigo_cartorio = ''.join(random.choices(string.digits, k=6))  # Código do cartório (6 dígitos)
        codigo_acervo = "01"  # Código de acervo próprio (fixo em 01)
        ano_registro = random.randint(1900, 2023)  # Ano do registro (4 dígitos)
        tipo_certidao = "4"  # Tipo de certidão (4 para óbito)
        numero_livro = ''.join(random.choices(string.digits, k=5))  # Número do livro (5 dígitos)
        numero_folha = ''.join(random.choices(string.digits, k=3))  # Número da folha (3 dígitos)
        numero_termo = ''.join(random.choices(string.digits, k=7))  # Número do termo (7 dígitos)
        
        # Cálculo do dígito verificador
        matricula = f"{codigo_cartorio}{codigo_acervo}55{ano_registro}{tipo_certidao}{numero_livro}{numero_folha}{numero_termo}"
        soma = sum(int(digito) for digito in matricula)
        digito_verificador = soma % 100

        # Retorna a matrícula formatada
        return f"{codigo_cartorio} {codigo_acervo} 55 {ano_registro} {tipo_certidao} {numero_livro} {numero_folha} {numero_termo} {str(digito_verificador).zfill(2)}"

# Função para simular a geração de registros civis
def simular_registro_civil():
    print("Simulação de Registro Civil\n")
    print("Registro de Nascimento:", RegistroCivil.gerar_registro_nascimento())
    print("Registro de Casamento:", RegistroCivil.gerar_registro_casamento())
    print("Registro de Casamento Religioso com Efeito Civil:", RegistroCivil.gerar_registro_casamento_religioso())
    print("Registro de Óbito:", RegistroCivil.gerar_registro_obito())

# Executar a simulação
simular_registro_civil()
