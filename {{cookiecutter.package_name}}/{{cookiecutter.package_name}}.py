from typing import Literal

import discord
from redbot.core import commands, Config
from redbot.core.bot import Red

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

_config_structure = {
    "global": {},
    "user": {},
    "channel": {},
    "guild": {},
    "member": {},
}


class {{ cookiecutter.cog_name }}(commands.Cog):
    """
    {{ cookiecutter.short }}
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            {{ cookiecutter.conf_id }},
            True
        )
        for key, value in _config_structure.items():
            getattr(self.config, f"register_{key}")(**value)

    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int):
        """This cog does not store any data"""
        return
