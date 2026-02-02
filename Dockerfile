# pull official base uv image
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

RUN apt-get update && apt-get install -y \
    libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# setup non-root
RUN groupadd --system --gid 999 nonroot \
  && useradd --system --gid 999 --uid 999 --create-home nonroot

# set workdir
WORKDIR /app

#enable bytecode compilation
ENV UV_COMPILE_BYTCODE=1

# Copy from cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# omit developement dependencies
ENV UV_NO_DEV=1

# ensure tools are on path
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install project's dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project


# add the project source code and install
# installing seperatley optimizes layer caching
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

RUN mkdir -p /app/markdown /app/publihs && \
    chown -R nonroot:nonroot /app

# Place executables at the front of path
ENV PATH="/app/.venv/bin:$PATH"

# reset the entrypoint, don't invoke uv
ENTRYPOINT []

# use the non-root user to run app
USER nonroot

# run the app
CMD ["python", "src/main.py"]
