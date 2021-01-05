from django.core.management import BaseCommand
import requests
import json
import xlsxwriter


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Export task running!")

        headers = {'Content-Type': 'application/json'}
        page = 1

        url = f"http://127.0.0.1:8000/api/accounts_follower?page={page}"
        payload = {
            "min_followers": 50000,
            "country": 1,
            "items_count": 20000000
        }

        accs = requests.post(url, data=json.dumps(payload), headers=headers).json()["accounts"]

        workbook = xlsxwriter.Workbook('data/data.xlsx')
        worksheet = workbook.add_worksheet()

        row = 1

        for acc in accs:
            worksheet.write(row, 0, row)
            worksheet.write(row, 1, acc["username"])
            worksheet.write(row, 2, acc["name"])
            worksheet.write(row, 3, acc["followers"])
            worksheet.write(row, 4, "\n".join(acc["categories"]))

            row += 1

        workbook.close()
