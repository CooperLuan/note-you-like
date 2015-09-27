# Schema

- `user`
- `user_notes`
- `url_response_cache`
- `user_feedback`

## user

保存用户信息

```js
{
    _id: ObjectId(),
    nickname: "",
    email: "",
    salt: "",
    hash_method: "",
    passwd: "",
}
```

## user_notes

保存用户笔记信息

```js
{
    _id: ObjectId(),
    url: "",
    md_text: "",
    time: "2015-09-01 09:00:08",
    update_time: "2015-09-01 10:09:01",
}
```

## url_response_cache

```js
{
    _id: ObjectId(),
    url: "",
    body: "<html></html>",
    timestamp: 140109839071,
    datetime: "2015-09-01 20:00:09",
    status: 1,      // 1/-1
}
```

## user_feedback

保存用户的反馈纪录

```js
{
    _id: ObjectId(),
    user: ObjectId(),
    issue_type: "url",  // url
    issue_body: {
        url: "",
    },
}
```
