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

@bot.command(name='reset', help='Reset all categories')
async def reset(ctx):
    for category in user_categories:
        user_categories[category].clear()
    embed = await update_embed()
    await ctx.send(embed=embed)


# Correctly register the error handler
@bot.event
async def on_command_error(ctx, error):
    print(f'An error occurred: {error}')

token = os.getenv('TOKEN')

bot.run(token)
