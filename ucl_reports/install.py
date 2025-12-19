import frappe

MODULE_NAME = "UCL Reports"
WORKSPACE_NAME = "UCL Reports"

REPORT_AR = "UCL Aged Debtors"
REPORT_AP = "UCL Aged Creditors"


def after_install():
    """
    Called automatically when the app is installed.
    Creates:
      - Module Def: UCL Reports
      - Workspace: UCL Reports (with Financial Reports section)
      - Two Script Reports
    """
    frappe.db.commit()  # make sure installation transaction is stable
    _ensure_module_def()
    _ensure_reports()
    _ensure_workspace()
    frappe.db.commit()


def _ensure_module_def():
    if frappe.db.exists("Module Def", MODULE_NAME):
        return

    doc = frappe.get_doc({
        "doctype": "Module Def",
        "module_name": MODULE_NAME,
        "app_name": "ucl_reports",
        "custom": 1
    })
    doc.insert(ignore_permissions=True)


def _ensure_reports():
    # Aged Debtors (AR)
    if not frappe.db.exists("Report", REPORT_AR):
        frappe.get_doc({
            "doctype": "Report",
            "report_name": REPORT_AR,
            "ref_doctype": "Sales Invoice",
            "report_type": "Script Report",
            "is_standard": "Yes",
            "module": MODULE_NAME
        }).insert(ignore_permissions=True)

    # Aged Creditors (AP)
    if not frappe.db.exists("Report", REPORT_AP):
        frappe.get_doc({
            "doctype": "Report",
            "report_name": REPORT_AP,
            "ref_doctype": "Purchase Invoice",
            "report_type": "Script Report",
            "is_standard": "Yes",
            "module": MODULE_NAME
        }).insert(ignore_permissions=True)


def _ensure_workspace():
    if frappe.db.exists("Workspace", WORKSPACE_NAME):
        return

    # Workspace "content" is JSON string.
    # We keep it simple: one section "Financial Reports" and two report shortcuts.
    content = [
        {"type": "header", "data": {"text": WORKSPACE_NAME, "level": 1}},
        {"type": "section", "data": {"label": "Financial Reports", "collapsible": 0}},
        {
            "type": "shortcut",
            "data": {
                "label": REPORT_AR,
                "type": "report",
                "link_to": REPORT_AR,
                "color": "blue",
                "icon": "report",
                "format": "{}"
            }
        },
        {
            "type": "shortcut",
            "data": {
                "label": REPORT_AP,
                "type": "report",
                "link_to": REPORT_AP,
                "color": "green",
                "icon": "report",
                "format": "{}"
            }
        }
    ]

    doc = frappe.get_doc({
        "doctype": "Workspace",
        "title": WORKSPACE_NAME,
        "module": MODULE_NAME,
        "label": WORKSPACE_NAME,
        "public": 1,
        "is_standard": 1,
        "content": frappe.as_json(content),
        "for_user": "",
        "sequence_id": 0
    })
    doc.insert(ignore_permissions=True)
