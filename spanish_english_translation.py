import openai

openai.api_key = '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'


def main():
    print('Introduce the text to be translated.\n')
    while True:
        txt = input('Text: ')
        response = translate(txt)
        print('Translation: ' + response)


def translate(text):
    prompt = 'Spanish text: ' + text + ' \nEnglish translation:'

    response = openai.Completion.create(
        prompt=prompt,
        engine="davinci",
        temperature=0.5,
        top_p=0,
        stop=['\nSpanish text:', '\nEnglish translation:', '\n'],
        frequency_penalty=0.1,
        presence_penalty=1,
        best_of=1,
        max_tokens=150).choices[0].text
    return response


if __name__ == '__main__':
    main()
