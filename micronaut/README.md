# Hegardt Backend

## Setup

1. Download Groovy 5: <https://groovy.apache.org/download.html>
2. Extract somewhere like `C:\Program Files\groovy-5.x.x`
3. Add to system environment variables:
   1. `GROOVY_HOME = C:\Program Files\groovy-5.0.0`
   2. Add `%GROOVY_HOME%\bin` to your `PATH`

### Administrate Postgres database with Docker

First, install _Docker Desktop_.

Create a .env in the root /Hegardt with the following values:

```dotenv
DB_USER=hegardt
DB_PASSWORD=hegardt
GITHUB_REPOSITORY=zorobay/hegardt
```

Then, from root, run:

```powershell
docker compose up postgres -d
```

We can wipe the volume and all data with

```powershell
docker compose down postgres -v
```

### Reset PROD database if seed files are updated

1. SSH into the server
2. `cd /root/Hegardt`
3. Check running volumes with `docker volume ls`
4. Take a backup of the database with `docker compose exec postgres pg_dump -U <db_user> <db_name> > ~/hegardt_backup_$(date +%Y%m%d).sql`
5. Stop everything and remove the volume:
   ```shell
    docker compose down
    docker volume rm <the_postgres_volume_name>
   ```
6. Run everything again with `docker compose up -d --remove-orphans`. The flyway migrations should be automatically applied.
7. Check logs with `docker logs --tail=200 hegardt-backend`

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
