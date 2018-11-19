# modern_health_api

All you gotta do is 
`git clone https://github.com/aircert/modern_health_api.git`
`cd modern_health_api`
`make`

### Admin credentials

```
username: admin
password: admin
```

### Documentation URLS

- http://localhost:8000/programs
- http://localhost:8000/weeks
- http://localhost:8000/pages

### Reminder

- Pages must be created prior to Weeks.
- Weeks must be created prior to Programs.

### Steps to create pages

1) visit (http://localhost:8000/pages)

2) Enter into Raw Data / Content for Page 1

```
{
    "name": "Page 1",
    "audio": "https://google.com/audio",
    "video": "https://google.com/video",
    "article": "https://google.com/article",
    "question": "https://google.com/question",
    "form": "https://google.com/form"
}
```

3) Enter into Raw Data / Content for Page 2

```
{
    "name": "Page 2",
    "audio": "https://google.com/audio",
    "video": "https://google.com/video",
    "article": "https://google.com/article",
    "question": "https://google.com/question",
    "form": "https://google.com/form"
}
```

### Steps to create weeks 

1) visit (http://localhost:8000/weeks)

2) Enter into Raw Data / Content for Week 1

```
{
    "name": "Week 1",
    "pages": [1,2]
}
```

3) Enter into Raw Data / Content for Week 2

```
{
    "name": "Week 2",
    "pages": [1,2]
}
```

### Steps to create programs

1) visit (http://localhost:8000/programs)

2) Enter into Raw Data / Content for Program 1

```
{
    "name": "Program 1",
    "weeks": [1,2]
}
```

### Steps to update a model

visit (http://localhost:8000/<model>/:id): http://localhost:8000/pages/1

Link to screencast: https://youtu.be/eAOL0tKhXJY
