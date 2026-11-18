
"""Single source of truth for roles and permissions."""

ROLE_GROUP_NAMES = {
    "administrator": "Administrator",
    "employee": "Employee",
    "manager": "Manager",
    "inventory_staff": "Inventory Staff",
    "purchasing_staff": "Purchasing Staff",
    "receiving_staff": "Receiving Staff",
}

DASHBOARD_URLS = {
    "administrator": "dashboard-administrator",
    "employee": "dashboard-employee",
    "manager": "dashboard-manager",
    "inventory_staff": "dashboard-inventory",
    "purchasing_staff": "dashboard-purchasing",
    "receiving_staff": "dashboard-receiving",
}

ROLE_SUMMARY = {
    "administrator": "Manage user accounts, roles and departments. Read-only access to inventory and requisitions.",
    "employee": "Create requisitions and track your own requests. View inventory items.",
    "manager": "Review and approve or reject submitted requisitions. View inventory.",
    "inventory_staff": "Maintain inventory items and categories, and record fulfilment of requisition lines.",
    "purchasing_staff": "View requisitions and stock levels to plan purchases. Procurement permissions are added with that module.",
    "receiving_staff": "View inventory. Receiving permissions are added with that module.",
}


def perms(app, model, *actions):
    return [f"{app}.{action}_{model}" for action in actions]


ROLE_PERMISSIONS = {
    "administrator": [
        *perms("accounts", "user", "add", "change", "view"),
        *perms("accounts", "department", "add", "change", "view"),
        *perms("inventory", "inventoryitem", "view"),
        *perms("inventory", "itemcategory", "view"),
        *perms("requisitions", "requisition", "view"),
        *perms("requisitions", "requisitionitem", "view"),
        *perms("requisitions", "statushistory", "view"),
        *perms("requisitions", "approvalhistory", "view"),
    ],
    "employee": [
        *perms("requisitions", "requisition", "add", "change", "view"),
        *perms("requisitions", "requisitionitem", "add", "change", "view"),
        *perms("inventory", "inventoryitem", "view"),
        *perms("inventory", "itemcategory", "view"),
    ],
    "manager": [
        *perms("requisitions", "requisition", "view"),
        "requisitions.approve_requisition",
        *perms("requisitions", "requisitionitem", "view"),
        *perms("requisitions", "statushistory", "view"),
        *perms("requisitions", "approvalhistory", "view"),
        *perms("inventory", "inventoryitem", "view"),
        *perms("inventory", "itemcategory", "view"),
        *perms("accounts", "department", "view"),
    ],
    "inventory_staff": [
        *perms("inventory", "inventoryitem", "add", "change", "view"),
        *perms("inventory", "itemcategory", "add", "change", "view"),
        *perms("requisitions", "requisition", "view"),
        *perms("requisitions", "requisitionitem", "change", "view"),
    ],
    "purchasing_staff": [
        *perms("inventory", "inventoryitem", "view"),
        *perms("inventory", "itemcategory", "view"),
        *perms("requisitions", "requisition", "view"),
        *perms("requisitions", "requisitionitem", "view"),
    ],
    "receiving_staff": [
        *perms("inventory", "inventoryitem", "view"),
        *perms("inventory", "itemcategory", "view"),
    ],
}
