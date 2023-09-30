import datetime


before_date = datetime.datetime(2021, 8, 31, tzinfo=datetime.timezone.utc)
after_date = datetime.datetime(2021, 6, 25, tzinfo=datetime.timezone.utc)

oldest_date = datetime.datetime(2021, 6, 25, tzinfo=datetime.timezone.utc)
temp = before_date - oldest_date
print(oldest_date)
print(type(print(temp)))
print(temp)