from flask import jsonify, request, abort


people_info = [
    {
        'name': "Jack The Sparrow",
        'age': 40,
        'occupation': 'pirate'
    },
    {
        'name': "Freddie Mercury",
        'age': 38,
        'occupation': 'rockstar'
    },
    {
        'name': "Katty Perry",
        'age': 30,
        'occupation': 'singer'
    },
]

def persons():
    return jsonify(people_info)


def person_add():
    try:
        data = request.get_json(force=True)
        name = data["name"]
        age = data["age"]
        occupation = data["occupation"]
        if name and age and occupation:
            people_info.append({"name": name, "age": age, "occupation": occupation})
            return jsonify({"Person " + name: "Added successfully"})
    except Exception as exc:
        print(exc)
        abort(400)



def hello():
    return "Hello world from Flask :)"


def hello_from():
    return "Hello from Ekaterina and Evgenia!"


def db():
    return "Hello DB Grads!"


def person_update():

    try:
        data = request.get_json(force=True)
        name = data["name"]
        age = data["age"]
        occupation = data["occupation"]
        if age and name and occupation:
            for i in range(len(people_info)):
                if people_info[i]["name"] == name:
                    people_info[i]["age"] = age
                    people_info[i]["occupation"] = occupation
                    return jsonify({"Person " + name: "Updated"})

            abort(400)
        else:
            abort(400)
    except Exception as exc:
        print(exc)
        abort(400)




