---
title: Deployment
subtitle: API Deployment
---

# Deployment

### Operating Environment

The API has two operating environments, configured trough the environment variable `ENVIRONMENT`.
Available options are `prod` and `dev`. 

!!! danger

    The `dev` environment should only be used for testing and development,
    as it may include endpoints that bypass security and authentication measures.
