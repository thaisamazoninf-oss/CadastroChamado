import pyautogui
import pyperclip
import time

def preencher_assyst(tipo, nome, oab, estado, cpf, email, matricula, assunto_titulo, maquina_titulo, tipos, assuntos, modos, maquinas, tombo, modo_titulo):
    
    if tipo == "":
        print("Erro perfil não selecionado.")
        return
    
    if tipo == "S":
        usuario_formatado = matricula.strip()
    elif tipo == "AE":
        usuario_formatado = f"{nome.strip().upper()} OAB {estado.strip().upper()} nº:{oab.strip()} - D"
    elif tipo == "E":
        usuario_formatado = f"{nome.strip().upper()} CPF - {cpf.strip()}"
    elif tipo == "Q":
        usuario_formatado = "USUARIO NAO REGISTRADO(Usuário Não Registrado)"
    elif tipo == "A":
        usuario_formatado = f"OAB:{oab.strip()}"


    #--------------- Concatenação -----------------------------------# 
    entrada_assunto = [k for k,v in assuntos.items() if v ['titulo'] == assunto_titulo][0]

    assunto = assuntos[entrada_assunto]
    
    entrada_modo = [k for k,v in modos.items() if v['tituloModo'] == modo_titulo][0]
    
    entrada_maquina =  [k for k,v in maquinas.items() if v['tituloMaquina'] == maquina_titulo][0]
    if tipo !="S":
        modo_titulo = ""
        maquina_titulo = ""
    
    perfil = tipos[tipo]["perfil"]

    conteudo = assunto["resol"]
    
    atribuir = assunto['atribuir']

    texto = f"Em ligação com {perfil},{conteudo}\n" if tipo == "E" else f"Em ligação com {perfil}{conteudo}"

#--------------------- Ações ----------------------------------#

    print("\nClique em ações")
    time.sleep(2)
    pyautogui.click(x=1214, y=222)

    if entrada_assunto in ["1", "5","16"]:
        print("\nClique em atribuir")
        time.sleep(2)
        pyautogui.click(x=1232, y=314)
        time.sleep(5)    
    
        #Digita Setor de atribuição
        print("\nAdicionando S.Operação")    
        time.sleep(2)
        pyperclip.copy(atribuir)
        pyautogui.hotkey("ctrl", "v")
        print("\nClique em S.Operação")
        time.sleep(2)
        pyautogui.click(x=373, y=412)
        
        time.sleep(2)
        
        # 2x TAb
        for _ in range(2):
            pyautogui.press("tab")
            time.sleep(0.2)

        # Adicionando Descrição. 
        print("\nAdicionando descrição")
        pyautogui.write('Verificar por gentileza.')
        
    else:
        
        print("\nClique em resolver")
        time.sleep(2)
        pyautogui.click(x=1274, y=439)
        time.sleep(5)
        
        # 1x TAB. 
        time.sleep(0.5)
        pyautogui.press("tab")
    
        # Adicionando Descrição. 
        print("\nAdicionando descrição")
        pyperclip.copy(texto)
        pyautogui.hotkey("ctrl", "v")    
