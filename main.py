import teamup as tu
import google_sheets as gs

google_sheet_all = gs.fetch_emails_from_csv("exported_google_sheet.csv")
google_sheet_current = gs.fetch_emails_from_csv("current_google.csv")
teamup_emails = tu.fetch_emails_from_teamup_csv("teamup_bookings.csv")

# emails in Teamup that aren't in the Google Sheet
invalid_emails = teamup_emails - google_sheet_all - google_sheet_current

if invalid_emails:
    print("Invalid Emails:", invalid_emails)
else:
    print("OK: All emails are valid and match the Google Sheet.")