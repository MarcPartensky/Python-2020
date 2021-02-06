@commands.command()
    async def avatar(self, ctx, user: discord.Member = None):
        """Récuperer l'avatar de ..."""
        if user is None:
            user = ctx.message.author
        url_avatar = user.avatar_url_as(format='png')
        embed = discord.Embed(
            title='Avatar de : ' + user.name,
            url=user.avatar_url_as(format='png'),
            description=(f'[Voir en plus grand]'
            f"({url_avatar})")
        )
        embed.set_thumbnail(url=url_avatar)
        await ctx.send(embed=embed)
