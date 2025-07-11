command_file_name = r"data\CommandScripts.xlsx"
command_sheet_name = "CommandScripts"

log_file_name = r"data\TestLogs.xlsx"
log_sheet_name = "Logs"

get_current_url_in_action_method = "current_url"
ga4_analytics_identifier = "collect?"  #"collect?v=2"
google_analytics_identifier = "www.google-analytics.com/"
unsecure_protocol = "http://"
secure_protocol = "https://"
dash_length = 120
media_tags = [
    ["tiktok", "sdkid"],
    ["facebook", "ev", "id"],
    ["snapchat", "pid"],
    ["pinterest", "tid", "dep"]
]

# This array is for testing WCAG and ADA compliance
# The first item of each array is the element, items without <> surrounding them are parameters
# items with <> surrounding them are child elements that must be present for compliance
# but for the "a" element, the items are text that should not be present as the link text.
wcag_ada_array = [
    ["img","alt", "src"],
    ["button", "aria-label"],
    ["input", "id", "name", "type"],
    ["label", "for"],
    ["textarea", "id", "name"],
    ["nav", "aria-label"],
    ["section", "aria-label"],
    ["form", "aria-label"],
    ["table", "<caption>"],
    ["th", "scope"],
    ["iframe", "src", "title"],
    ["svg", "role", "aria-label", "<title>"],
    ["video", "<source>"],
    ["source", "src", "type"],
    ["track", "kind", "src", "srclang", "label"],
    ["a", "click", "here"]
]
connection_string_template = f"mssql+pyodbc://@*server*/*database*" \
    "?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"

terminal_color_red = "\033[31m"
terminal_color_green = "\033[32m"
terminal_color_reset = "\033[0m"
terminal_color_blue = "\033[34m"

# terminal_colors = [
#     "red", "\033[31m"
#     "green", "\033[32m"
#     "yellow", "\033[33m"
#     "blue", "\033[34m"
#     "reset", "\033[0m"
# ]
