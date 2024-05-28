import httpx, os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv('AI_TOKEN'),
                     http_client=httpx.AsyncClient(
                        proxies=os.getenv('PROXY'),
                        transport=httpx.HTTPTransport(local_address='0.0.0.0')
                    ))

async def gpt4(question):
    response = await client.chat.completions.create(
        messages=[{
            'role': 'system',
            'content': 'Текст отправляется в Телеграм с разметкой Markdown, поэтому формируй сообщения в соответствии с требованиями функции message.answer(response.choices[0].message.content, parse_mode="Markdown"), чтобы не было кусков синтаксиса в ответе'
        },
        {
            'role': 'user',
            'content': str(question)
        }],
        model='gpt-4o'
    )
    return response