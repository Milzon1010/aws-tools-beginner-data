import boto3
import datetime

def get_cost_and_usage():
    """
    Retrieves the unblended cost for the previous month using AWS Cost Explorer.
    """
    ce = boto3.client('ce')
    # Tentukan tanggal mulai dan akhir: periode bulan sebelumnya
    today = datetime.date.today()
    first_day_this_month = today.replace(day=1)
    last_month = first_day_this_month - datetime.timedelta(days=1)
    start_date = last_month.replace(day=1)
    end_date = first_day_this_month

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.isoformat(),
            'End': end_date.isoformat()
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )
    
    print("Cost Explorer Response:")
    print(response)
    return response

if __name__ == "__main__":
    get_cost_and_usage()
