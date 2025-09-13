## ✍️ Create Migrations

### ➕ Create empty migration file:

```shell
alembic revision -m "migration message"
```

### ⚙️ Autogenerate migration from models:

```shell
alembic revision --autogenerate -m "Add new table"
```

---

## ⬆️ Apply Migrations

### ✅ Apply all new migrations:

```shell
alembic upgrade head
```

### ⬆️ Upgrade one revision:

```shell
alembic upgrade +1
```

### 📌 Upgrade to specific revision:

```shell
alembic upgrade <revision_id>
```

---

## ⬇️ Rollback / Downgrade

### 🔙 Roll back one revision:

```shell
alembic downgrade -1
```

### 🔄 Downgrade to specific revision:

```shell
alembic downgrade <revision_id>
```

### 💥 Reset everything:

```shell
alembic downgrade base
```

---

## 🔍 Debugging & Info

### 📍 Show current DB revision:

```shell
alembic current
```

### 📜 Show revision history:

```shell
alembic history
```

### 📎 Show full history (verbose):

```shell
alembic history --verbose
```
