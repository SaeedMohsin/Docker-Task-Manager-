#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BACKUP_DIR="$PROJECT_DIR/backups"

mkdir -p "$BACKUP_DIR"

BACKUP_FILE="$BACKUP_DIR/taskmanager_$(date +%Y-%m-%d_%H-%M-%S).sql"

echo "Starting PostgreSQL backup..."

cd "$PROJECT_DIR"

docker compose exec -T db sh -c \
'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' > "$BACKUP_FILE"

echo "Backup completed successfully!"
echo "Backup file: $BACKUP_FILE"
