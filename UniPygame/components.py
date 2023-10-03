from .commons import Vec2
class Component:
    def __init__(self):
        self.name = "component_default_name"
        self.id = 0
    def __str__(self):
        return self.name
    def apply(self, object):
        pass

class Collider(Component):
    def __init__(self):
        super().__init__()
        self.name = f"Collider_{self.id}"
def list_contains_type(lst : list, tpe):
    for i in lst:
        if type(i) == tpe:
            return i
    return Component()
class Ridgidbody(Component):
    def __init__(self):
        super().__init__()
        self.name = f"Ridgidbody_{self.id}"
        self._velocity = 0
        self._vertical_velocity = 0
        self.bouncieness = 0.0
        self.density = 1.0
        self.simulated = True
        self.apply_weight = True
        self.gravity_scale = 1.0
    def apply(self, object):
        if self.simulated:
            #Find all objects rect and put them into a list (Used for calculating collisions)
            colliders_in_scene = [i if (list_contains_type(i._components, Collider) and object.scene.__getbyEid__(object.id) != i) else None for i in object.scene._in_scene_entities]
            [colliders_in_scene.append(c) for c in [i if list_contains_type(i._components, Collider) and object.scene.__getbySid__(object.id) != i else None for i in object.scene._in_scene_sprites]]
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
            weight = surface_area / (object.GetComponent(Ridgidbody).density * 1000)
            #Calculate drag
            drag = object.rect.width / 100

            #Brake if moving upwards
            if (float(self._velocity) > 0.0):
                self._velocity -= (0.035 * self.gravity_scale) * drag
            self._velocity += (0.081 * self.gravity_scale) * (weight if self.apply_weight else 1) if not grounded else self._velocity * float(hit_object.GetComponent(Ridgidbody).bouncieness - 1 if hit_object.HasComponent(Ridgidbody) else -1)
            if abs(self._velocity) != self._velocity:
                self._velocity = self._velocity if self._velocity < 0.001 else 0

            object.position.y += self._velocity
            object.position.x += self._vertical_velocity
    def AddVelocity(self, velocity : Vec2):
        self._velocity += velocity.y
        self._vertical_velocity += velocity.x