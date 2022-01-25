from factory import Documento

cnpj_um = "22556722000160"
documento_cnpj = Documento.cria_documento(cnpj_um)
print(documento_cnpj)

cpf_um = '03042368378'
documento_cpf = Documento.cria_documento(cpf_um)
print(documento_cpf)

cnh_um = '04158506970'
documento_cnh = Documento.cria_documento(cnh_um)
print(documento_cnh)