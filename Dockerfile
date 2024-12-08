FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.5.7 /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen --no-dev
RUN chmod a+x boot.sh
ENV FLASK_APP=microblog.py

# Set up entry point to run the app
EXPOSE 8080
ENTRYPOINT ["./boot.sh"]