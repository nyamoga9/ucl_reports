frappe.query_reports["UCL Aged Creditors"] = {
  filters: [
    {
      fieldname: "company",
      label: __("Company"),
      fieldtype: "Link",
      options: "Company",
      default: frappe.defaults.get_user_default("Company"),
      reqd: 1
    },
    {
      fieldname: "report_date",
      label: __("As Of Date"),
      fieldtype: "Date",
      default: frappe.datetime.get_today(),
      reqd: 1
    },
    {
      fieldname: "ageing_based_on",
      label: __("Ageing Based On"),
      fieldtype: "Select",
      options: ["Posting Date", "Due Date"],
      default: "Posting Date"
    },
    {
      fieldname: "range1",
      label: __("Range 1 (Days)"),
      fieldtype: "Int",
      default: 30
    },
    {
      fieldname: "range2",
      label: __("Range 2 (Days)"),
      fieldtype: "Int",
      default: 60
    },
    {
      fieldname: "range3",
      label: __("Range 3 (Days)"),
      fieldtype: "Int",
      default: 90
    },
    {
      fieldname: "range4",
      label: __("Range 4 (Days)"),
      fieldtype: "Int",
      default: 120
    }
  ]
};
