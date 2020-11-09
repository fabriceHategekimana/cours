## ETU classrooms



| VERBE | URL                        | BODY                          | RETURN CODE   |
| ----- | -------------------------- | ----------------------------- | ------------- |
| GET   | /classrooms                | {name: analyse I}             | 200 (OK)      |
| GET   | /classrooms/contents       | {name: calcul.pdf}            | 200 (OK)      |
| POST  | /classrooms/contents       | {name: tp.zip, bin: AF34....} | 201 (CREATED) |
| GET   | /classrooms/ETU_conference | {}                            | 200 (OK)      |





## /classrooms

```json
[
    {
    id: 0,
	name: "analyse"
    sections: ["slides", "vidéos", "tps"],
	...
},
...
]
```



## /classrooms/contents

```json
{
	id: 0,
	name: "foo.txt",
    bin: "BlaBla"
}
```



## /classroom/ETU_conference

```json
{}
```

