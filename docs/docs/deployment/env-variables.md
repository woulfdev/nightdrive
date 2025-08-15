---
icon: material/variable
description: Overview and explanation of enviroment variables.
---

# Environmant Variables

### Gerneral

| Variable                                                          | Description                                                                                                                |  Default  | Container |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------: | :-------- |
| BASE_URL :fontawesome-solid-exclamation-circle:{title="required"} |                                                                                                                            |           |           |
| REQUIRE_SIGNUP_CODE                                               | Require users to provide a code to sign up                                                                                 |  `True`   | api       |
| SIGNUP_CODE_LIFETIME                                              | The time in hours a signup code is usable                                                                                  |   `24`    | api       |
| EMAIL_REQUIRE_VERIFICATION                                        | Require users to click a varification link in an E-Mail                                                                    |  `False`  | api       |
| ENVIRONMENT                                                       | Operating environment either `prod` or `dev`                                                                               |  `prod`   | api       |
| LOGGING_LEVEL                                                     |                                                                                                                            |  `INFO`   | api       |
| MESSAGE_OF_THE_DAY                                                | Message to be displayed on login or signup screen                                                                          |           | api       |
| TIME_ZONE                                                         | Time zone identifier from this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List){:target="_blank"} | `Etc/UTC` |           |


### Security

| Variable                                                            | Description                        | Default | Container |
| :------------------------------------------------------------------ | :--------------------------------- | :-----: | :-------- |
| ACCESS_TOKEN_EXPIRATION_HOURS                                       | The time in hours a token is valid |  `192`  | api       |
| SECRET_KEY :fontawesome-solid-exclamation-circle:{title="required"} | Used to generate JWT               |         | api       |

### Passwords

Password requirement settings.

| Variable                        | Description                                                                      | Default | Container |
| :------------------------------ | :------------------------------------------------------------------------------- | :-----: | :-------- |
| PASSWORD_MIN_LENGTH             | Minimum password length (can't be set `<8`)                                      |  `12`   | api       |
| PASSWORD_REQUIRE_NUMBERS        | Require passwords to include numbers `0-9`                                       | `True`  | api       |
| PASSWORD_REQUIRE_UPER_LOWERCASE | Require password to include upper and lowercase letters `a-z`, `A-Z`             | `True`  | api       |
| PASSWORD_REQUIRE_SYMBOLS        | Require password to include special characters `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/` | `True`  | api       |

### Database

PostgreSQL server connection.

| Variable                                                                   | Description                      |   Default    | Container |
| :------------------------------------------------------------------------- | :------------------------------- | :----------: | :-------- |
| POSTGRES_SERVER :fontawesome-solid-exclamation-circle:{title="required"}   | Postgres database server address |              |           |
| POSTGRES_PORT                                                              | Postgres database port           |    `5432`    | db, api   |
| POSTGRES_USER                                                              | Postgres database user           | `nightdrive` | db, api   |
| POSTGRES_PASSWORD :fontawesome-solid-exclamation-circle:{title="required"} | Postgres database password       |              | db, api   |
| POSTGRES_DB                                                                | Postgres database name           | `nightdrive` | db, api   |

### E-Mail

SMTP server setup.

| Variable        | Description             |   Default    | Container |
| :-------------- | :---------------------- | :----------: | :-------- |
| SMTP_AUTH_TYPE  | Options: `TLS` or `SSL` |    `TLS`     |           |
| SMTP_PORT       |                         |    `587`     |           |
| SMTP_HOST       |                         |              |           |
| SMTP_USER       |                         | `nightdrive` |           |
| SMTP_PASSWORD   |                         |              |           |
| SMTP_FROM_EMAIL |                         |              |           |
| SMTP_FROM_NAME  |                         | `NightDrive` |           |
