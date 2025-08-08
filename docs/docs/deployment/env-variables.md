---
icon: material/variable
description: Overview and explanation of enviroment variables.
---

# Environmant Variables

### Gerneral

| Variable                                                          | Default | Description                                                                                                                |
| :---------------------------------------------------------------- | :-----: | :------------------------------------------------------------------------------------------------------------------------- |
| BASE_URL :fontawesome-solid-exclamation-circle:{title="required"} |         |                                                                                                                            |
| REQUIRE_SIGNUP_CODE                                               |  true   | Require users to provide a code to sign up                                                                                 |
| SIGNUP_CODE_LIFETIME                                              |   24    | The time in hours a signup code is usable                                                                                  |
| EMAIL_REQUIRE_VERIFICATION                                        |  false  | Require users to click a varification link in an E-Mail                                                                    |
| ENVIRONMENT                                                       |  prod   | Operating environment either prod or dev                                                                                   |
| MESSAGE_OF_THE_DAY                                                |  None   | Message to be displayed on login or signup screen                                                                          |
| TIME_ZONE                                                         | Etc/UTC | Time zone identifier from this [list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List){:target="_blank"} |


### Security

| Variable                                                            | Default | Description                        |
| :------------------------------------------------------------------ | :-----: | :--------------------------------- |
| ACCESS_TOKEN_EXPIRATION_HOURS                                       |   192   | The time in hours a token is valid |
| SECRET_KEY :fontawesome-solid-exclamation-circle:{title="required"} |         | Used to generate JWT               |

### Passwords

Password requirement settings.

| Variable                        | Default | Description                                                                      |
| :------------------------------ | :-----: | :------------------------------------------------------------------------------- |
| PASSWORD_MIN_LENGTH             |   12    | Minimum password length (can't be set `<8`)                                      |
| PASSWORD_REQUIRE_NUMBERS        |  True   | Require passwords to include numbers `0-9`                                       |
| PASSWORD_REQUIRE_UPER_LOWERCASE |  True   | Require password to include upper and lowercase letters `a-z`, `A-Z`             |
| PASSWORD_REQUIRE_SYMBOLS        |  True   | Require password to include special characters `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/` |

### Database

PostgreSQL server connection.

| Variable                                                                   |  Default   | Description                      |
| :------------------------------------------------------------------------- | :--------: | :------------------------------- |
| POSTGRES_SERVER :fontawesome-solid-exclamation-circle:{title="required"}   |            | Postgres database server address |
| POSTGRES_PORT                                                              |    5432    | Postgres database port           |
| POSTGRES_USER                                                              | nightdrive | Postgres database user           |
| POSTGRES_PASSWORD :fontawesome-solid-exclamation-circle:{title="required"} |            | Postgres database password       |
| POSTGRES_DB                                                                | nightdrive | Postgres database name           |

### E-Mail

SMTP server setup.

| Variable        |  Default   | Description             |
| :-------------- | :--------: | :---------------------- |
| SMTP_AUTH_TYPE  |    TLS     | Options: `TLS` or `SSL` |
| SMTP_PORT       |    587     |                         |
| SMTP_HOST       |            |                         |
| SMTP_USER       | nightdrive |                         |
| SMTP_PASSWORD   |            |                         |
| SMTP_FROM_EMAIL |            |                         |
| SMTP_FROM_NAME  | NightDrive |                         |
