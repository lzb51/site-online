#tela inicial:  
    #titulo: hashzap
    #botao: iniciar chat:
        # quando clicar no botao   
        # abrir um poup/alerta
            #titulo: bem vindo ao haszap    
            #caixa de texto: escreva seu nome no chat
            #botao: entrar no chat
                #quando clicar no botao:
                    #sumir popup
                    #sumir o titulo
                    #sumir o botao iniciar chat
                        #carregar chat
                        # carregar o campo de enviar mensagem: "digite sua mensagem" 
                        # botao enviar
                        #   quando clicar no botao enviar
                            #enviar a mensagem
                            # limpar a caixa de mensagem

#pip install flet -> pra fazer o site
#importar a biblioteca

import flet as ft


#criar uma funcao principal para rodar o seu aplicativo
     #         |
     #         |
     #         V
     #como fazer
#def nome_da_funcao(parametro):
#    o que essa funcao vai fazer
#    passo 1 
#    passo 2
#    passo 3
#    passo 4

def main (pagina):

   

     #titulo 
    titulo = ft.Text("Hashzap")


    #websocket -> tunel para ter mais gente se falando

    def enviar_mensagem_tunel(mensagem):
        #executar tudo oq eu quero que aconteca para todos os usuarios que recebem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    #criar tunel de comunicacao
    pagina.pubsub.subscribe(enviar_mensagem_tunel)    
    
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        
        
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        #chat.controls.append(texto) <-para adicionar valor
        campo_enviar_mensagem.value = "" #<- limpar a caixa de texto
        pagina.update()


    campo_enviar_mensagem = ft.TextField(label="Digite aqui a sua mensagem:",
                                          on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar]) #<- dentro de uma lista para colocar varias coisas na mesma linha

    chat = ft.Column()

    def entrar_chat(envento):
    #quando clicar no botao:
        #sumir popup
        popup.open = False
        #sumir o titulo
        pagina.remove(titulo)
        #sumir o botao iniciar chat
        pagina.remove(botao)
        
        #carregar chat   
        pagina.add(chat)


        # botao enviar
        # carregar o campo de enviar mensagem: "digite sua mensagem" 
        pagina.add(linha_enviar)


        #adicionar no chat a mensagem "pessoa entrou no chato"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)

        pagina.update()

                         

    #criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click= entrar_chat)
    popup = ft.AlertDialog(
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup] )# <- esta em uma lista por estar no plural ent da para colocar mais de uma coisa dentro dessa funcao / bom pra quando for fazer algo na tela


    #botao inicial
    #tem q ter um parametro para conseguir receber informação
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() #<- atualizar a tela para o usuario 



    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    

    #colocar elementos
    pagina.add(titulo)
    pagina.add(botao)




#executar essa funcao com o flet


#apertar ctrl + c -> para fechar o site

ft.app(main, view=ft.WEB_BROWSER)



#colocar online para todos -> deploy flet


