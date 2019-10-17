# Integration app for Momo API

Instructions

1. To install the app dependencies, Run >> pip install -r requirements.txt
2. Create  local_settings.py from the local_settings.example.py
3. Set the MOMO config details especially the MOMO_SUBSCRIPTION_KEY

4. Run command for migration >> python manage.py migrate
5. Run the prompt command using >> python manage.py create_momo_request
6. Enter the required details as prompted to create a MOMO request object and send a collection request

7. Run Command for updating momo requests >> python manage.py update_momo_requests //can be used on crontab