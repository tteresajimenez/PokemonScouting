def test_list_pokemon_empty(client):
    response = client.get("/pokemon")
    assert response.status_code == 200
    assert response.json == []


def test_add_pokemon(client):
    response = client.post(
        "/pokemon",
        json={"name": "pikachu"}
    )

    assert response.status_code == 201
    assert response.json["name"] == "pikachu"


def test_list_pokemon_after_add(client):
    client.post("/pokemon", json={"name": "pikachu"})

    response = client.get("/pokemon")
    assert response.status_code == 200

    names = [p["name"] for p in response.json]
    assert "pikachu" in names

def test_delete_pokemon(client):
    client.post("/pokemon", json={"name": "pikachu"})

    response = client.delete("/pokemon/pikachu")
    assert response.status_code == 204


def test_delete_non_existing_pokemon(client):
    response = client.delete("/pokemon/mewtwo")
    assert response.status_code == 404
