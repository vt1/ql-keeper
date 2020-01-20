import pytest
import json

from django.test import RequestFactory
from .. import schema
from graphene.test import Client
from .data import initdata_users, initdata_categories, get_user


pytestmark = pytest.mark.django_db


def test_users():
    initdata_users()

    client = Client(schema)
    executed = client.execute("""query 
                                 {
                                     users
                                     {
                                        username
                                     }
                            }""")
    expected = {
        "data": {
            "users": [
              {
                "username": "testUser"
              },
              {
                "username": "testUser2"
              }
            ]
        }
    }
    executed_json = json.dumps(executed)
    assert executed == expected


def test_categories():
    initdata_users()
    initdata_categories()

    client = Client(schema)
    executed = client.execute("""query 
                                     {
                                         categories
                                         {
                                            title
                                         }
                                }""")
    expected = {
        "data": {
            "categories": [
                {
                    "title": "Category1"
                },
                {
                    "title": "Category2"
                },
                {
                    "title": "Category3"
                }
            ]
        }
    }
    executed_json = json.dumps(executed)
    assert executed == expected


def test_userbyid():
    initdata_users()
    client = Client(schema)
    executed = client.execute("""query 
                                 {
                                     user(userid:5)
                                     {
                                        username
                                     }
                            }""")
    expected = {
        "data": {
            "user": {
                "username": "testUser"
            }
        }
    }
    assert executed == expected


def test_mutations_create():
    initdata_users()

    req = RequestFactory().get('graphql/')
    req.user = get_user(7)
    client = Client(schema)
    executed = client.execute("""mutation CategoryMutation {
                                    createCategory(title:"UnitTestGraphQL"){
                                        category {
                                        title
                                        }        
                                    }
                                }""", context=req)
    expected = {
        "data": {
            "createCategory": {
                "category": {
                    "title": "UnitTestGraphQL"
                }
            }
        }
    }
    assert executed == expected


def test_mutations_update():
    initdata_users()
    initdata_categories()

    client = Client(schema)
    executed = client.execute("""mutation CategoryMutation {
                                    updateCategory(categoryid: 5, title: "TestCategoryUPD") {
                                        category {
                                            title      
                                            }
                                        }
                                    }""")
    expected = {
        "data": {
            "updateCategory": {
                "category": {
                    "title": "TestCategoryUPD"
                }
            }
        }
    }
    assert executed == expected