import g4f
from gtts import gTTS

from g4f.Provider import (
    Bard,
    Bing,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
)

# Initialize messages list with specific message
messages = [{"role": "user", "content": "TürkTelekom'da çalışan müşteri hizmetleri temsilcisi olarak görev yapmanızı istiyorum. Size sorduğum her soruya bir Türk Telekom çalışanıymış gibi ve talebe özel bir yanıtla yanıt vereceksiniz. Rolünüze olabilecek en gerçekçi şekilde yaklaşarak sadece bir müşteri hizmetleri temsilcisinin ilgileneceği konular hakkında cevaplar verirseniz sevinirim. Bu mesaja 'Merhaba, ben TürkTelekom Müşteri Hizmetleri'nden Bing. Bugün size nasıl yardımcı olabilirim?' şeklinde yanıt vererek konuşmaya başlayın."}]

# Run g4f.ChatCompletion with specific message
response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=messages,  # Use specific message
    provider=Bing,
    cookies={"_U": "1LLeZXAKKUoOd-7gq_BcU_x6KZ-_NbCv_HZ7puip53_II8yTx93cr3TscYEjq1rnyUiFOrQU7wNbdlpOZzxK2AAAkzGbaLaELV8hbpdsM_WOu8fFaaqh309O_IHY7vOzlcRdYD08uFW_Jo0j9H3eRvrg5K51rF-uELtOaqkOycyIyx368PNMdkuwd7OYN0fEVCb8A--qVczuiP4UkK5oaGg"},
    auth=False,
    stream=True
)

# Print response from provider
full_response = ""
print("Bing: ", end="")
for message in response:
    print(message, flush=True, end='')
    # Append AI message to messages list
    full_response += message
messages.append({"role": "system", "content": full_response})

print() #Empty line

while True:
    user_input = str(input("Siz: "))
    if user_input.lower() == "çıkış":
        break

    # Append user message to messages list
    messages.append({"role": "user", "content": user_input})

    # Usage:
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=messages,  # Use updated messages list
        provider=Bing,
        cookies={"_U": "1LLeZXAKKUoOd-7gq_BcU_x6KZ-_NbCv_HZ7puip53_II8yTx93cr3TscYEjq1rnyUiFOrQU7wNbdlpOZzxK2AAAkzGbaLaELV8hbpdsM_WOu8fFaaqh309O_IHY7vOzlcRdYD08uFW_Jo0j9H3eRvrg5K51rF-uELtOaqkOycyIyx368PNMdkuwd7OYN0fEVCb8A--qVczuiP4UkK5oaGg"},
        auth=False,
        stream=True
    )
    
    # Print response from provider
    full_response = ""
    print("Bing: ", end="")
    for message in response:
        print(message, flush=True, end='')
        # Append AI message to messages list
        full_response += message
    messages.append({"role": "system", "content": full_response})

    print() #Empty line