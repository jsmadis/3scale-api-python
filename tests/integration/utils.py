from threescale import resources


def assert_resource(resource: resources.DefaultResource):
    assert resource is not None
    assert resource.entity_id is not None
    assert resource.entity is not None


def assert_resource_params(obj: resources.DefaultResource, params: dict, allowed=None):
    for (key, val) in params.items():
        if allowed is not None and key in allowed:
            assert obj[key] == val, f"Resource value for key \"{key}\" should be correct."
            assert obj.entity[key] == val, "Entity value for key \"{key}\" should be correct."
