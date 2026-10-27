STATUSES = ["pending", "pass", "fail"]
def valid_cases(data):
    if type(data) != list:
        return False
    seen = []
    for item in data:
        if type(item) != dict:
            return False
        if len(item) != 3 or "id" not in item or "title" not in item or "status" not in item:
            return False
        if type(item["id"]) != int or item["id"] <= 0:
            return False
        if item["id"] in seen:
            return False
        if type(item["title"]) != str or len(item["title"].strip()) < 5:
            return False
        if item["status"] not in STATUSES:
            return False
        seen.append(item["id"])
    return True
def add_case(items, title):
    title = title.strip()
    if len(title) < 5:
        return None
    max_id = 0
    for item in items:
        if item["id"] > max_id:
            max_id = item["id"]
    new_id = max_id + 1
    new_case = {"id": new_id, "title": title, "status": "pending"}
    items.append(new_case)
    return new_id
def set_result(items,case_id, status):
    status = status.strip().lower()
    if status not in STATUSES:
        return "invalid_status"
    for item in items:
        if item["id"] == case_id:
            if item["status"] == status:
                return "unchanged"
            return "updated"
    return "not_found"
def summarize(items):
    pending_count = 0
    pass_count = 0
    fail_count = 0
    for item in items:
        if item["status"] == "pending":
            pending_count += 1
        elif item["status"] == "pass":
            pass_count += 1
        elif item["status"] == "fail":
            fail_count += 1
    result = {
        "total": len(items),
        "pending": pending_count,
        "pass": pass_count,
        "fail": fail_count,
    }
    return result