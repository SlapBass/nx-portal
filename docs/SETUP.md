# Setup Development Environment

## Suposed Platforms

- macOS

- Ubuntu-based Linux distribution

>> If you're Window user, please setup WSL.

## Recommended Toolchains

- **pipenv** is necessary. `requirements.txt` is no longer used.

- If you're using macOS, try **Postgre.app**. It is 

- If you're using Ubuntu, FreeBSD, install **PostgreSQL11**.


## Clone poject repository & run local server

After completed cloning project repository, run following commands to restore Python environment.

```shell
pipenv shell
pipenv install
pipenv install -d
```

NX Portal uses `mirage` development tool. You can run local server by running `mg s` instead of `python manage.py runserver`.
After lanched server, access [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

```shell
mg s
```