# Atlas Failover
This is a demo script for testing MongoDB Atlas failover.

## Dependencies
To run this script, you need python 2.7 and the following libraries installed:
```
sudo pip install dnspython pymongo faker
```
## Set the connection string
The connection string is hard-coded in `replica_failover.py`. Edit it to anything you want.

## Run the application
The application would insert a fake document every 1 second. And print the primary node hostname and the email inserted.
```
python __main__.py
```
If you want to test `retryWrites` (which automatically retry writes when fails), simply add command line args `true`:
```
python __main__.py true
```

## Test failover
In Atlas dashboard, find the button `...`. In the dropdown menu, you'll see "Test Failover".

Enjoy!
