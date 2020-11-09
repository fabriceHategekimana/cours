



## TD7 Rest API

##### Oetske Leroux, Christina Nguyen, Mahya Daqiqui, Fabrice Hategekimana



| VERBE  | URL                        | BODY                                      | RETURN CODE   |
| ------ | -------------------------- | ----------------------------------------- | ------------- |
| GET    | /classrooms                | {name: "analyse I"}                       | 200 (OK)      |
| GET    | /classrooms/contents       | {name: "calcul.pdf"}                      | 200 (OK)      |
| POST   | /classrooms/contents       | {name: "tp.zip", bin: "AF34...."}         | 201 (Created) |
| GET    | /classrooms/etu_conference | {classroom_name: "analyse I"}             | 200 (OK)      |
| GET    | /store                     | {name: "FacultyLaw"}                      | 200 (OK)      |
| GET    | /store/facultylaw          | {name: "Droit_penal"}                     | 200 (OK)      |
| POST   | /store/facultylaw          | {name: "nom_du_produit"}                  | 201 (Created) |
| DELETE | /store/facultylaw          | {name: "Objet_vendre"}                    | 200 (OK)      |
| GET    | /network                   | {name: "ETU-Network"}                     | 200 (OK)      |
| GET    | /network/content           | {name: "thread"}                          | 201 (Created) |
| GET    | /network/id_person         | {name: "User"}                            | 200 (OK)      |
| POST   | /network/id_post           | {id_wall: WallUser { id_post: idPostN}}   | 201 (OK)      |
| GET    | /messenger                 | {}                                        | 200 (OK)      |
| POST   | /messenger                 | {}                                        | 201 (Created) |
| POST   | /messenger                 | {content: "Hello...",  reciever_id: 2345} | 200 (OK)      |





## /Classrooms

```json
{
    id: 0,
	name: "analyse"
    sections: [
        {
        	name: "slides",
        	contents_id: [3, 238, ...]
        },
     	{
           name: "vidéo",
            ...
        },
        ...
            ],
	...
}
```



## /classrooms/contents

```json
{
	id: 0,
	name: "foo.txt",
    bin: "315FABBC..."
}
```



## /classroom/ETU_conference

```json
{
    id: 0,
    link: "//afles....."
}
```



## /store

```json
{
	id: 0,
    name: "FacultyLaw",
    ...
	
}
```



##  /store/(faculty)

```json
{
	id: 0,
	name: "Droit pénal",
	price: 45.5,
	owner: ...
}
```



## /network

```json
{
	id: 0,
	name: "...",
	...
}
```



## /network/content

```json
{
	id: 0,
	title: "project X",
	owner: ...,
	...
}
```





## /network/id_person

```json
{
	id: 1518,
	surname: "Julie",
	lastname: "...",
	posts_ids: [354, 63755, 798785, ...],
	...
}
```



## /network/post

```json
{
	id: 175948,
    title: "Progress of websemantic",
    content: "The last decades...",
    ...
}
```



## /messenger

```json
{
	id: 34892,
	title: "About the exam session"
	content: "Dear professor...",
	labels: ["exams", "physics", ...],
	...
}
```

