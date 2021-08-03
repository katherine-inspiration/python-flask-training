from middleware import *
from flask import jsonify


def initialize_routes(app):
    app.add_url_rule("/api/hello/", "hello", hello)
    app.add_url_rule("/api/db/", "db", db)
    app.add_url_rule("/api/hello_from/", "hello_from", hello_from)
    app.add_url_rule("/api/", "list_routes", list_routes, defaults={'app': app})
    app.add_url_rule("/api/persons/", "persons", persons)
    app.add_url_rule("/api/persons/", "person_add", person_add, methods=["POST"])
    app.add_url_rule("/api/persons/", "person_update", person_update, methods=["PUT"])


def list_routes(app):
    route_list = {}
    for route in app.url_map.iter_rules():
        route_dict = {
            "Route": str(route),
            "Endpoint": route.endpoint,
            "Methods": list(route.methods)
        }
        route_list[route.endpoint] = route_dict
    return jsonify({"Routes": route_list, "Total": len(route_list)})
