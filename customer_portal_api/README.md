# Customer Portal API

An independent consumer/admin backend service that reuses the existing repository's platform registration kernel, platform metadata, task runtime, account assets, proxy, and system capabilities.

## Implemented Capabilities

- Authentication: login, refresh token, logout, current user
- Consumer endpoints:
  - `GET /api/app/platforms`
  - `GET /api/app/config/options`
  - `GET /api/app/products`
  - `POST /api/app/tasks/register`
  - `GET /api/app/tasks`
  - `GET /api/app/tasks/{task_id}`
  - `GET /api/app/tasks/{task_id}/events`
  - `GET /api/app/tasks/{task_id}/logs/stream`
  - `GET /api/app/orders`
  - `POST /api/app/orders`
  - `GET /api/app/orders/{order_no}`
  - `POST /api/app/payments/{order_no}/submit`
  - `GET /api/app/subscriptions`
  - `GET /api/app/profile`
  - `PATCH /api/app/profile`
- Admin endpoints:
  - Users, roles, permissions, platform authorization, product catalog
  - Platforms, config, registration tasks, task queries, task logs
  - Accounts, platform actions, proxies, Solver status
- Payment endpoints:
  - `POST /api/payment/callback/{channel_code}`

## Directory Structure

```text
customer_portal_api/
├── app/
│   ├── routers/
│   ├── services/
│   ├── bootstrap.py
│   ├── config.py
│   ├── db.py
│   ├── deps.py
│   ├── models.py
│   └── security.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── main.py
```

## Local Development

### 1. Install Dependencies

Run from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you prefer to install only the new project path:

```bash
pip install -r customer_portal_api/requirements.txt
```

### 2. Configure Environment Variables

Copy the environment variable template:

```bash
cp customer_portal_api/.env.example customer_portal_api/.env
```

Common variables:

- `PORTAL_JWT_SECRET`
- `PORTAL_ADMIN_USERNAME`
- `PORTAL_ADMIN_PASSWORD`
- `PORTAL_ADMIN_EMAIL`
- `PORTAL_START_SOLVER`
- `ACCOUNT_MANAGER_DATABASE_URL`

### 3. Start the Service

Run from the repository root:

```bash
source .venv/bin/activate
export $(grep -v '^#' customer_portal_api/.env | xargs)
python -m uvicorn customer_portal_api.main:app --host 0.0.0.0 --port 8100 --reload
```

API documentation:

- Swagger UI: `http://127.0.0.1:8100/docs`
- OpenAPI JSON: `http://127.0.0.1:8100/openapi.json`

Default admin credentials:

- Username: `admin`
- Password: `admin123456`

On first startup, the admin account is automatically written to the database.

## Docker Deployment

Run from the repository root:

```bash
docker compose -f customer_portal_api/docker-compose.yml up --build
```

Service listens on:

- `http://127.0.0.1:8100`

## Design Notes

- The new project reuses the existing repository's platform registration and task execution kernel without reimplementing platform plugin logic
- The new project's own tables (users, refresh tokens, platform authorization, orders, subscriptions, task ownership) share the same SQLite database with existing business tables
- The consumer registration endpoint creates real registration tasks, and the task ownership table restricts users to only viewing their own tasks
- The payment pipeline includes product seeding, order placement, payment submission, payment callback, subscription activation, and platform registration permission enabling
