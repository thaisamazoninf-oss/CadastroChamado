import pyautogui
import pyperclip
import time
import json


# Carrega os dados do JSON externo
with open('dados_assyst.json', 'r', encoding='utf-8') as f:
    dados_assyst = json.load(f)

tipos = dados_assyst['tipos']
assuntos = dados_assyst['assuntos']

#Escolhar o perfil do usuário 

while True:        
    print("\nPerfis disponiveis:")
    for chave, info in tipos.items():
            print(f"- {chave}: {info['perfil']}")
            
    entrada_tipo = input("Digite as opções disponiveis a cima: ").strip().upper()
    if entrada_tipo in tipos:
        break
    else:
        print("Tipo inválido. Tente novamente.")

print(f"Você escolheu o tipo: {entrada_tipo}")
    
tipo = tipos[entrada_tipo]

#------------ Mostra assunto --------------------------#
print("\nAssuntos disponiveis:")
for chave, info in assuntos.items():
    print(f"- {chave}: {info['titulo']}")

entrada_assunto = input("Digite o assunto exatamente como mostrado acima: ").strip().lower()
if entrada_assunto not in assuntos:
    print("Assunto inválido.")
    exit()
    
#--------------- Concatenação -----------------------------------# 
perfil = tipos[entrada_tipo]["perfil"]

conteudo = assuntos[entrada_assunto]["resol"]

texto = f"Em ligação com {perfil} {conteudo}"
#--------------------- Ações ----------------------------------#

print("\nClique em ações")
time.sleep(2)
pyautogui.click(x=1214, y=222)

if entrada_assunto in ["1", "5"]:
    print("\nClique em resolver")
    time.sleep(2)
    pyautogui.click(x=1225, y=437)
    time.sleep(5)

    # 1x TAB. 
    time.sleep(0.5)
    pyautogui.press("tab")
else:
    print("\nClique em atribuir")
    time.sleep(2)
    pyautogui.click(x=1232, y=314)
    time.sleep(5)

    #Digita Advogado
    print("\nAdicionando S.Operação")    
    time.sleep(2)
    pyautogui.write('S. OPE')
    time.sleep(2)
    
    print("\nClique em S.Operação")
    time.sleep(2)
    pyautogui.click(x=193, y=406)
    
    # 2x TAb
    for _ in range(2):
        pyautogui.press("tab")
        time.sleep(0.2)
    
# Adicionando Descrição. 
print("\nAdicionando descrição")
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")


