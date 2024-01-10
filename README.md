Questa è una repo in cui è strutturato un template focalizzato a costruire il backend di un applicazione modulare e scalabile utilizzando FastAPI e sqlAlchemy con focus sull'accesso ai dati da parte di vari utenti

Al momento non consideriamo il service layer aggiuntivo ma gestiamo direttamente nei routes

It is feasible to use a repository-service pattern in some complex FastAPI applications through DI. The repository-service pattern is responsible for the creation of the repository layer of the application, which manages the Creation, Reading, Updates, and Deletion (CRUD) of data source. A repository layer requires data models that depict the table schemas of a collection or database. The repository layer needs the service layer to establish a connection with other parts of the application. The service layer operates like a business layer, where the data sources and business processes meet to derive all the necessary objects needed by the REST API. The communication between the repository and service layers can only be possible by creating injectables.

With the power of DI, we have created an online recipe system with an organized set of models, repository, and service layers. The project structure shown in Figure 3.3 is quite different from the previous prototypes because of the additional layers, but it still has main.py and all the packages and modules with their respective APIRouter.

FastAPI allows you to build independent sub-applications inside the main application.

Mounting the submodules
All the FastAPI decorators of each sub-application must be mounted in the main.py component of the top-level application for them to be accessed at runtime. The mount() function is invoked by the FastAPI decorator object of the top-level application, which adds all FastAPI instances of the sub-applications into the gateway application (main.py) and maps each with its corresponding URL context.

Creating a common gateway
It will be easier if we use the URL of the main application to manage the requests and redirect users to any of the three sub-applications. The main application can stand as a pseudo-reverse proxy or an entry point for user requests, which will always redirect user requests to any of the desired sub-applications. This kind of approach is based on a design pattern called API Gateway. Now, let us explore how we can apply this design to manage independent microservices mounted onto the main application using a workaround.

There are so many solutions when it comes to implementing this gateway endpoint, and among them is having a simple REST API service in the top-level application with an integer path parameter that will identify the ID parameter of the microservice.

Managing a microservice’s configuration details
So far, this chapter has provided us with some popular design patterns and strategies that can give us a kickstart on how to provide our FastAPI microservices with the best structures and architecture. This time, let us explore how the FastAPI framework supports storing, assigning, and reading configuration details to mounted microservice applications such as database credentials, networking configuration data, application server information, and deployment details. First, we need to install python-dotenv using pip:

pip install python-dotenv

All of these settings are values that are external to the implementation of the microservice applications. Instead of hardcoding them into the code as variable data, usually, we store them in the env, property, or INI files. However, challenges arise when assigning these settings to different microservices.

Frameworks that support the externalized configuration design pattern have an internal processing feature that fetches environment variables or settings without requiring additional parsing or decoding techniques. For instance, the FastAPI framework has built-in support for externalized settings through pydantic’s BaseSettings class.

Storing settings in the properties file
Another option is to store all these settings inside a physical file with an extension of .env, .properties, or .ini. For instance, this project has the erp_settings.properties file found in the /config folder

Setting up the database connection

To connect to any database, SQLAlchemy requires an engine that manages the connection pooling and the installed dialect. The create_engine() function from the sqlalchemy module is the source of the engine object. But to successfully derive it, create_engine() requires a database URL string to be configured. This URL string contains the database name, the database API driver, the account credentials, the IP address of the database server, and its port.

Initializing the session factory
All CRUD transactions in SQLAlchemy are driven by sessions. Each session manages a group of database "writes" and "reads," and it checks whether to execute them or not. For instance, it maintains a group of inserted, updated, and deleted objects, checks whether the changes are valid, and then coordinates with the SQLAlchemy core to pursue the changes to the database if all transactions have been validated. It follows the behavior of the Unit of Work design pattern. SQLAlchemy relies on sessions for data consistency and integrity.

from sqlalchemy.orm import sessionmaker
engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False,
autoflush=False, bind=engine)
Apart from engine binding, we also need to set the session’s autocommit property to False to impose commit() and rollback() transactions. The application should be the one to flush all changes to the database, so we need to set its autoflush feature to False as well.

Applications can create more than one session through the SessionFactory() call, but having one session per APIRouter is recommended.

Defining the Base class
Next, we need to set up the Base class, which is crucial in mapping model classes to database tables. Although SQLAlchemy can create tables at runtime, we opted to utilize an existing schema definition for our prototype. Now, this Base class must be subclassed by the model classes so that the mapping to the tables will happen once the server starts. The following script shows how straightforward it is to set up this component:

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Invoking the declarative_base() function is the easiest way of creating the Base class rather than creating registry() to call generate_base(), which can also provide us with the Base class.

Note that all these configurations are part of the /db_config/sqlalchemy_connect.py module of the prototype. They are bundled into one module since they are crucial in building the SQLAlchemy repository. But before we implement the CRUD transactions, we need to create the model layer using the Base class.

Implementing the repository layer
In the SQLAlchemy ORM, creating the repository layer requires the model classes and a Session object. The Session object, derived from the SessionFactory()directive, establishes all the communication to the database and manages all the model objects before the commit() or rollback() transaction. When it comes to the queries, the Session entity stores the result set of records in a data structure called an identity map, which maintains the unique identity of each data record using the primary keys.

All repository transactions are stateless, which means the session is automatically closed after loading the model objects for insert, update, and delete transactions when the database issues a commit() or rollback() operation. We import the Session class from the sqlalchemy.orm module.

---

lancia con il comando

uvicorn app.main:app --reload
