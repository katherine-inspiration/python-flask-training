from middleware import *
from flask import jsonify


def initialize_routes(app):
    app.add_url_rule("/api/hello/", "hello", hello)
    app.add_url_rule("/api/db/", "db", db)
    app.add_url_rule("/api/hello_from/", "hello_from", hello_from)
    app.add_url_rule("/api/", "list_routes", list_routes, defaults={'app': app})


def list_routes(app):
    for route in app.url_map.iter_rules():
        print(route.methods, route.endpoint, '-', route)
    return "Routes Info Goes Here"
