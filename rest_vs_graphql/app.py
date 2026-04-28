from flask import Flask, request, jsonify
import graphene

app = Flask(__name__)

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())

    def resolve_user(root, info, id):
        return {"id": id, "name": "alex"}

schema = graphene.Schema(query=Query)

@app.route("/graphql", methods=["GET", "POST"])
def graphql():
    if request.method == "GET":
        query = request.args.get("query")
    elif request.is_json:
        query = request.get_json()["query"]
    else:
        query = request.form.get("query")

    result = schema.execute(query)
    return jsonify(result.data)

app.run(port=8000)
