# Hegardt Backend

## Setup

1. Download Groovy 5: https://groovy.apache.org/download.html
2. Extract somewhere like `C:\Program Files\groovy-5.x.x`
3. Add to system environment variables:
   1. `GROOVY_HOME = C:\Program Files\groovy-5.0.0`
   2. Add `%GROOVY_HOME%\bin` to your `PATH`

## Administrate Postgres Database
First, install _Docker Desktop_.

Create .env file in the root with:

```dotenv
DB_USER=hegardt
DB_PASSWORD=hegardt
```

Then, from root, run:
```powershell
docker compose up postgres -d
```

We can wipe the volume and all data with 
```powershell
docker compose down postgres -v
```

## Micronaut 4.10.9 Documentation

- [User Guide](https://docs.micronaut.io/4.10.9/guide/index.html)
- [API Reference](https://docs.micronaut.io/4.10.9/api/index.html)
- [Configuration Reference](https://docs.micronaut.io/4.10.9/guide/configurationreference.html)
- [Micronaut Guides](https://guides.micronaut.io/index.html)
---

- [Shadow Gradle Plugin](https://gradleup.com/shadow/)
- [Micronaut Gradle Plugin documentation](https://micronaut-projects.github.io/micronaut-gradle-plugin/latest/)
## Feature serialization-jackson documentation

- [Micronaut Serialization Jackson Core documentation](https://micronaut-projects.github.io/micronaut-serialization/latest/guide/)


## Feature micronaut-aot documentation

- [Micronaut AOT documentation](https://micronaut-projects.github.io/micronaut-aot/latest/guide/)


