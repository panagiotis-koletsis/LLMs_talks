import ollama
ollama.pull('mistral')
print("mistral pull complete")
# ollama.pull('zephyr')
# print("zephyr pull complete")


messages = []

# def askZ(question):
#     messages.append(
#         {
#             'role': 'user',
#             'content': question,
#         }
#     )
#     print(question)
#     stream = ollama.chat(
#         model='Zephyr',
#         messages=messages,
#         stream=True
#     )
#     response = ''
#     for chunk in stream:
#         message_content = chunk['message']['content']
#         response += message_content
#     messages.append(
#         {
#             'role': 'assistant',
#             'content': response,
#         }
#     )
#     print("test",response)
#     return response
#     # for chunk in stream:
#     #     print(chunk['message']['content'], end='', flush=True)

def askM(question):
    messages.append(
        {
            'role': 'user',
            'content': question,
        }
    )
    print(question)
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
    print("test",response)
    return response
    # for chunk in stream:
    #     print(chunk['message']['content'], end='', flush=True)

question = 'My name is panos'
responseM = askM(question)
question2 = 'tell me something related to motorbikes'
#askM(question2)
#askZ(responseM)

# for i in range(9):
#     if (i % 2 == 1):
#         askM(question)
#     else:
#         askZ()
