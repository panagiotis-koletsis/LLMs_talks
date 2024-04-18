import ollama  # Assuming ollama is your library for chat interactions
ollama.pull('mistral')
print("mistral pull complete")
ollama.pull('zephyr')
print("zephyr pull complete")
question = 'Tell me something'

messages = []

def askM(question):
    messages.append(
        {
            'role': 'user',
            'content': question,
        }
    )
    #print(question)
    stream = ollama.chat(
        model='mistral',
        messages=messages,
        stream=True
    )
    response = ''
    for chunk in stream:
        message_content = chunk['message']['content']
        response += message_content
    messages.append(
        {
            'role': 'assistant',
            'content': response,
        }
    )
    print("--Mistral",response)
    return response
    # for chunk in stream:
    #     print(chunk['message']['content'], end='', flush=True)


def askZ(question):
    messages.append(
        {
            'role': 'user',
            'content': question,
        }
    )
    #print(question)
    stream = ollama.chat(
        model='Zephyr',
        messages=messages,
        stream=True
    )
    response = ''
    for chunk in stream:
        message_content = chunk['message']['content']
        response += message_content
    messages.append(
        {
            'role': 'assistant',
            'content': response,
        }
    )
    print("--Zephyr",response)
    return response
    # for chunk in stream:
    #     print(chunk['message']['content'], end='', flush=True)


responseM = 'Tell me something related to motorbikes'
print("Mistral",responseM)
responseZ = ''
for i in range(5):
    if (i % 2 ==0):
        responseZ = askZ(responseM)
    else:
        responseM = askM(responseZ)





