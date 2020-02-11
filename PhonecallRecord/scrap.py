for i in range(len(log['events'])):
    if log['events'][i][type] == 'call':
        billing_date = datetime.datetime.strptime(log['events'][i]['time'],
                                                  "%Y-%m-%d %H:%M:%S")
        billing_month = billing_date.month
        billing_year = billing_date.year
        new_month(customer_list, billing_month, billing_year)
        call = Call(log['events'][i]['src_number'], log['events'][i]
        ['des_number'], billing_date, log['events'][i]['duration'],
                    log['events'][i]['src_loc'], log['events'][i]['des_loc'])

# start recording the bills from this date
# Note: uncomment the following lines when you're ready to implement this


for event_data in log['events']:
    billing_date.month
