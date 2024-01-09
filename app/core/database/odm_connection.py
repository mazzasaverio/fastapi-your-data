# # app/core/database/odm_connection.py
# from beanie import init_beanie
# from motor.motor_asyncio import AsyncIOMotorClient
# from app.config.settings import settings
# from app.models.nosql_models.docs_categ import DocsNameCateg


# async def init_odm():
#     client = AsyncIOMotorClient(settings.mongodb_url)
#     database = client.get_default_database()
#     await init_beanie(
#         database, document_models=[DocsNameCateg]
#     )  # List all Beanie documents
