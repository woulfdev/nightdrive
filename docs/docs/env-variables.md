# Environmant Variables

### Gerneral

| Variable                                                          | Default | Description                                              |
| :---------------------------------------------------------------- | :-----: | :------------------------------------------------------- |
| BASE_URL :fontawesome-solid-exclamation-circle:{title="required"} |         |                                                          |
| REQUIRE_SIGNUP_CODE                                               |  true   | Allow use sigup without token                            |
| SIGNUP_CODE_LIFETIME                                              |   24    | The time in hours a signup code is usbale                |
| EMAIL_REQUIRE_VERIFICATION                                        |  false  | Require users to click a varification link in an E-Mail. |
| ENVIRONMENT                                                       |  prod   |                                                          |

### Security

| Variable                                                            | Default | Description                        |
| :------------------------------------------------------------------ | :-----: | :--------------------------------- |
| ACCESS_TOKEN_EXPIRATION_HOURS                                       |   192   | The time in hours a token is valid |
| SECRET_KEY :fontawesome-solid-exclamation-circle:{title="required"} |         |                                    |

### Database

| Variable                                                                   |  Default   | Description |
| :------------------------------------------------------------------------- | :--------: | :---------- |
| POSTGRES_SERVER :fontawesome-solid-exclamation-circle:{title="required"}   |            |             |
| POSTGRES_PORT                                                              |    5432    |             |
| POSTGRES_USER :fontawesome-solid-exclamation-circle:{title="required"}     |            |             |
| POSTGRES_PASSWORD :fontawesome-solid-exclamation-circle:{title="required"} |            |             |
| POSTGRES_DB                                                                | nightdrive |             |

### E-Mail

SMTP server setup.

| Variable        | Default | Description |
| :-------------- | :-----: | :---------- |
| SMTP_TLS        |  true   |             |
| SMTP_SSL        |  false  |             |
| SMTP_PORT       |   587   |             |
| SMTP_HOST       |         |             |
| SMTP_USER       |         |             |
| SMTP_PASSWORD   |         |             |
| SMTP_FROM_EMAIL |         |             |
| SMTP_FROM_NAME  |         |             |
