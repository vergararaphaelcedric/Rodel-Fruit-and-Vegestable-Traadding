from django.urls import reverse, NoReverseMatch


def dashboard_ui(request):
    """Provide role-aware navigation data to dashboard templates."""

    if not request.user.is_authenticated:
        return {}

    user = request.user
    role = getattr(user, "role", "")

    sections = []

    # Main navigation
    main_items = [
        {
            "label": "Dashboard",
            "url": reverse(user.dashboard_url_name),
            "icon": "bi-speedometer2",
        },
    ]

    if user.has_perm("accounts.view_user"):
        main_items.append({
            "label": "User Management",
            "url": reverse("user-list"),
            "icon": "bi-people",
        })

    sections.append({
        "title": "MAIN MENU",
        "items": main_items,
    })

    # Business modules will be added when their pages and URLs exist.
    module_items = []

    if role == "employee":
      module_items.append({
        "label": "Requisitions",
        "url": reverse("requisition-create"),
        "icon": "bi-file-earmark-text",
        "disabled": False,
    })

    if role in {"inventory_staff", "manager", "employee",
                "purchasing_staff", "receiving_staff", "administrator"}:
        module_items.append({
            "label": "Inventory",
            "url": None,
            "icon": "bi-box-seam",
            "disabled": True,
        })

    if role == "purchasing_staff":
        module_items.append({
            "label": "Procurement",
            "url": None,
            "icon": "bi-cart",
            "disabled": True,
        })

    if role == "receiving_staff":
        module_items.append({
            "label": "Receiving",
            "url": None,
            "icon": "bi-truck",
            "disabled": True,
        })

    if module_items:
        sections.append({
            "title": "WORKSPACE",
            "items": module_items,
        })

    full_name = user.get_full_name().strip()
    display_name = full_name or user.username

    initials = "".join(
        part[0].upper()
        for part in display_name.split()
        if part
    )[:2]

    return {
        "nav_sections": sections,
        "ui_initials": initials or "U",
        "notification_count": 0,
        "notifications": [],
    }
