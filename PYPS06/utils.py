import datetime

CATEGORIES = ["Programming", "Database", "Networking", "AI", "Mathematics", "Literature", "Science"]
LOAN_DAYS = 14
FINE_PER_DAY = 5


def load_records(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_records(filename, records):
    with open(filename, "w") as f:
        for record in records:
            f.write(record + "\n")


def get_today():
    return datetime.date.today().strftime("%Y-%m-%d")


def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def get_next_id(records, prefix):
    max_num = 0
    for record in records:
        parts = record.split(",")
        rid = parts[0].strip()
        if rid.startswith(prefix):
            try:
                num = int(rid[len(prefix):])
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
    return f"{prefix}{max_num + 1:03d}"
