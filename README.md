

# TELEGRAM_SSID_PASSWORDS

## Descripción
Este codigo te permite obtener en un archivo de texto a través de un bot en telegram, los SSID y passwords guardados en windows
![1](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/a18673ac-d791-4b8b-b905-00300cf8c353)


### Instalación

* Abrimos una terminal CMD e instalamos PyTelegramBotAPI:
```
pip install PyTelegramBotAPI
```


## 1. Crear bot con BotFather

- Primeramente buscamos en telegram a @BotFather e iniciamos una conversación presionando el boton START:
> ![2](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/8de3efc2-4a88-40eb-b32a-55d907ae4297)

- Despues seleccionamos el comando /newbot:
> ![3](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/f8777f8b-e2e4-4fef-8a10-b48c2d5b4375)

- Escogemos un nombre para nuestro bot:
> ![4](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/058dce55-6e61-4ca4-9dba-af0ecbe69532)


- Ahora agregamos un username que tenga al final bot:
> ![5](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/dfa49f06-648c-45e4-983f-98017d42ec1f)


- Una vez hecho eso, nos va mandar un token:
> ![6](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/0ba3bab3-b150-4466-910a-7e6d9dd1d694)


- Ese token lo vamos a colocar en nuestro codigo de Python:
> ![7](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/7614361a-7797-4626-a403-6c6fc1862701)

- Por ultimo, iniciamos con el boton de START una conversación con nuestro bot:
  > IMPORTANTE INICIAR LA CONVERSACIÓN PARA RECIBIR MENSAJES
> ![8](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/80595d89-3430-4b88-8b04-c73d332c430d)


## 2. Obtener nuestro chat_id
- Buscamos en telegram a @userinfobot y nuevamente presionamos el boton de START:
> ![9](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/4bfc3b17-1f0e-4ca2-859d-f669c1900b99)



- Te va entregar tu CHAT_ID:
> ![10](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/8761dac7-c7fd-483b-aefc-d19416a58b98)


-Ese CHAT_ID, lo colocamos en nuestro codigo de Python:
> ![11](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/dbb60ab5-234d-45f8-81d2-f01d92dd9e13)



## 3. Ejecutamos nuestro codigo:
- Una vez configurado nuestro token y chat_id en nuestro codigo de Python, ahora solo falta ejecutarlo.
- Obtendras en tu bot un archivo txt, ese archivo contiene los SSID Y Paswords:
> ![12](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/85458491-a5bc-4d2e-ad27-f612e55266e8)



> ![13](https://github.com/Kariel97/telegram_wifi_paswords/assets/84166289/d3943127-4c9d-4e88-b9ba-23aa43718003)
