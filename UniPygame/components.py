class Component:
    def __init__(self):
        self.name : str = "component_default_name"
        self.id = 0
    def __str__(self):
        return self.name
    def apply(self, object):
        print(self.name)
        print(object.position)

class Collider(Component):
    def __init__(self):
        super().__init__()
        self.name = f"Collider_{self.id}"
    def apply(self, object):
        pass
def list_contains_type(lst : list, tpe) -> Component:
    for i in lst:
        if type(i) == tpe:
            return i
    return Component
class Ridgidbody(Component):
    def __init__(self):
        super().__init__()
        self.name = f"Ridgidbody_{self.id}"
        self.velocity = 0
        self.bouncieness = 0.0
        self.density = 1.0
        self.simulated = True
        self.gravity_scale = 1.0
    def apply(self, object):
        if self.simulated:
            #Find all objects rect and put them into a list (Used for calculating collisions)
            colliders_in_scene = [i if (list_contains_type(i._components, Collider) and object.scene.__getbyEid__(object.id) != i) else None for i in object.scene._in_scene_entities]
            [colliders_in_scene.append(c) for c in [i if list_contains_type(i._components, Collider) and object.scene.__getbySid__(object.id) else None for i in object.scene._in_scene_sprites]]
            while None in colliders_in_scene:
                colliders_in_scene.pop(colliders_in_scene.index(None))

            #Collision detection
            collision = object.rect.collidelist(colliders_in_scene)
            grounded = True if collision != -1 else False
        
            #Get collided object
            try:
                hit_object = colliders_in_scene[collision]
            except (ValueError, IndexError):
                hit_object = object
            #Calculate the surface area
            surface_area = object.rect.width * object.rect.height
            #Calculate weight
            weight = surface_area / (object.get_component(Ridgidbody).density * 1000)
            #Calculate drag
            drag = object.rect.width / 100

            #Brake if moving upwards
            if (float(self.velocity) < 0.0):
                self.velocity += (0.035 * self.gravity_scale) * drag

            self.velocity -= (0.081 * self.gravity_scale) * weight if not grounded else self.velocity * float(hit_object.get_component(Ridgidbody).bouncieness + 1)
            if abs(self.velocity) == self.velocity:
                self.velocity = self.velocity if self.velocity > 0.001 else 0

            object.position.y -= self.velocity
            #print(hit_object, collision, colliders_in_scene, grounded, self.velocity, object.position.y)