#### Docker up
```bash
docker compose up -d
```

#### Docker down
```bash
docker compose down
```

```bash
liquibase \
--changeLogFile=src/main/resources/db/changelog/1.0.0.xml \
--url=hibernate:nl.moukafih.demo.repository.entity?dialect=liquibase.ext.hibernate.database.HibernateGenericDialect \
--driver=liquibase.ext.hibernate.database.connection.HibernateDriver \
generateChangeLog
```
hibernate:spring:nl.moukafih.demo.repository.entity?dialect=org.hibernate.dialect.PostgreSQLDialect