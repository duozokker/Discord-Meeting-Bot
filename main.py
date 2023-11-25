import discord
from discord.ext import commands
import random
import os



intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Enable the message content intent


bot = commands.Bot(command_prefix="!", intents=intents)

# Data structure to hold the user categories
user_categories = {
    "Green": [],
    "Yellow": [],
    "Red": [],
    "Blue": []
}

async def update_embed():
    embed = discord.Embed(title="User Categories", description="Lists of users in each category")
    for category, users in user_categories.items():
        embed.add_field(name=category, value="\n".join(users) if users else "No users", inline=False)
    return embed

def move_user_to_category(user, category):
    # Remove the user from other categories if present
    for cat in user_categories:
        if user in user_categories[cat]:
            user_categories[cat].remove(user)

    # Add the user to the specified category
    user_categories[category].append(user)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='green', help='Add yourself to the green category')
async def join_green(ctx):
    user = ctx.message.author.display_name
    move_user_to_category(user, "Green")
    embed = await update_embed()
    print("green")
    await ctx.send(embed=embed)

@bot.command(name='yellow', help='Add yourself to the yellow category')
async def join_yellow(ctx):
    user = ctx.message.author.display_name
    move_user_to_category(user, "Yellow")
    embed = await update_embed()
    print("yellow")
    await ctx.send(embed=embed)

@bot.command(name='red', help='Add yourself to the red category')
async def join_red(ctx):
    user = ctx.message.author.display_name
    move_user_to_category(user, "Red")
    embed = await update_embed()
    print("red")
    await ctx.send(embed=embed)

@bot.command(name='blue', help='Add yourself to the blue category')
async def join_blue(ctx):
    user = ctx.message.author.display_name
    move_user_to_category(user, "Blue")
    embed = await update_embed()
    print("blue")
    await ctx.send(embed=embed)

# List of mom jokes
mom_jokes = [
    "Die Mutter von Fin ist so weise, wenn sie an den Strand geht, kommt das Meer zu ihr, um sie um Rat zu fragen!",
    "Warum hat die Mutter von Fin eine Leiter in die Bar gebracht? Sie hat gehört, dass die Getränke aufs Haus gehen!",
    "Wie nennt man die Mutter von Fin, wenn sie vor einem Computer sitzt? Data Mom!",
    "Die Mutter von Fin ist so stark, sie benutzt den Eiffelturm als Zahnstocher!",
    "Warum kann die Mutter von Fin nicht Schach spielen? Bei jedem Zug sagt sie: 'König mich!'",
    "Die Mutter von Fin ist so groß, wenn sie sich bückt, zeigt sie auf dem Radar!",
    "Wie verdient die Mutter von Fin ihren Lebensunterhalt? Sie verkauft Schatten!",
    "Warum trägt die Mutter von Fin eine Uhr auf jedem Arm? Eine ist für die Zeitzone, in der sie ist, die andere für die, in die sie passt!",
    "Die Mutter von Fin ist so pünktlich, sie kam gestern schon für ihren Termin morgen!",
    "Warum geht die Mutter von Fin nie zum Bowling? Sie wirft den Ball und die Erde dreht sich!",
    "Die Mutter von Fin ist so magisch, sie kann Lasagne in eine Pizza verwandeln, indem sie sie umdreht!",
    "Warum hat die Mutter von Fin den Job als Aufzugführerin verloren? Sie hat das Hochhaus in einen Bungalow verwandelt!",
    "Die Mutter von Fin ist so kreativ, sie kann aus einem Tropfen Wasser eine Eisbahn machen!",
    "Warum hat die Mutter von Fin eine Antenne auf dem Kopf? Sie empfängt Gedanken aus der Zukunft!",
    "Die Mutter von Fin ist so alt, sie hat ein Autogramm von Moses!",
    "Warum spielt die Mutter von Fin nie Verstecken? Weil, wenn sie sich versteckt, findet sie niemand mehr!",
    "Die Mutter von Fin ist so schnell, sie kann um die Welt rennen und sich selbst in den Rücken treten!",
    "Warum hat die Mutter von Fin einen Bagger im Garten? Um ihre Diätpillen auszugraben!",
    "Die Mutter von Fin ist so klug, sie kann mit einem Schachbrett Tetris spielen!",
    "Warum ist die Mutter von Fin immer in den Nachrichten? Weil sie so groß ist, sie passt nicht auf einen Bildschirm!"
]

@bot.command(name='fin', help='Tell a random mom joke')
async def tell_joke(ctx):
    joke = random.choice(mom_jokes)
    print("fin")
    await ctx.send(joke)

# Correctly register the error handler
@bot.event
async def on_command_error(ctx, error):
    print(f'An error occurred: {error}')

token = os.getenv('TOKEN')

bot.run(token)
