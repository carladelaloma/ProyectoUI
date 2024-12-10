bl_info = {
    "name": "MyFirstAddon",
    "description": "Sample",
    "author": "Carla",
    "version": (0, 0, 1),
    "blender": (4, 2, 3),
    
    "location": "View3D > Sidebar > Herramientas Artista 3D",
    "category": "Development",
}


import bpy

def move_obj_to_worldorigin():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
        obj.location = (0, 0, 0)
        obj.select_set(True)


class MESH_OT_move_to_worldorigin(bpy.types.Operator):
    """Mover el origen de un objeto al del mundo"""
    
    bl_idname = "mesh.move_to_worldorigin"  # Para que sea único y lo pueda llamar desde el panel
    bl_label = "Mover al origen del mundo"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        move_obj_to_worldorigin()  # Llamar la función para mover al origen del mundo
        return {"FINISHED"}


class TestPanel(bpy.types.Panel):
    bl_label = "Herramientas"   # Nombre del panel
    bl_region_type = "UI"       # Zona de la pantalla
    bl_space_type = "VIEW_3D"   # Vista 3D
    bl_category = "Herramientas Artista 3D" # Nombre de la pestaña
    bl_idname = "3D_VIEW_PT_HerramientasArtista3D" # Prevenir duplicados
    
    def draw(self, context):
        layout = self.layout
        
        # Crear una fila nueva
        row = layout.row()
        row.label(text="Mover el objeto", icon="UNPINNED")
        
        # Botón para ejecutar el operador
        row = layout.row()
        row.operator("mesh.move_to_worldorigin", icon="TRACKER")  # Referencia al operador creado


# REGISTRAR LA CLASE

def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(MESH_OT_move_to_worldorigin)


def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(MESH_OT_move_to_worldorigin)

if __name__ == "__main__":
    register()
