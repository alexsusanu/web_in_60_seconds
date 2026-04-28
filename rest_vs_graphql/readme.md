pip install flask graphene flask-graphqp install flask graphene flask-graphql

----------------------


You’re building a page that shows:

user name
last 5 orders
for each order → items + price
total spend


REST:

GET /user/1
GET /orders?user_id=1
GET /orders/101/items
GET /orders/102/items
GET /orders/103/items
GET /orders/104/items
GET /orders/105/items

GraphQL:

query {
  user(id: 1) {
    name
    orders(limit: 5) {
      id
      total
      items {
        name
        price
      }
    }
  }
}

-----------------------


Internal tooling / DevOps dashboard

You’re building a page that shows:

list of Kubernetes pods
for each pod → logs (last 10 lines)
for each pod → node info
for each pod → restart count

REST:

GET /pods

[
  {"id": "pod-1", "node_id": "node-1"},
  {"id": "pod-2", "node_id": "node-2"}
]

GET /pods/pod-1/logs
GET /pods/pod-1/stats
GET /nodes/node-1

GET /pods/pod-2/logs
GET /pods/pod-2/stats
GET /nodes/node-2

GraphQL:

query {
  pods {
    id
    logs(last: 10)
    restartCount
    node {
      name
      cpu
    }
  }
}

REST → you either make many calls OR keep adding custom endpoints
GraphQL → you make one query and let the backend resolve across services
