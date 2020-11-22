# ToDo Alert

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ronniesong0809/todo-alert/blob/master/LICENSE)

Copyright (c) 2020 Ronnie Song

`Creating alerts is a good way to monitor a service and ensure the SLOs are being met. `

This is a toy-level python script running outside of our [SRE ToDo App](http://35.197.22.173/home/). It could detect that the site is not reachable and then send an email to our team. 

## Setup and Run
Set Environment Variables, Replace TODO entries with your Gmail address and password.
```
$ export GMAIL_ADDRESS=TODO
$ export GMAIL_PASSWORD=TODO
```

Git clone, and install dependencies.
```
$ git clone https://github.com/ronniesong0809/todo-alert.git
$ cd todo-alert
$ pip install -r requirements.txt
```

Run
```
$ python run.py
```
or run in the background
```
$ nohup run.py &
```

## References

[Login credentials not working with Gmail SMTP](https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp)

[Less secure apps & your Google Account](https://support.google.com/accounts/answer/6010255)

## License

This program is licensed under the "MIT License". Please see the file [LICENSE]() in the source distribution of this software for license terms.