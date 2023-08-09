from marvin import AIApplication
from marvin_recipes.tools.chroma import MultiQueryChroma
from prefect import flow


knowledge_bot = AIApplication(
    name="knowledge bot",
    description="suggests resources based on a user's introduction - provide links",
    tools=[MultiQueryChroma(description="research Prefect topics", client_type="base")],
)


@flow
async def suggest_resources(introduction_message: str):
    return await knowledge_bot.run(introduction_message)


if __name__ == "__main__":
    import asyncio
    import marvin

    marvin.settings.log_level = "DEBUG"

    result = asyncio.run(
        suggest_resources(
            introduction_message="Hi, I'm a new Prefect user and I'm interested in prefect blocks"  # noqa: E501
        )
    )

    print(result)
