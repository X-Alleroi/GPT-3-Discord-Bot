import discord
import openai as ai

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(prompt = prompt, engine =  "text-davinci-003", temperature = 0.85,top_p=1, frequency_penalty=0,
    presence_penalty=0.7, best_of=2,max_tokens=3500,stop = "\nHuman: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"{answer}\n"
    return chat_log

if __name__ == "__main__":
    ai.api_key = "API Key Here"

    completion = ai.Completion()

    start_chat_log = ""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(chat(message.content, start_chat_log))

client.run('Bot Token Here')
