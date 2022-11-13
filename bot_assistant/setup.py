from setuptools import setup, find_packages


setup(
    name="bot_assistant",
    version="0.0.1",
    autor="Vladislav Tumoschuk",
    entry_points={
        "console_scripts": ["bot-assistant=bot_assistant.bot_assistant:handler"],
    },
    packages=find_packages(),
    include_package_data=True,
    description="Bot assistant for phone book"
)