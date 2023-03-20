

### health
```
curl --request GET \
  --url http://localhost:8000/v1/health
```


### create

```
curl --request POST \
  --url http://localhost:8000/v1/movies \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "MH370 Netflix",
	"description": "Malaysia Airlines"
}'
```

### all

```
curl --request GET \
  --url http://localhost:8000/v1/movies
```


### movie by id

```
curl --request GET \
  --url http://localhost:8000/v1/movies/75241253-73bc-43f8-a210-730eb41b6fe0
```

### delete by id

```
curl --request DELETE \
  --url http://localhost:8000/v1/movies/a4176e9e-f61f-451f-8aec-d76206df15df
```

### update (patch)

```
curl --request PATCH \
  --url http://localhost:8000/v1/movies \
  --header 'Content-Type: application/json' \
  --data '{
	"id": "f8c22aa5-d301-48b6-95ee-eae0420a6229",
	"title": "MH370 Netflix",
	"description": "Malaysia Airlines que llevaba 239 personas a bordo desapareció de los radares."
}'
```