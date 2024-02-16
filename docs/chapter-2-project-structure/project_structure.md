1. Project Structure. Consistent & predictable
   There are many ways to structure the project, but the best structure is a structure that is consistent, straightforward, and has no surprises.

If looking at the project structure doesn't give you an idea of what the project is about, then the structure might be unclear.
If you have to open packages to understand what modules are located in them, then your structure is unclear.
If the frequency and location of the files feels random, then your project structure is bad.
If looking at the module's location and its name doesn't give you an idea of what's inside it, then your structure is very bad.
Although the project structure, where we separate files by their type (e.g. api, crud, models, schemas) presented by @tiangolo is good for microservices or projects with fewer scopes, we couldn't fit it into our monolith with a lot of domains and modules. Structure that I found more scalable and evolvable is inspired by Netflix's Dispatch with some little modifications.

Reference

[fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async)

https://github.com/BCG-X-Official/agentkit
