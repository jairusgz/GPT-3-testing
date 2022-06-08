import openai

openai.api_key = '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'


def main():
    chat_log = 'AI: Hello, I am GPT-3. I am here to help you. Please ask me anything.'
    print(chat_log)
    while True:
        response, log = ask_question(chat_log)
        print('AI: ' + response)
        chat_log += log
        if chat_log.count('\nAI: ') > 5:
            chat_log = chat_log[-1000:]


def ask_question(chat_log):
    question = input('You: ')
    chat_log += '\nYou: ' + question + '\n'
    prompt = chat_log + '\nAI: '
    if len(prompt) > 1500:
        prompt = prompt[-1000:]
    response = openai.Completion.create(
        prompt=prompt,
        engine="davinci",
        stop=['\nYou', '.AI', '\nAI'],
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=1,
        best_of=1,
        max_tokens=150).choices[0].text
    chat_log += '\nAI: ' + response
    return response, chat_log


if __name__ == '__main__':
    main()
