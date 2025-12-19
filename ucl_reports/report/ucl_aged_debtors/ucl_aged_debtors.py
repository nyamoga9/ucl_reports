import frappe

def execute(filters=None):
    filters = frappe._dict(filters or {})

    company = filters.get("company") or frappe.defaults.get_user_default("Company")
    report_date = filters.get("report_date") or frappe.utils.today()

    erpnext_filters = frappe._dict({
        "company": company,
        "report_date": report_date,
        "ageing_based_on": filters.get("ageing_based_on") or "Posting Date",
        "range1": int(filters.get("range1") or 30),
        "range2": int(filters.get("range2") or 60),
        "range3": int(filters.get("range3") or 90),
        "range4": int(filters.get("range4") or 120),
        "party_type": "Customer",
        "group_by_party": 1,
        "show_future_payments": 0,
        "based_on_payment_terms": 0,
    })

    # Use ERPNext's official AR ageing logic
    from erpnext.accounts.report.accounts_receivable.accounts_receivable import execute as ar_execute
    columns, data, message, chart, report_summary = ar_execute(erpnext_filters)

    return columns, data
