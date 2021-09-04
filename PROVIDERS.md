# Providers API
## Create Provider
### Request
``` POST /providers/```
```
{
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```

### Response
```
{
	"id": 1,
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```

## Delete Provider
### Request
``` DELETE /providers/id```
### Response
```
HTTP/1.1 204 0
```
## Update Provider
### Request
``` PUT /providers/id```
```
{
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```

### Response
```
{
	"id": 1,
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```
## Update Provider Partially
### Request
``` PATCH /providers/id```
```
{
	"name": "new Revisto",
	"email": "anotherRevisto@revs.ir",
}
```

### Response
```
{
	"id": 1,
	"name": "new Revisto",
	"email": "anotherRevisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```
## View Specific Provider
### Request
``` GET /providers/id```

### Response
```
{
	"id": 1,
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
}
```
## Get list of providers
### Request
``` GET /providers/```

### Response
```
{
	"id": 1,
	"name": "Revisto",
	"email": "Revisto@revs.ir",
	"phone_number": "+548746487",
	"language": "Persian",
	"currency": "IRR"
},
{
	"id": 2,
	"name": "Revider",
	"email": "Revider@revs.ir",
	"phone_number": "+641857484",
	"language": "English",
	"currency": "Pound"
}
```